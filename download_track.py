#!/usr/bin/python
import sys
import os
import subprocess

def download(slsk):
    command = ['museekcontrol', '--download', slsk]
    p = subprocess.Popen(command, stdout=subprocess.PIPE) 
    text = p.stdout.read()
    retcode = p.wait()
    print(text)
    return retcode

def search(query):
    command = ['museekcontrol', '--gsearch', query]
    p = subprocess.Popen(command, stdout=subprocess.PIPE) 
    text = p.stdout.read()
    retcode = p.wait()
    print(text)
    print(retcode)

    results = text.split('---------')
    users = []
    slsk = []
    size = []
    bitrate = []
    filetype = [] 
    ret = []
    for r in results:
        r = r.strip()
        subresults = r.split('\n')
        user = subresults[0][subresults[0].find('User'):]
        users.append(user)
        # print(r)
        # print('USER: {}'.format(user))
        for s in subresults[1:]:
            if 'slsk://' in s:
    	        slsk.append(s[s.find('slsk://'):])
    	        filetype.append(os.path.splitext(s[s.find('slsk://'):])[1])
    	    if 'Size' in s:
    	        size.append(s[s.find('Size: '):s.find('Bitrate: ')].replace('Size: ', ''))
    	        bitrate.append(s[s.find('Bitrate: '):s.find('Length: ')].replace('Bitrate: ', ''))
    	        # filetype.append(s[s.find('filetype:'):])    

    return users, slsk, size, bitrate, filetype

if __name__ == '__main__':
    users, slsk, size, bitrate, filetype= search(sys.argv[1])
    for user, slsk, size, bitrate, filetype in zip(users, slsk, size, bitrate, filetype):
        print(user, slsk, size, bitrate, filetype)
        if 'flac' in filetype or 'wav' in filetype: 
            if 'feat' not in slsk.lower() and 'ft.' not in slsk.lower() and 'remix' not in slsk.lower() and 'instrumental' not in slsk.lower():
                print(user, slsk, size, bitrate, filetype)
                download(slsk)
                break



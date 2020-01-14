import csv
import sys
import subprocess


with open(sys.argv[1], "r") as f:
    reader = csv.reader(f) 
    next(reader, None)
    for i, line in enumerate(reader):
        track = line[0]
        artist = line[1]
        # print(track, artist)
        query = '{} {}'.format(track, artist)
        print('Searching: {}'.format(query))
        cmd = ['docker', 'exec', '-it', 'museek', '/download_track.py', query]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        text = p.stdout.read()
        retcode = p.wait()
        print(text)
        print(retcode)
        # break

import requests
import os,sys

from config import *

def read_input(day,test=False):
    if len(sys.argv) > 1:
        if sys.argv[1] == "-t": test=True
    if test: path = f"tmp/{day}-test.txt"
    else: path = f"tmp/{day}.txt"
    if not os.path.isfile(path):
        if test:
            print("reading from stdin... ^D when finished")
            data = sys.stdin.read()
        else:
            print("caching...")
            r = requests.get(f"https://adventofcode.com/{year}/day/{day}/input",cookies={'session':session})
            data = r.content.decode()
        with open(path,"w") as f: f.write(data)
    else:
        with open(path,"r") as f: data = f.read()
    return data.splitlines()

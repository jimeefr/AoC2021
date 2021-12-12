import requests
import os

with open("session.txt","r") as f: sess=f.read()

def read_input(day):
    path = f"tmp/{day}.txt"
    if not os.path.isfile(path):
        print("caching...")
        r = requests.get(f"https://adventofcode.com/2021/day/{day}/input",cookies={'session':sess})
        data = r.content.decode()
        with open(path,"w") as f: f.write(data)
    else:
        with open(path,"r") as f: data = f.read()
    return data.splitlines()

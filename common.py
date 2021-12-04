import requests

with open("session.txt","r") as f: sess=f.read()

def read_input(day):
    r = requests.get(f"https://adventofcode.com/2021/day/{day}/input",cookies={'session':sess})
    return r.content.decode().splitlines()
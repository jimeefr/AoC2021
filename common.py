import requests

sess=open("session.txt","r").read()

def read_input(day):
    r = requests.get(f"https://adventofcode.com/2021/day/{day}/input",cookies={'session':sess})
    c = r.content.decode()
    data = c.split('\n')
    while data[-1] == '': data.pop()
    return data
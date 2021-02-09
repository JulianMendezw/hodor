#!/usr/bin/python3

from requests import post

# This is a url where we want to scraping
url = 'http://158.69.76.135/level0.php'

# This is how we want to do in the page
input_data = {'id': 2358, 'holdthedoor': 'submit'}

for i in range(1024):
    resp = post('http://158.69.76.135/level0.php', data=input_data)
    print("votacion: {}".format(i), end='\r', flush=True)

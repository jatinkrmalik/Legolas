from goose3 import Goose
import sys
import os
import time
import re
from slackclient import SlackClient

url = sys.argv[1] 

#g = Goose()
g = Goose({'enable_image_fetching': True})

article = g.extract(url=url)

#import pdb; pdb.set_trace()

print('Title: ', article.title)
print('-'*15)
print('TL;DR: ', article.meta_description)
print('-'*15)
print('Top image: ', article.top_image.src)
print('-'*15)
print('Ad-free article:\n', article.cleaned_text)
print('='*15)
print("Beep blop beep, I am a bot. Please drop a mail to jatinkrmalik@gmail.com to report a bug")
print('='*15)

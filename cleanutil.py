from goose3 import Goose
import sys

def cleanup(url):
    #g = Goose()
    g = Goose({'enable_image_fetching': True})
    
    article = g.extract(url=url)
    
    #import pdb; pdb.set_trace()
    response = {}
    response['title'] = article.title
    # print('Title: ', article.title)
    # print('-'*15)
    response['tldr'] = article.meta_description
    # print('TL;DR: ', article.meta_description)
    # print('-'*15)
    response['img'] = article.top_image.src
    # print('Top image: ', article.top_image.src)
    # print('-'*15)
    response['post'] = article.cleaned_text
    #print('='*15)
    response['disc'] = "Beep blop beep, I am a bot. Please drop a mail to jatinkrmalik@gmail.com to report a bug"
    # print("Beep blop beep, I am a bot. Please drop a mail to jatinkrmalik@gmail.com to report a bug")
    # print('='*15)
    return response

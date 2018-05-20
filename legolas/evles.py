"""elves.py: contains magical methods for legolas to perform."""

__author__ = "Jatin K Malik"
__email__ = "jatinkrmalik@gmail.com"
__version__ = "0.1.1"
__status__ = "Beta version"

from goose3 import Goose
import sys

def witchcraft(url):
    """
    Return a clean ad free string for the url given in the params.
    
    Arguments:
        url {string} -- url of the page to extract information from.
    
    Returns:
        string -- a clean string containing title, tldr, image and post.
    """

    #g = Goose()
    g = Goose({'enable_image_fetching': True})
    
    article = g.extract(url=url)
    
    # import pdb; pdb.set_trace()
    # response = {}
    response = ""
    # response['title'] = article.title
    response += "\n*Title:* " + str(article.title) + '\n'
    response += '-'*15
    # response['tldr'] = article.meta_description
    response += '\n *TL;DR:* ' + str(article.meta_description) + '\n'
    response += '-'*15
    # response['img'] = article.top_image.src
    try:
        img = article.top_image.src
        response += '\n*Post image:* ' +  str(img) + ' \n'
        response += '-'*15
    except:
        print("No image found.")
    # response['post'] = article.cleaned_text
    response += '\n *Ad-free Post:*\n' + str(article.cleaned_text) + '\n'
    #print('='*15)
    response += '-'*15
    response += "\n *Original url:* " + str(url) + '\n\n\n'
    response += '='*25
    # response['disc'] = "Beep blop beep, I am a bot. Please drop a mail to jatinkrmalik@gmail.com to report a bug"
    response += "\n_Beep blop beep, I am a bot. Please drop a mail to jatinkrmalik@gmail.com to report a bug._\n"
    # print('='*15)
    response += '='*25

    return response

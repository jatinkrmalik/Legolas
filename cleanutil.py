from goose3 import Goose
import sys

def cleanup(url):
    #g = Goose()
    g = Goose({'enable_image_fetching': True})
    
    article = g.extract(url=url)
    
    # import pdb; pdb.set_trace()
    # response = {}
    response = ""
    # response['title'] = article.title
    response += "\n **Title:** " + str(article.title) + '\n'
    response += '-'*15
    # response['tldr'] = article.meta_description
    response += '\n **TL;DR:** ' + str(article.meta_description) + '\n'
    response += '-'*15
    # response['img'] = article.top_image.src
    # response += '\nTop image: ' +  str(article.top_image.src)
    # response += '-'*15
    # response['post'] = article.cleaned_text
    response += '\n **Post:** ' + str(article.cleaned_text) + '\n\n\n'
    #print('='*15)
    response += '='*15
    # response['disc'] = "Beep blop beep, I am a bot. Please drop a mail to jatinkrmalik@gmail.com to report a bug"
    response += "\n_Beep blop beep, I am a bot. Please drop a mail to jatinkrmalik@gmail.com to report a bug._\n"
    # print('='*15)
    response += '='*15

    return response

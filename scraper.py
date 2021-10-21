from requests_html import HTMLSession
from bs4 import BeautifulSoup

from mailer import Emailer

class Scraper(object):
    '''
    Main web scraping object. Takes in a URL and requested data point such as 
    price or title of the object and returns a string of that data.
    '''

    def __init__(self):

        test = Emailer()
        s = HTMLSession()
        URL = 'https://smile.amazon.com/dp/0593298683'
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
        'Accept-Language' : 'en-US,en;q=0.5',
        'Accept-Encoding' : 'gzip', 
        'DNT' : '1',
        'Connection' : 'close'}

        r = s.get(URL, headers=header)

        soup = BeautifulSoup(r.text, "html.parser")

        results = soup.find(id='price')

        print(results.get_text())

        print('Trying to send an email...')
        test.sendMessage(
            '''\
            Hey there! This is a test email, where the price for the item is {}!
            '''.format(results.get_text())
            )
        print('Email sent.')

if __name__ == '__main__':
    scraper = Scraper()
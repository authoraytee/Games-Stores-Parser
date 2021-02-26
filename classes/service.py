import requests
from bs4 import BeautifulSoup

class Service():

    def __init__(self, basicLink, game, convertNameSign, tag, htmlclass):
        self.basicLink = basicLink
        self.game = game
        self.convertNameSign = convertNameSign
        self.tag = tag
        self.htmlclass = htmlclass

    def __convertGameNameAndJoinToLink(self, link, game, sign):
        game = sign.join(game)
        link = link.format(game)
        return link

    def __getRequest(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        return soup

    def __parse(self, url, soup, tag, htmlclass):

        soup = self.__getRequest(url)


        try:
            quotes = soup.find(tag, class_=htmlclass)
            quotes = quotes.text.split()
            price = quotes[0]
            return price
        except:
            return 'Game is out of stock or entered incorrectly!'

    def output(self)
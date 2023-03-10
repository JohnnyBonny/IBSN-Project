from bs4 import BeautifulSoup
import requests

#9780679863717

def getBookInformation(ibsn):
    URL = "https://www.bookfinder.com/search/?isbn=" + ibsn + "&mode=isbn&st=sr&ac=qr"
    res = requests.get(URL)

    obj = BeautifulSoup(res.content, 'html.parser')

    title = obj.find(id='describe-isbn-title')
    print(BeautifulSoup.get_text(title))

    author = obj.find(itemprop='author')
    print(BeautifulSoup.get_text(author))
    #return title, author

def main():
    ibsn = input("Enter the IBSN of the book ")
    getBookInformation(ibsn)

main()
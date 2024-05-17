from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.myjobmag.com/').text
soup = BeautifulSoup('html_text', 'lxml')
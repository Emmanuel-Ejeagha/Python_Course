from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.myjobmag.com/').text
soup = BeautifulSoup('html_text', 'lxml')

company_name = soup.find('li', class_="job-desc")
# date_posted = soup.find('div', class_='read-date-sec-li')
# job_info = soup.find(class_='job-key-info').text
# job_details = soup.find(class_='job-details')
print(company_name)
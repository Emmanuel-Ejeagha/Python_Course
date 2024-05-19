from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.myjobmag.com/').text
soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li', class_="job-list-li")

for job in jobs:
    company_name = job.find('h2').text if job.find('h2') else 'N/A'
    job_desc = job.find('li', class_='job-desc').text if job.find('li', class_='job-desc') else 'N/A'
    job_date = job.find('li', id='job-date').text if job.find('li', id='job-date') else 'N/A'
    job_desc = job.find('li', class_='mag_b')
    print(f'''
    Company name: {company_name}
    Company Info: {job_desc}
    Date posted: {job_date}
    ''')

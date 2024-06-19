from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
    
    html_text = requests.get('https://www.myjobmag.com/').text
    soup = BeautifulSoup(html_text, 'lxml')

    # Find all job-list-li elements
    jobs = soup.find_all('li', class_="job-list-li")
    for index, job in enumerate(jobs):
        # Extract the job title and link
        job_info = job.find('li', class_="job-info")
        if job_info:
            title_element = job_info.find('h2').find('a') if job_info.find('h2') else None
            if title_element:
                job_title = title_element.text.strip()
                job_link = title_element['href']
            else:
                job_title = 'N/A'
                job_link = 'N/A'
            
            # Extract the job description
            job_desc = job_info.find('li', class_='job-desc').text.strip() if job_info.find('li', class_='job-desc') else 'N/A'
            
            # Extract the job date
            job_date = job_info.find('li', id='job-date').text.strip() if job_info.find('li', id='job-date') else 'N/A'
            
            with open(f'posts/{index}.txt', 'w') as f:
                f.write(f'Job Title: {job_title}\n')
                f.write(f" Job Link: {job_link}\n")
                f.write(f"Job Description: {job_desc}\n")
                f.write(f"Date Posted: {job_date}\n")
                

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1
        
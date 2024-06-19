#!/usr/bin/python3

# importing the modules
from bs4 import BeautifulSoup

# opening and reading a file
with open('templates/index.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    
    listing = soup.find_all('h1')
    courses = soup.find_all('div', class_='card')
    # print(course)
    
    for course in courses:
        course_name = course.h5.text
        course_prince = course.a.text
        
        print(course_name)
        print(course_prince)

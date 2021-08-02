from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    company_name = job.header.h3.text.replace(' ', '')
    skills = job.find('span', class_='srp-skills').text.replace(' ', '')

    published_date = job.find('span', class_='sim-posted').span.text
    if published_date == "Posted few days ago":
        print(f'''Company Name: {company_name}Required Skills: {skills}''')

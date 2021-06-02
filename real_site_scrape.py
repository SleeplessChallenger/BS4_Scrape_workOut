from bs4 import BeautifulSoup
import requests


html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html'
						 '?searchType=personalizedSearch&from=submit&txtKeywords'
						 '=python&txtLocation=').text
# (above) we used .text as otherwise it'll return status code

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
# we can decrease our scale to detached elements

for job in jobs:
	job_dates = job.find('span', class_='sim-posted').span.text
	# double span as there is nested span inside outer span

	if job_dates != 'Posted few days ago':
		continue

	elif 'few' in job_dates:
		company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
		# (above) we used `replace` so as to bypass unnecessary whitespaces

		skills = job.find('span', class_='srp-skills').text.replace(' ', '')

		print(f'''
Comapny; {company_name},
Skills: {skills}
''')

from bs4 import BeautifulSoup
import requests
import time
import pathlib
import uuid

file_root = pathlib.Path.cwd()


def check(unKnownOnes, skills):
	skills = skills.strip().split(',')
	for skill in skills:
		if skill in unKnownOnes:
			return False
	return True


noSkill = input('Write undesired skill: ').lower()


def find_jobs():
	html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html'
							 '?searchType=personalizedSearch&from=submit&txtKeywords'
							 '=python&txtLocation=').text
	# (above) we used .text as otherwise it'll return status code

	soup = BeautifulSoup(html_text, 'lxml')
	jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
	# we can decrease our scale to detached elements

	c = noSkill.split()

	all_data = []

	for job in jobs:
		job_dates = job.find('span', class_='sim-posted').span.text
		# double span as there is nested span inside outer span

		if job_dates != 'Posted few days ago':
			continue

		elif 'few' in job_dates:
			company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
			# (above) we used `replace` so as to bypass unnecessary whitespaces

			skills = job.find('span', class_='srp-skills').text.replace(' ', '')

			more_info = job.header.h2.a['href']

			if check(c, skills):

				temp = 	f'''Company: {company_name.strip()},
Skills: {skills.strip()},
More info: {more_info.strip()}

'''

				all_data.append(temp)

				path_ = pathlib.Path(f"{file_root}/saved_posts").mkdir(parents=True, exist_ok=True)
				path_ = path_ if path_ is not None else f"{file_root}/saved_posts"

				print(f"Company: {company_name.strip()}")
				print(f"Skills: {skills.strip()}")
				print(f"More info: {more_info.strip()}")
				print('')

	name = str(uuid.uuid4())

	with open(f"{path_}/{name}", 'w') as fl:
		for item in all_data:
			fl.write(item)


if __name__ == '__main__':
	while True:
		try:
			find_jobs()
			time.sleep(600)
		except KeyboardInterrupt:
			print('さようなら')
			break

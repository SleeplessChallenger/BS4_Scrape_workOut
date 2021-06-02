from bs4 import BeautifulSoup


with open('home.html', 'r') as file:
	content = file.read()

	soup = BeautifulSoup(content, 'lxml')
	courses = soup.find_all('div', class_='card')

	for course in courses:
		course_name = course.h5.text
		course_price = course.a.text
		exact_price = course_price.split()[-1]

		print(f"{exact_price} for {course_name}")

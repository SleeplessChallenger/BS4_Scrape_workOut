from bs4 import BeautifulSoup


with open('home.html', 'r') as file:
	content = file.read()

	soup = BeautifulSoup(content, 'lxml')
	tags = soup.find('h5')
	tags_all = soup.find_all('h5')

	for course in tags_all:
		print(course)

	print(tags)
	# `find()` searches for first element
	# `find_all()` searches for all elements

	# print(soup.prettify())
	# `prettify()` is to present html nicer

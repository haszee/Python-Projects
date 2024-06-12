import requests
import bs4
import re

'''
GET CONTENTS OF TABLE OF CONTENTS FROM WIKIPEDIA PAGE
'''
# result = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')

# soup = bs4.BeautifulSoup(result.text, 'lxml')

# site_title = soup.select('title')[0].getText()

# site_class = soup.select('.vector-toc-text')

# print(site_title)

# site_class.pop(0)

# for item in site_class:
#     item = re.findall(r'[^\d.]+',item.text.strip())
#     print("".join(item))

'''
GET IMAGE FROM WIKIPEDIA PAGE AND SAVE IT IN A FILE
'''
# res = requests.get('https://en.wikipedia.org/wiki/Wikipedia:Ten_things_you_may_not_know_about_images_on_Wikipedia')
# soup = bs4.BeautifulSoup(res.text, 'lxml')

# building = soup.select('.mw-file-element')[1]['src']

# image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/%D0%9B%D0%B0%D0%B2%D1%80%D0%B8%D0%BA%D0%B8%2C_%D0%B1%D1%80%D0%BE%D1%88%D0%B5%D0%BD%D0%B0%D1%8F_%D0%B3%D1%80%D0%B0%D0%B4%D0%B8%D1%80%D0%BD%D1%8F_%D1%81%D0%B2%D0%B5%D1%80%D1%85%D1%83_%282%29.jpg/245px-%D0%9B%D0%B0%D0%B2%D1%80%D0%B8%D0%BA%D0%B8%2C_%D0%B1%D1%80%D0%BE%D1%88%D0%B5%D0%BD%D0%B0%D1%8F_%D0%B3%D1%80%D0%B0%D0%B4%D0%B8%D1%80%D0%BD%D1%8F_%D1%81%D0%B2%D0%B5%D1%80%D1%85%D1%83_%282%29.jpg')

# f = open('my_image.jpg', 'wb') # wb = write in binary
# f.write(image_link.content)
# f.close()

'''
SCRAPE THE BOOK LISTINGS & GET ALL BOOKS WITH A 2 STAR RATING FROM ALL PAGES
'''

# books_url = 'https://books.toscrape.com/catalogue/page-{}.html'

# titles = []

# for page in range(1,51):
# 	res = requests.get(books_url.format(page))
# 	soup = bs4.BeautifulSoup(res.text, 'lxml')
# 	all_books = soup.select('.product_pod')
# 	for book in all_books:
# 		if book.select('.star-rating.Two'):
# 			titles.append(book.select('a')[1]['title'])

# print(titles)

'''
PRINT ALL UNIQUE QUOTED AUTHORS IN ALL THE PAGES
'''

quotes_url = 'http://quotes.toscrape.com/page/{}'
page = 1
authors = set()

while True: # last_page = False
	res = requests.get(quotes_url.format(page))
	if 'No quotes found!' in res.text: # you figure this out by trying a page that is out of range
		print(f'You are on page {page-1}. This is the last page.')
		break
	else:
		soup = bs4.BeautifulSoup(res.text, 'lxml')
		all_authors = soup.select('.author')
		for name in all_authors:
			authors.add(name.text)
	page += 1

print(authors)

# from turtle import ht
from bs4 import BeautifulSoup
import ipdb
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)

doc = BeautifulSoup(html.text, 'html.parser')

# print(doc.select('.heading-primary')[0].contents)

courses = doc.select('.heading-20-semibold')
print(doc.select('.heading-20-semibold'))
print("testing")
print(doc.select('.heading-20-semibold')[0])
print("testing")
for course in courses:
    print(course.contents[0].strip())
ipdb.set_trace()

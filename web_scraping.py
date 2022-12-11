# bs4 for html parsing and urllib.request for getting html file
from bs4 import BeautifulSoup
import urllib.request

url = urllib.request.urlopen('https://ful.io')
urlData = url.read()

soup = BeautifulSoup(urlData, features='html5lib')

links = []
for link in soup.find_all('a'):
	data = link.get('href')
	if 'https' not in data and '@' not in data and 'tel' not in data:
		continue
	links.append(data)

socials = []
emails = []
contacts = []
for link in links:
	if 'http' in link:
		socials.append(link)
	elif 'mailto' in link:
		link  = link.replace('mailto:','')
		emails.append(link)
	else:
		link = link.replace('tel:','')
		contacts.append(link)

print("Social Links:")
for social in socials:
	print(social)

print("Emails:")
for email in emails:
	print(email)

print("Contacts:")
for contact in contacts:
	print(contact)
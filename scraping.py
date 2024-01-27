import requests
from bs4 import BeautifulSoup
url = "https://www.linkedin.com/jobs/"

r = requests.get(url)
htmlcontent = r.content
print(htmlcontent)

soup = BeautifulSoup(htmlcontent, "html.parser")
print(soup.prettify)


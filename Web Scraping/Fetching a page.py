import requests
from bs4 import BeautifulSoup
url = 'https://books.toscrape.com/'

header = {"Users-Agent" : "Mozilla/5.0" }
response = requests.get(url,headers=header)
print(response)
# print(response.status_code)
# print(response.text)    # HTML page 

if response.status_code == 200:
    html_string = response.text
    soup = BeautifulSoup(html_string, "lxml")
    print(soup.title.text)
    print(soup.find("h1").text)
    print(soup.title.text)
    print(soup.find("a"))
    print(soup.find("div", class_= "conatainer-fluid page"))
else:
    print("ERROR: ",{response.status_code})

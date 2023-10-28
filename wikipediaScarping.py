import requests
import pandas as pd
from bs4 import BeautifulSoup

html_text = requests.get("https://en.m.wikipedia.org/wiki/List_of_video_games_featuring_Mario").text

data = []

list_header = []
soup = BeautifulSoup(html_text,'lxml')
print(soup.find('table').get_text())
header = soup.find_all("table")[1].find("tr")

for items in header:
	try:
		list_header.append(items.get_text())
	except:
		continue
list_header.pop()

HTML_data = soup.find_all("table")[1].find_all("tr")[1:]


rowspan_name = ""
for no, element in enumerate(HTML_data):
	sub_data = []
	
	for sub_no, sub_element in enumerate(element):
		try:
			if sub_element.has_attr("rowspan"):
				rowspan_name = sub_element.get_text()

			sub_data.append(sub_element.get_text())

		except:
			continue
	sub_data = sub_data[:-1]
	if len(sub_data) < 4:
		sub_data.insert(0, rowspan_name)

	
	data.append(sub_data)


dataFrame = pd.DataFrame(data = data, columns = list_header)
dataFrame.to_csv('Mario.csv')

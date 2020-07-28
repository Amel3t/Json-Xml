import xml.etree.ElementTree as ET
from collections import Counter

with open('newsafr.json', encoding='UTF-8') as f:
    json_data = json.load(f)

new_list = json_data['rss']['channel']['items']
big_six = []
for news in new_list:
	for i in news['description'].split():
		if len(i) > 6:
			big_six.append(i)

new = Counter(big_six).most_common(10)
print(new)
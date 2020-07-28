import xml.etree.ElementTree as ET
from collections import Counter

parser = ET.XMLParser(encoding='UTF-8')
tree = ET.parse('newsafr.xml')
root = tree.getroot()
# print(root.tag)
# print(root.text)
# print(root.attrib)

# for child in root:
#     print(child.tag, child.attrib)

# print(root[0][1].text)
channel_node = root.find('channel')
# print(root.findall("myTag"))
# print(root[0].find("myOtherTag"))
items_list = channel_node.findall('item')
items_list2 = root.findall('channel/item/description')
new_list = []
new_list2 = []
for title in items_list2:
	new_list.append(title.text)
	# print(title.text)
# print((items_list2))
for i in new_list:
	new_list2.extend(i.split(' '))
# print(new_list[0])
# print(new_list[0].split(' '))

# print(new_list2)

word = [word for word in new_list2 if len(word) > 6]

new = Counter(word).most_common(10)
print(new)
from bs4 import BeautifulSoup
soup = BeautifulSoup(open("sample.gpx"))
#print(soup)
allWpt = soup.find_all("wpt")
print("all wpt count: %d", len(allWpt))
for i in range(len(allWpt)):
	currentWpt = allWpt[i]
	originalTag = currentWpt.contents[1]
	print(originalTag.name)
	originalTag = originalTag.name
	newTimeTag = soup2.new_tag("time")
	originalTag.append(newTimeTag)
	print(originalTag)
	#newTimeTag.string = "2010-01-01T00:00:00Z"
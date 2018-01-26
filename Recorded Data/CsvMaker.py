import csv
import requests
humanRows=[]
for x in range(5):
	humanRows.append([])
r = requests.get("http://flappybird.ma1geek.org/getScores.php").json()
for obj in r:
	if obj["user"] == "scottcrawshaw":
		if obj["user"] not in humanRows[0]:
			humanRows[0].append(obj["user"])
		humanRows[0].append(obj["score"])
	elif obj["user"] == "Zacha":
		if obj["user"] not in humanRows[1]:
			humanRows[1].append(obj["user"])
		humanRows[1].append(obj["score"])
	elif obj["user"] == "Jimmy":
		if obj["user"] not in humanRows[2]:
			humanRows[2].append(obj["user"])
		humanRows[2].append(obj["score"])
	elif obj["user"] == "ethanberman":
		if obj["user"] not in humanRows[3]:
			humanRows[3].append(obj["user"])
		humanRows[3].append(obj["score"])
	elif obj["user"] == "jessicawang":
		if obj["user"] not in humanRows[4]:
			humanRows[4].append(obj["user"])
		humanRows[4].append(obj["score"])

with open('learningtest.csv', 'w') as csvfile:
	filewriter = csv.writer(csvfile, delimiter=',',
	quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for row in humanRows:
		filewriter.writerow(row)
import urllib.request
import xml.etree.ElementTree as ET
import csv

url = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"
response = urllib.request.urlopen(url)
rss_content = response.read()

with open("rssfeed.xml", "wb") as file:
    file.write(rss_content)

tree = ET.parse("rssfeed.xml")
root = tree.getroot()

news_items = []
for item in root.findall(".//item"):
    news = {
        "title": item.find("title").text,
        "link": item.find("link").text,
        "description": item.find("description").text,
        "pubDate": item.find("pubDate").text
    }
    news_items.append(news)

csv_file = "news_items.csv"
with open(csv_file, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["title", "link", "description", "pubDate"])
    writer.writeheader()
    for news in news_items:
        writer.writerow(news)

print("Đã lưu các mục tin tức vào tệp CSV.")
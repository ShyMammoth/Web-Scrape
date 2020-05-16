import re

with open("careforsg.html", encoding='utf-8') as f:
    text = f.read()
    urls = re.findall(r'href="https:\/\/www\.tiktok\.com\/@[\'"]?([^\'" >]+)', text)
with open("all_href.txt", "w") as f:
    for item in urls:
        f.write("https://www.tiktok.com/@{}\n".format(item))
# print(', '.join(urls))
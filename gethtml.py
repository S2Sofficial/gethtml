#Get HTML Code of any website using Python 3

from urllib.request import urlopen
#Url of website which your want to get code
url = "https://swaroop2sky.github.io"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)
title_index = html.find("<title>")
title_index


#this command is for just to remove program finished line in the last
a=input()

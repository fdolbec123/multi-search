import urllib.request as url

with url.urlopen("https://www.google.ca/") as response:
    html = response.read()
    print(html)
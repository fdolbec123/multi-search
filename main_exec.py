import urllib.request as url
import urllib.parse as parse
from bs4 import BeautifulSoup as Bs4

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.1'
user_agent_end = '02 Safari/537.36'
user_agent = user_agent + user_agent_end

headers = {"User-Agent": user_agent}

base_google_url = "https://www.google.ca/search?q="
base_duck_duck_go = "https://duckduckgo.com/html?q="

terme = "pizza toute garnie"
terme_converti_en_html = parse.quote_plus(terme)

url_de_recherche_google = base_google_url + terme_converti_en_html
url_de_recherche_duck_duck_go = base_duck_duck_go + terme_converti_en_html

request_google = url.Request(url_de_recherche_google, None, headers)
request_duck_duck_go = url.Request(url_de_recherche_duck_duck_go, None, headers)

with url.urlopen(request_google) as response:
    html = response.read().decode('utf8')
    soup = Bs4(html, 'html.parser')

    g = soup.find_all("div", {"class": "g"})
    h3_results = []
    links_results = []
    print(g)
    g_list = list(g)
    descriptions_list = []
    for div_g in g:
        h3s = div_g.find_all("h3", {"class": "LC20lb"})
        for h3 in h3s:
            a = h3.text
            h3_results.append(a)
        hrefs = div_g.find_all("a")
        c = []
        for href in hrefs:
            b = href.get('href')
            c.append(b)
        if c[0].startswith("http"):
            links_results.append(c[0])
        descriptions = div_g.find_all("span", {"class": "st"})
        for description in descriptions:
            e = description.text
            descriptions_list.append(e)
    print(descriptions_list)
    print(h3_results)
    print(links_results)


print("DuckDuckGo")

with url.urlopen(request_duck_duck_go) as response2:
    html2 = response2.read().decode("utf8")
    soup2 = Bs4(html2, 'html.parser')
    test_a_2 = soup2.find_all('a')
    for links in test_a_2:
        # print(links.get("href"))
        pass

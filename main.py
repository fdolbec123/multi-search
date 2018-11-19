import urllib.request as url

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.1'
user_agent_end = '02 Safari/537.36'
user_agent = user_agent + user_agent_end

headers = {"User-Agent": user_agent}
request = url.Request("https://www.google.ca/search?q=test", None, headers)
with url.urlopen(request) as response:
    html = response.read()
    print(html)

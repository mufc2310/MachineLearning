import requests

html_page = requests.get("https://www.imdb.com/chart/tvmeter?ref_=nv_tvv_mptv")

print(html_page.text)
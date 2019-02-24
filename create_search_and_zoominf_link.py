import requests
from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup

try:
    def search(company_lists):
        try:
            for company in company_lists:
                site = 'zoominfo%20'
                company = company.lower()
                url = "https://google.com/search?q=" + site + company+"%20"
                header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) '
                                        'AppleWebKit / 537.36(KHTML, like Gecko) Chrome / '
                                        '71.0.3578.98 Safari / 537.36'}
                r = requests.get(url, headers=header, timeout=5)
                r1 = r.text
                soup = BeautifulSoup(r1, 'html.parser')
                for i in soup.findAll('a'):
                    link = i.get('href')
                    if link.startswith('/url?'):
                        link = parse_qs(urlparse(link).query)['q']
                        result = link[0].startswith('https://www.zoominfo.com/c/' + company)
                        if result is True:
                            url_data.append(link[0])
                            break
            print(url_data)
        except Exception as e1:
            print(str(e1))

    company_list = [input('Company Name: ')]
    url_data = []
    (search(company_list))
except Exception as e:
    print(str(e))














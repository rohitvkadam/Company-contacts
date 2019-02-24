import requests
import create_search_and_zoominf_link
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import sqlite3

try:
    def data(web_link):
        try:
            conn = sqlite3.connect('websiteinfo.db')
            c = conn.cursor()
            # c.execute("CREATE TABLE company_contact (company text,contact integer)")
            for zoom_link in web_link:
                url1 = str(zoom_link)
                ua = UserAgent()
                header = {'User-Agent': str(ua.chrome)}
                k = requests.get(url1, headers=header, timeout=5)
                k1 = k.text
                soup = BeautifulSoup(k1, 'html.parser')
                for co_title in soup.findAll(class_="fn"):
                    co_title.get('span')
                    print(co_title.text)
                    if soup.findAll(class_='content-box_row phone'):
                        for phone_no in soup.findAll('div', class_='content-box_row phone'):
                            print('phone no: ', phone_no.span.text)
                            c.execute("INSERT INTO company_contact(company, contact) VALUES (?,?)",
                                      (str(co_title.text), phone_no.span.text))
                    else:
                        pn = 0
                        print("Company don't have contact Number. ")
                        c.execute("INSERT INTO company_contact(company, contact) VALUES (?,?)",
                                  (str(co_title.text), int(pn)))
                    print('-'*100)
                    c.execute("SELECT * FROM company_contact")
                    print(" Table in sql3lite Database : company_contact ")
                    print(c.fetchall())
            conn.commit()
            conn.close()
        except Exception as e1:
            print(str(e1))
    data(create_search_and_zoominf_link.url_data)
except Exception as e:
    print(str(e))


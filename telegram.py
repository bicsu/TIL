import requests
from bs4 import BeautifulSoup as bs

token = "699313570:AAGqOCKZnk5k1BCazhXIIiYL6J7KV9UV21M"
method_name = "getUpdates"
url = "https://api.telegram.org/bot{0}/{1}".format(token, method_name)
update = requests.get(url).json()
#print(update["result"][0]["message"]['from']['id'])

url_kospi = "https://finance.naver.com/sise/"
html_kos = requests.get(url_kospi).text
soup_kos = bs(html_kos, 'html.parser')
select = soup_kos.select_one('#KOSPI_now')

print(select.text)




user_id = update["result"][0]["message"]['from']['id']
method_name = "sendmessage"
msg = select.text
msg_url = "https://api.telegram.org/bot{0}/{1}?chat_id={2}&text={3}".format(token, method_name, user_id, msg)
# print(msg_url)
print(requests.get(msg_url))



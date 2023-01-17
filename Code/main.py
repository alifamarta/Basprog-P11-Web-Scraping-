import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd

URL = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=laptop&_sacat=0"
page = req.get(URL)
soup = bs(page.content, 'html.parser')

produk = soup.find_all('li', attrs={'class': 's-item'})

nama_produk = []
harga_produk = []
for item in produk:
  nama = item.find('div', attrs={'class': 's-item__title'}).text
  harga = item.find('span', attrs={'class': 's-item__price'}).text
  nama_produk.append(nama)
  harga_produk.append(harga)

df = pd.DataFrame({'Barang': nama_produk, 'Harga': harga_produk})

print(df)
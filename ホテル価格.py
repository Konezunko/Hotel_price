#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install requests')


# In[2]:


import requests
from bs4 import BeautifulSoup


# In[4]:


url = 'https://travel.rakuten.co.jp/HOTEL/74543/74543.html?l-id=hotelList_7_74543'
res = requests.get(url)

import requests
from bs4 import BeautifulSoup
url = 'https://travel.rakuten.co.jp/HOTEL/74543/74543.html?l-id=hotelList_7_74543'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
elems = soup.select('//*[@id="4985055-s01"]/ul/li[3]/dl/dd[1]/div/span/strong')



# In[9]:


pip install lxml


# In[5]:


res.text


# In[13]:



import requests
from lxml import html

url = 'https://travel.rakuten.co.jp/HOTEL/74543/74543.html?l-id=hotelList_7_74543'
res = requests.get(url)

# HTMLをlxmlのhtmlオブジェクトに変換
tree = html.fromstring(res.content)

# XPathを用いて要素を取得
elems = tree.xpath('//*[@id="4985055-s01"]/ul/li[3]/dl/dd[1]/div/span/strong')


# elemsは要素のリストになるので、内容を表示したい場合は以下のように行います。
print(elems.text)


# In[61]:


kakaku = soup.find_all('span', attrs={'class':'ndPrice'})
a = kakaku[0].text.strip('合計')
print(a.replace('円(税込)',''))


# In[26]:


https://hotel.travel.rakuten.co.jp/hotelinfo/plan/?f_no=149334&f_flg=PLAN&f_teikei=&f_hizuke=&f_hak=&f_dai=japan&f_chu=hokkaido&f_shou=noboribetsu&f_sai=&f_tel=&f_target_flg=&f_tscm_flg=&f_p_no=&f_custom_code=&f_search_type=&f_camp_id=&f_static=1&f_rm_equip=


# In[26]:


import requests
from lxml import html

# ターゲットとなるURLを指定します。
hotel_code = {
    'dormy': 149334,
    'route': 149334,
    'rouground': 168374,
    'newbajet': 7506,
    'prince': 5499,
    'apa': 74543
}
keys_list = list(hotel_code.keys())

for  i in range(len(hotel_code)):
    
    url = 'https://hotel.travel.rakuten.co.jp/hotelinfo/plan/{}?f_flg=PLAN&f_teikei=&f_hizuke=&f_hak=&f_dai=japan&f_chu=hokkaido&f_shou=noboribetsu&f_sai=&f_tel=&f_target_flg=&f_tscm_flg=&f_p_no=&f_custom_code=&f_search_type=&f_camp_id=&f_static=1&f_rm_equip=&f_hi1=13&f_tuki1=9&f_nen1=2023&f_hi2=14&f_tuki2=9&f_nen2=2023&f_heya_su=1&f_otona_su=1&f_kin2=0&f_kin=&f_s1=0&f_s2=0&f_y1=0&f_y2=0&f_y3=0&f_y4=0'
    url = url.replace('{}', hotel_code[keys_list[i]])  # 例：'f_otona_su=1'を'f_otona_su=2'に置き換える

    # ウェブページを取得します。
    res = requests.get(url)
    res.raise_for_status()  # エラーが発生した場合に例外をスローします。

    # HTMLをlxmlのhtmlオブジェクトに変換します。
    tree = html.fromstring(res.content)

    # XPathやCSSセレクタを使用して価格などの要素を取得します。
    # 以下はXPathの例です。適切なXPathを使用する必要があります。
    prices = tree.xpath('//*[@id="4985055-s01"]/ul/li[3]/dl/dd[1]/div/span/strong')

    # 取得した価格を表示します。
    if prices:
        for price in prices:
            price_value = str(price.text)
            price=(price_value)

            print(price_value)
    else:
        print("-")


# In[18]:


print(type(price))


# In[24]:


import pandas as pd


# In[48]:


import pandas as pd
import requests
from lxml import html

# ターゲットとなるURLを指定します。
hotel_code = {
    'dormy': 149334,
    'route': 78111,
    'rouground': 168374,
    'newbajet': 7506,
    'prince': 5499,
    'apa': 74543
}

xpaths = [
    '//*[@id="3587642-sdn"]/ul/li[3]/dl/dd[1]/div/span/strong',
    '//*[@id="3577746-ss"]/ul/li[3]/dl/dd[1]/div/span/strong',
    '//*[@id="4298646-ns"]/ul/li[3]/dl/dd[1]/div/span/strong',
    '//*[@id="1495742-sr-vod"]/ul/li[3]/dl/dd[1]/div/span/strong',
    '//*[@id="5676414-sgl"]/ul/li[3]/dl/dd[1]/div/span/strong',
    '//*[@id="4985055-s01"]/ul/li[3]/dl/dd[1]/div/span/strong'
]


base_url = 'https://hotel.travel.rakuten.co.jp/hotelinfo/plan/{}?f_flg=PLAN&f_teikei=&f_hizuke=&f_hak=&f_dai=japan&f_chu=hokkaido&f_shou=noboribetsu&f_sai=&f_tel=&f_target_flg=&f_tscm_flg=&f_p_no=&f_custom_code=&f_search_type=&f_camp_id=&f_static=1&f_rm_equip=&f_hi1=13&f_tuki1=9&f_nen1=2023&f_hi2=14&f_tuki2=9&f_nen2=2023&f_heya_su=1&f_otona_su=1&f_kin2=0&f_kin=&f_s1=0&f_s2=0&f_y1=0&f_y2=0&f_y3=0&f_y4=0'

hotel_names = []
hotel_prices = []

for hotel_name, code in hotel_code.items():
    url = base_url.format(code)
    try:
        # ウェブページを取得します。
        res = requests.get(url)
        res.raise_for_status()  # エラーが発生した場合に例外をスローします。

        # HTMLをlxmlのhtmlオブジェクトに変換します。
        tree = html.fromstring(res.content)
        # XPathやCSSセレクタを使用して価格などの要素を取得します。
        # 以下はXPathの例です。適切なXPathを使用する必要があります。
        #prices = tree.xpath('//*[@id="3587642-sdn"]/ul/li[3]/dl/dd[1]/div/span/strong')
        
        
        for xpath in xpaths:
            prices = tree.xpath(xpath)

            # もし価格が取得できたらループを終了する
            if prices:
                break

        
        
        
        #ホテル名と価格をリストに追加
        hotel_names.append(hotel_name)
        
        #ホテル名を表示します
        print(hotel_name)
        # 取得した価格を表示します。
        if prices:
            for price in prices:
                hotel_prices.append(prices[0].text)
                print(price.text)
        else:
            hotel_prices.append("-")
            print("-")
            
    except requests.HTTPError:
        print(f"Failed to fetch data for hotel: {hotel_name}")

df = pd.DataFrame({
    'Hotel Name':hotel_name,
    'Price':hotel_prices
})

df.to_excel('https://d.docs.live.net/a8e563a22fa45f4d/%E3%83%89%E3%82%AD%E3%83%A5%E3%83%A1%E3%83%B3%E3%83%88/%E3%83%9B%E3%83%86%E3%83%AB%E4%BE%A1%E6%A0%BC%E6%9C%80%E7%B5%82%E7%89%88.xlsx',index=False,engine='openpyxl')

        
        
        
        
        


# In[45]:


(/*[@id="3587642-sdn"]/ul/li[3]/dl/dd[1]/div/span/strong)
(/*[@id="3577746-ss"]/ul/li[3]/dl/dd[1]/div/span/strong)
(/*[@id="4298646-ns"]/ul/li[3]/dl/dd[1]/div/span/strong)
(/*[@id="1495742-sr-vod"]/ul/li[3]/dl/dd[1]/div/span/strong)
(/*[@id="5676414-sgl"]/ul/li[3]/dl/dd[1]/div/span/strong)
(/*[@id="4985055-s01"]/ul/li[3]/dl/dd[1]/div/span/strong)


# In[ ]:





# In[ ]:





import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date as DT
from django.core.management.base import BaseCommand
from myapp.models import (Elespectador)



class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):

        urls = ["https://www.elcolombiano.com/tecnologia",
        "https://www.elcolombiano.com/negocios",
        "https://www.elcolombiano.com/deportes/futbol",
        "https://www.elcolombiano.com/entretenimiento"]
        categories = ['tecnologia','economia', 'deportes', 'entretenimiento']
        
        for i in range(4):

            r = requests.get(urls[i])

            category = categories[i]

            # with open('response.html', 'w', encoding='utf-8') as f:
            #     f.write(r.text)

            soup = BeautifulSoup(r.text, 'html.parser')

            posts = soup.find_all('article')

            dataList = []
            for post in posts:
                try:
                    try:
                        publishDate = post.find('div',class_='categoria-noticia').text.split('|')[-1].strip().split('/')
                        publishDate = DT(int(publishDate[-1]), int(publishDate[-2]), int(publishDate[-3]))
                    except:
                        publishDate = None
                    link = post.find('h3')
                    headline = link.text.strip()
                    url ="https://www.elcolombiano.com"+link.find("a")['href'] 
                    record = {'headline':headline, 'category':category ,'published_date':publishDate, 'link':url}
                    dataList.append(record)
                except:
                    pass
                
            try:
                df = pd.DataFrame(dataList)
                df_new = df.sort_values('published_date', ascending=False)
                final_value = df_new.loc[0].to_dict()
                
            except:
                final_value = dataList[0]

            Elespectador.objects.create(
                title=final_value['headline'],
                category=final_value['category'],
                date=final_value['published_date'],
                source="www.elcolombiano.com",
                url=final_value['link']
                )
            print(final_value)



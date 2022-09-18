from django.core.management.base import BaseCommand
from myapp.models import (Blog, Elespectador)
from bs4 import BeautifulSoup
import regex as re
import requests
import json
from datetime import datetime as DT
import pandas as pd



HEADERS = {
    "referrer" : "https://www.google.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}



def larepublic():
    r= requests.get("https://www.larepublica.co/economia")

    print(r.status_code)
    with open("response.html", "w", encoding="utf-8") as f:
        f.write(r.text)
    soup = BeautifulSoup(r.text, "html.parser")

    elems = soup.find_all('div', class_="col-7 pl-3 pr-3")
    print(len(elems))


    for elem in elems:
        title = elem.find('text-fill')
        if title:
            link = title.find("a")['href']
            print(link)
            print(title.text.strip())
        
    


def eltimpo():
    links = soup.find_all("a")
    for a in links:
        try:
            link = a['href']
            parts = link.split("/")
            # print(parts)
            if parts[1]=="politica":
                link = "https://www.eltiempo.com"+link
                print(link)
        except:
            pass






# for elem in elems:
#     published = elem.find('span', class_="fecha published-at")
#     published_date = elem.find('span', class_="published-at")
#     try:
#         print(published.text)
#     except:
#         pass
#     titleContainer = elem.find("h3", class_='title-container box-title')
#     try:
#         title = titleContainer.text
#     except:
#         pass
#     articleUrl = elem.find('a', class_="title page-link")
#     if title:
        
#         print(articleUrl.text)
#         print(articleUrl['href'])
        
            
# elems = soup.find_all("div", class_="info_contenido")    

# data = []
# for elem in elems:
#     date_published = elem.find("meta", attrs={"itemprop":"datePublished"})
#     if date_published:
#         date_published = date_published['content']
#         linkPost = elem.find("a", class_="multimediatag page-link")
#         if linkPost:
#             post = {"date_published":date_published, "linkPost":"https://www.eltiempo.com"+linkPost['href']}
#             data.append(post)
#             title = elem.find("h3",class_='elecciones_titulo_dos').text.strip()





import requests







class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        
        cookies = {
            '_vwo_uuid_v2': 'DD5A8D38BC281FAEA4771CF42AA23CA62|4982a806844c6ec1ccd53ef45c5a4f82',
            '_vwo_uuid': 'DD5A8D38BC281FAEA4771CF42AA23CA62',
            '_pprv': '%7B%22consent%22%3A%7B%220%22%3A%7B%22mode%22%3A%22opt-in%22%7D%2C%221%22%3A%7B%22mode%22%3A%22opt-in%22%7D%2C%222%22%3A%7B%22mode%22%3A%22opt-in%22%7D%2C%223%22%3A%7B%22mode%22%3A%22opt-in%22%7D%2C%224%22%3A%7B%22mode%22%3A%22opt-in%22%7D%2C%225%22%3A%7B%22mode%22%3A%22opt-in%22%7D%2C%226%22%3A%7B%22mode%22%3A%22opt-in%22%7D%2C%227%22%3A%7B%22mode%22%3A%22opt-in%22%7D%7D%7D',
            '_pcid': '%7B%22browserId%22%3A%22l7lrbcgtnhk0x7sp%22%7D',
            '_tfpvi': 'YWM1OGMyNTktN2VkMi00MmJkLWFiODctN2FiODc3YjY5N2U2Iy03LTI%3D',
            '_gcl_au': '1.1.198304581.1662200594',
            '__pat': '-18000000',
            'cX_P': 'l7lrbcgtnhk0x7sp',
            '_fbp': 'fb.1.1662200595941.1733530086',
            'trc_cookie_storage': 'taboola%2520global%253Auser-id%3D044bcdff-9c4f-443c-b6d3-79f50e82478b-tucta0cb095',
            'cX_G': 'cx%3A3rx5b745cfw0l3lnavul3be3ic%3A1m3j7d93mdngn',
            '_cc_id': '116fcd33a5a21a0cdbe6f683ade6b580',
            'panoramaId_expiry': '1662806542894',
            'panoramaId': 'a146032bcd97b449be5dfd540d3a16d5393804e57e2e4df2dd4267dc232814c1',
            'xbc': '%7Bkpex%7DFcHKMyMFbv85HiEX3EZDow9o-iNEYoXJhz7wL9b0bvfDIFRfTzlAwb3CIDoG1vFLb9SsFbg5ae_7frkUjDnA1i3GRwqocsAYNPNtC3-xEA6oEVpR3sdtrDxZmfdy7iAywIr9Eg0epkT2O5C0lhU-f35TcvCcoNfujkpWf_rZK9I5G6GhsTtyYRqR6dMKn7qa478oQFmdTjzCEmF_bzDS5KmNyxA9c6IIKfQpCaNhCt_6gLGRNLVsRrce5pG0ESBwIJtn6LEIsLORt-kaHQXKt4YjGfU-c0cm5mxgWlONBJww7Sa-1Sq3e12HscPFt5skcVugNk7fkbUm8KpNwDtNmk-Rj9C2AN0CYUYNN77XEjAuVMVrhJBsw2qFrXr0ervPnHlswHlClZ_SfijlPd51iRSM1SqeJcm1sZDm8uHihXNc6seuB6e2AtUsyTuMxaDdLWSg0Ofh9l2W9isFnmAUoudTCPR2AwPQx_lm1nD476O26eoH5VEZs6WLh50mtq74wzbaq9RR9TSnOOc2CFMuPjlV0bdDQn1hdWNlU7yDo1_q1nlH45bdnHrEaRYRYKtaSsh4nBNs8_J6ODbmsUcSLhzb7tC-DanLAcjCOdupIq4',
            '_pbjs_userid_consent_data': '3524755945110770',
            '_vis_opt_s': '2%7C',
            '_vis_opt_test_cookie': '1',
            'cX_S': 'l7viz08kc6aucxg4',
            '_pc_suscriptor': 'false',
            '_gid': 'GA1.2.603441335.1662791241',
            '__gads': 'ID=a87b0eb265490fa7-22a2759321d50031:T=1662200596:S=ALNI_MY4XwcsYB5grhHU54EHTGZy9MJWdA',
            '__gpi': 'UID=00000b1ba0e0056f:T=1662200596:RT=1662791241:S=ALNI_MYAiWVS_wts2rWp6MAz3-TRrjZ3wQ',
            '_vfa': 'www%2Eelespectador%2Ecom.00000000-0000-4000-8000-a4de5f363b96.a80d5911-a975-4090-921c-d0e401901220.1662200599.1662200599.1662791244.2',
            '__tbc': '%7Bkpex%7Dg1VA4RlLpk6JO7P-UDSzIY5ZU4hk-RWUhoCEs_ZGmC47Ndfuo1FftDKXrachWmdk',
            '_ga': 'GA1.2.1864635455.1662200596',
            '___iat_vis': '31AAAD3A7EAD4FC3.5e628daa293de598f6c49aa3ac3aaaa0.1662791500118.cf8eae0dcf4f93b422a244422d69ff30.OBUBJEIBEB.11111111.1.0',
            '_vwo_ds': '3%3At_1%2Ca_1%3A2%241662200587%3A88.50403468%3A156_2_1_590642_1%2C154_2_1_590642_1%2C150_2_1_590642_1%2C148_2_1_590642_1%2C149_2_1_590642_1%3A25_1%2C24_1%2C23_1%2C2_1%2C15_1%3A183_1%2C179_1%2C27_1%2C12_1%2C3_1%2C2_1%3A6',
            'AKA_A2': 'A',
            '_ga_FPLL0E7S46': 'GS1.1.1662797647.4.0.1662797647.0.0.0',
            'RT': '"z=1&dm=elespectador.com&si=re1naj62j7p&ss=l7viyrtx&sl=0&tt=0"',
            '_pctx': '%7Bu%7DN4IgDghg5gpgagSxgdwJIBMQC4QBsDsAbgLYDO6ADANYBeAnAEywBOpA9iADQgCupMrbADseuXNz4CAygBcIMvthAQhbIVxCkEMmBiUBGfQGYArPrr4AHBUv5DJgGz4HlkyAC%2BQA',
            '__pvi': '%7B%22id%22%3A%22v-2022-09-10-01-14-08-676-iW440wuAK1bBMTrd-939a5592569604197859a3aaf84f05dc%22%2C%22domain%22%3A%22.elespectador.com%22%2C%22time%22%3A1662797648677%7D',
            '_vwo_sn': '590642%3A1',
        }

        headers = {
            'authority': 'www.elespectador.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'referer': 'https://www.elespectador.com/economia/',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        }


        lis = [{
                'query': '{"section":"/opinion/editorial","size":20,"sourceInclude":"_id,additional_properties,canonical_url,type,subtype,description.basic,headlines.basic,subheadlines.basic,taxonomy.primary_section._id,taxonomy.primary_section.name,taxonomy.primary_section.path,taxonomy.sections.name,taxonomy.tags.text,taxonomy.tags.slug,first_publish_date,display_date,last_updated_date,promo_items.basic,promo_items.comercial,promo_items.comercial_movil,promo_items.jw_player,label,credits.by._id,credits.by.name,credits.by.additional_properties.original,credits.by.image.url,commentCount"}',
                'd': '589',
                '_website': 'el-espectador',
                },	
               {
                'query': '{"section": "/opinion/columnistas" ,"size":20,"sourceInclude":"_id,additional_properties,canonical_url,type,subtype,description.basic,headlines.basic,subheadlines.basic,taxonomy.primary_section._id,taxonomy.primary_section.name,taxonomy.primary_section.path,taxonomy.sections.name,taxonomy.tags.text,taxonomy.tags.slug,first_publish_date,display_date,last_updated_date,promo_items.basic,promo_items.comercial,promo_items.comercial_movil,promo_items.jw_player,label,credits.by._id,credits.by.name,credits.by.additional_properties.original,credits.by.image.url,commentCount"}',
                'd': '589',
                '_website': 'el-espectador',
               },
               {
                'query': '{"section": "/economia" ,"size":20,"sourceInclude":"_id,additional_properties,canonical_url,type,subtype,description.basic,headlines.basic,subheadlines.basic,taxonomy.primary_section._id,taxonomy.primary_section.name,taxonomy.primary_section.path,taxonomy.sections.name,taxonomy.tags.text,taxonomy.tags.slug,first_publish_date,display_date,last_updated_date,promo_items.basic,promo_items.comercial,promo_items.comercial_movil,promo_items.jw_player,label,credits.by._id,credits.by.name,credits.by.additional_properties.original,credits.by.image.url,commentCount"}',
                'd': '589',
                '_website': 'el-espectador',
               },
               
               {
                'query': '{"section": "/politica" ,"size":20,"sourceInclude":"_id,additional_properties,canonical_url,type,subtype,description.basic,headlines.basic,subheadlines.basic,taxonomy.primary_section._id,taxonomy.primary_section.name,taxonomy.primary_section.path,taxonomy.sections.name,taxonomy.tags.text,taxonomy.tags.slug,first_publish_date,display_date,last_updated_date,promo_items.basic,promo_items.comercial,promo_items.comercial_movil,promo_items.jw_player,label,credits.by._id,credits.by.name,credits.by.additional_properties.original,credits.by.image.url,commentCount"}',
                'd': '589',
                '_website': 'el-espectador',
               },
               {
                'query': '{"section": "/tecnologia" ,"size":20,"sourceInclude":"_id,additional_properties,canonical_url,type,subtype,description.basic,headlines.basic,subheadlines.basic,taxonomy.primary_section._id,taxonomy.primary_section.name,taxonomy.primary_section.path,taxonomy.sections.name,taxonomy.tags.text,taxonomy.tags.slug,first_publish_date,display_date,last_updated_date,promo_items.basic,promo_items.comercial,promo_items.comercial_movil,promo_items.jw_player,label,credits.by._id,credits.by.name,credits.by.additional_properties.original,credits.by.image.url,commentCount"}',
                'd': '589',
                '_website': 'el-espectador',
               },
               {
                'query': '{"section": "/judicial" ,"size":20,"sourceInclude":"_id,additional_properties,canonical_url,type,subtype,description.basic,headlines.basic,subheadlines.basic,taxonomy.primary_section._id,taxonomy.primary_section.name,taxonomy.primary_section.path,taxonomy.sections.name,taxonomy.tags.text,taxonomy.tags.slug,first_publish_date,display_date,last_updated_date,promo_items.basic,promo_items.comercial,promo_items.comercial_movil,promo_items.jw_player,label,credits.by._id,credits.by.name,credits.by.additional_properties.original,credits.by.image.url,commentCount"}',
                'd': '589',
                '_website': 'el-espectador',
               },
               {
                'query': '{"section": "/ambiente" ,"size":20,"sourceInclude":"_id,additional_properties,canonical_url,type,subtype,description.basic,headlines.basic,subheadlines.basic,taxonomy.primary_section._id,taxonomy.primary_section.name,taxonomy.primary_section.path,taxonomy.sections.name,taxonomy.tags.text,taxonomy.tags.slug,first_publish_date,display_date,last_updated_date,promo_items.basic,promo_items.comercial,promo_items.comercial_movil,promo_items.jw_player,label,credits.by._id,credits.by.name,credits.by.additional_properties.original,credits.by.image.url,commentCount"}',
                'd': '589',
                '_website': 'el-espectador',
               },
               {
                'query': '{"section": "/salud" ,"size":20,"sourceInclude":"_id,additional_properties,canonical_url,type,subtype,description.basic,headlines.basic,subheadlines.basic,taxonomy.primary_section._id,taxonomy.primary_section.name,taxonomy.primary_section.path,taxonomy.sections.name,taxonomy.tags.text,taxonomy.tags.slug,first_publish_date,display_date,last_updated_date,promo_items.basic,promo_items.comercial,promo_items.comercial_movil,promo_items.jw_player,label,credits.by._id,credits.by.name,credits.by.additional_properties.original,credits.by.image.url,commentCount"}',
                'd': '589',
                '_website': 'el-espectador',
               },
               {
                'query': '{"section": "/entretenimiento" ,"size":20,"sourceInclude":"_id,additional_properties,canonical_url,type,subtype,description.basic,headlines.basic,subheadlines.basic,taxonomy.primary_section._id,taxonomy.primary_section.name,taxonomy.primary_section.path,taxonomy.sections.name,taxonomy.tags.text,taxonomy.tags.slug,first_publish_date,display_date,last_updated_date,promo_items.basic,promo_items.comercial,promo_items.comercial_movil,promo_items.jw_player,label,credits.by._id,credits.by.name,credits.by.additional_properties.original,credits.by.image.url,commentCount"}',
                'd': '589',
                '_website': 'el-espectador',
               },
               {
                'query': '{"section": "/educacion" ,"size":20,"sourceInclude":"_id,additional_properties,canonical_url,type,subtype,description.basic,headlines.basic,subheadlines.basic,taxonomy.primary_section._id,taxonomy.primary_section.name,taxonomy.primary_section.path,taxonomy.sections.name,taxonomy.tags.text,taxonomy.tags.slug,first_publish_date,display_date,last_updated_date,promo_items.basic,promo_items.comercial,promo_items.comercial_movil,promo_items.jw_player,label,credits.by._id,credits.by.name,credits.by.additional_properties.original,credits.by.image.url,commentCount"}',
                'd': '589',
                '_website': 'el-espectador',
               },
               {
                'query': '{"section": "/deportes" ,"size":20,"sourceInclude":"_id,additional_properties,canonical_url,type,subtype,description.basic,headlines.basic,subheadlines.basic,taxonomy.primary_section._id,taxonomy.primary_section.name,taxonomy.primary_section.path,taxonomy.sections.name,taxonomy.tags.text,taxonomy.tags.slug,first_publish_date,display_date,last_updated_date,promo_items.basic,promo_items.comercial,promo_items.comercial_movil,promo_items.jw_player,label,credits.by._id,credits.by.name,credits.by.additional_properties.original,credits.by.image.url,commentCount"}',
                'd': '589',
                '_website': 'el-espectador',
               },
               ]
        for params in lis:   
            query= params['query']
            category = json.loads(query)
            category = category['section'].split("/")[1]
            response = requests.get('https://www.elespectador.com/pf/api/v3/content/fetch/general', params=params, cookies=cookies, headers=headers)

            data_dic = json.loads(response.text)

            data_dic  = data_dic['content_elements']

            dataList = []
            for data in data_dic:
                try:
                    headline = data['description']['basic']
                    url = 'https://www.elespectador.com' + data['canonical_url']
                    publishDate = data['first_publish_date'].split('T')[0].split('-')
                    publishDate = DT(int(publishDate[0]), int(publishDate[1]), int(publishDate[2]))
                    category = category
                    record = {'headline':headline, 'published_date':publishDate, 'link':url}
                    dataList.append(record)
                except:
                    pass


            df = pd.DataFrame(dataList)
            df_new = df.sort_values('published_date', ascending=False)
            final_value = df_new.loc[0].to_dict()

            record = Elespectador.objects.create(
            	title=final_value['headline'], 
            	category=category,
            	date=final_value['published_date'],
            	source="www.elespectador.com",
            	url=final_value['link']
            	)

            



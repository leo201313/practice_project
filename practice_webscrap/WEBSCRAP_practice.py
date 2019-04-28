import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd


def movie_parsing(url):
    # url='https://maoyan.com/films/837'
    response =requests.get(url)
    content = response.content
    parser = BeautifulSoup(content,'html.parser')
    movie_brief_container=parser.select('div .movie-brief-container')[0]
    movie_name=movie_brief_container.select('.name')[0].text #movie name

    movie_brief_container_ul=movie_brief_container.select('ul')[0]
    movie_brief_container_ul_li=movie_brief_container_ul.select('li')
    movie_kind=movie_brief_container_ul_li[0].text #movie kind
    movie_area_length=movie_brief_container_ul_li[1].text #movie area and length
    movie_first_date=movie_brief_container_ul_li[2].text #movie date

    movie_index_content_score = parser.select('.movie-index-content.score.normal-score')[0]
    movie_score=movie_index_content_score.select('.star-wrapper')[0].select('.star-on')[0]['style']
    #movie score
    # for further learning, maybe I can try to trans the stonefront.
    return([url,movie_name,movie_kind,movie_area_length,movie_first_date,movie_score])

def page_parsing(url):
    response=requests.get(url)
    parser=BeautifulSoup(response.content,'html.parser')
    board_wrapper = parser.select('body .board-wrapper')[0]
    for movie in range(10):
        movie_id = board_wrapper.select('dd')[movie].select('a')[0]['href']
        web_url.append('https://maoyan.com{}'.format(movie_id))



web_url=[]
data_list=[]
for pages in range(10):
    page_url='https://maoyan.com/board/4?offset={}'.format(pages*10)
    page_parsing(page_url)



for url in web_url:
    data_list.append(movie_parsing(url))


movie_data=pd.DataFrame(data_list,columns=['url','movie_name','movie_kind','movie_area_length','movie_first_date','movie_score'])
# print(movie_data)

movie_data.to_csv('maoyantop100.csv')



# url='https://maoyan.com/board/4?offset=00'
# response=requests.get(url)
# parser=BeautifulSoup(response.content,'html.parser')
# board_wrapper = parser.select('body .board-wrapper')[0]
# for movie in range(10):
#     movie_id = board_wrapper.select('dd')[movie].select('a')[0]['href']
#     web_url.append('https://maoyan.com{}'.format(movie_id))
#     print(web_url)
#













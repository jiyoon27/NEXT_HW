import requests
from bs4 import BeautifulSoup
import csv

file = open('movieutf8.csv', mode='w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)
writer.writerow(["title", "rating", "image", "director", "actor", "date"])

MOVIE_URL = f'https://movie.naver.com/movie/running/current.nhn'
movie_html = requests.get(MOVIE_URL)
movie_soup = BeautifulSoup(movie_html.text,"html.parser")

movie_list_box = movie_soup.find('ul', {'class':'lst_detail_t1'})
movie_items = movie_list_box.find_all('li')

final_result = []
for movie_item in movie_items:
    title = movie_item.find("dt", {"class":"tit"}).find("a").text
    rating = movie_item.find("span", {"class":"num"}).text
    image_box = movie_item.find("div", {"class":"thumb"})
    image = image_box.find("a").find("img")['src']
    movie_info = movie_item.find_all("span", {"class":"link_txt"})
    director = movie_info[1].text
    actor = movie_info[-1].text.replace("\r", "").replace("\n", "").replace("\t", "")
    date_info = movie_item.find("dl", {"class":"info_txt1"})
    date = date_info.find_all("dd")[0].text.split("|")[-1].replace("\r", "").replace("\n", "").replace("\t", "")

    result = {
        'title' : title,
        'rating' : rating,
        'image' : image,
        'director' : director,
        'actor' : actor,
        'date' : date
    }
    final_result.append(result)

for result in final_result:
    row = []
    row.append(result['title'])
    row.append(result['rating'])
    row.append(result['image'])
    row.append(result['director'])
    row.append(result['actor'])
    row.append(result['date'])
    writer.writerow(row)

print (final_result)


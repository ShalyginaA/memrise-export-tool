from bs4 import BeautifulSoup
import requests

f = open('course_id.txt', 'r')
course_id = str(f.read())
f.close()
r = requests.get('https://www.memrise.com/course/' + course_id)
soup = BeautifulSoup(r.content, 'html.parser')

# extract url for each level
level_urls = []
for s in soup.find_all(attrs = {'class' : 'level clearfix'}): 
    level_urls.append(s['href'])

all_words = u''
for level_url in level_urls:
    request = requests.get('https://www.memrise.com' + level_url)
    soup = BeautifulSoup(request.content, 'html.parser')
    for s in soup.find_all('div', attrs = {'class' : 'col_a col text'}):
        word = s.get_text()
        translation = s.next_sibling()[0].get_text()
        all_words = all_words + word + '\t' + translation + '\n'        

f = open(course_id + '.txt', 'w')
f.write(all_words)
f.close()


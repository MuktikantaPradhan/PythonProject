from bs4 import BeautifulSoup
import requests


def main():
    r = requests.get('https://www.youtube.com/')
    soup = BeautifulSoup(r.content, 'html')

    title = soup.title.string
    print ('TITLE IS :', title)

    meta = soup.find_all('meta')

    for tag in meta:
        if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in ['description', 'keywords']:
            print ('NAME    :',tag.attrs['name'].lower())
            print ('CONTENT :',tag.attrs['content'])
            contentKey=tag.attrs['content']            
    

if __name__ == '__main__':
    main()
#! python3
import bs4, requests, os

# starting URL
url = 'http://xkcd.com'
# store comics image in ./xkcd
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
# TODO: Download the page.
    print('Downloading Page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text) 
# TODO: Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        
# TODO: Download the image.
        print('Downloading Image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()  

# TODO: Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

# TODO: Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
print('Done. ')

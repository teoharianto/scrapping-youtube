import bs4, requests, os, csv, io
page = requests.get('https://www.youtube.com/', timeout=(5, None))
soup = bs4.BeautifulSoup(page.text, 'html.parser')

i = 0
while os.path.exists('Downloaded File%s.txt' % i):
        i+=1
filename = "Scraping-youtube%s.csv" % i
downloadedFile = csv.writer(io.open(filename,'w', encoding="utf-8"))

if page.status_code==200:
    print("=" * 30 + "Title" +"=" * 30)
    title = soup.select('h3 a')
    single = soup.find_all('span', class_="accessible-description")
    double = soup.find_all('a', class_="yt-uix-sessionlink spf-link ")
    triple = soup.select("ul[class='yt-lockup-meta-info']")
    titleList=[]
    
    def titles():
        for a in title:
            linkVideo = "Link = https://www.youtube.com"+a['href']
            titlee = a['title']
            course=[titlee,linkVideo]
            titleList.append(course)

    def singles():
        for b in single:    
            durasi = b.get_text()
            course=[durasi]
            titleList.append(course)
    def doubles():
        for c in double:
            upload = c.get_text()
            link = "https://www.youtube.com"+c['href']

            course=[upload, link]
            titleList.append(course)
    def triples():
        for ul in triple:
            items2 = ul.find('li').text
            for li in ul.find_all('li'):
                items1 = li.text 
            course=[items2, items1]
            titleList.append(course)
    titles()
    singles()
    doubles()
    triples()
    print()
    for row in titleList:
        downloadedFile.writerow(row)
    
    

    
        

            
            
            
            
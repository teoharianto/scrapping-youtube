import bs4, requests, csv, io
# get webpage data
page = requests.get('https://www.youtube.com/', timeout=(5, None))
soup = bs4.BeautifulSoup(page.text, 'html.parser')

if page.status_code == requests.codes.ok:
    # Input File name and open a file
    namaFile = input('Ketik Nama File Yang Diinginkan :\n>> ')
    openFile = io.open(f'{namaFile}.csv','w', encoding="utf-8", newline='')
    downloadedFile = csv.writer(openFile)
    downloadedFile.writerow(['Judul', 'Link Video', 'Durasi', 'Pengupload', 'Link Pengupload', 'Jumlah Penonton', 'Waktu Upload'])

    print("=" * 30 + "Finished" +"=" * 30)
    # Looking for element to scrap
    title = soup.select('h3 a')
    single = soup.find_all('span', class_="accessible-description")
    double = soup.find_all('a', class_="yt-uix-sessionlink spf-link ")
    triple = soup.select("ul[class='yt-lockup-meta-info']")
    # List for all
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

    for row in titleList:
        downloadedFile.writerow(row)
 

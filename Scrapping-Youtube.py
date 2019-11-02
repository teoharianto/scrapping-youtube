import bs4, requests
page = requests.get('https://www.youtube.com/', timeout=(5, None))
soup = bs4.BeautifulSoup(page.text, 'html.parser')
if page.status_code==200:
    print("=" * 30 + "Title" +"=" * 30)
    title = soup.select('h3 a')
    single = soup.find_all('span', class_="accessible-description")
    double = soup.find_all('a', class_="yt-uix-sessionlink spf-link ")
    triple = soup.select("ul[class='yt-lockup-meta-info']")

    for a in title:
        title = a['title']
        linkVideo = "Link = https://www.youtube.com"+a['href']
        print("Judul = ", title)
        print(linkVideo)
    for b in single:    
        durasi = b.get_text()
        print("Durasi = ",durasi)  
    for c in double:
        upload = c.get_text()
        link = "https://www.youtube.com"+c['href']
        print("Pengupload = ",upload)
        print("Link Pengupload = " + link)
    for ul in triple:
        items2 = ul.find('li').text
        print("Jumlah Viewer = " + items2)
        for li in ul.find_all('li'):
            items1 = li.text 
        print("Jumlah Waktu Upload = " + items1)
            
    print("==" * 30)
    
    
    

    
        

            
            
            
            
import requests, random, bs4,openpyxl
wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='movie'
sheet['A1']='序号'
sheet['B1']='电影名'
sheet['C1']='评分'
sheet['D1']='推荐语'
sheet['E1']='链接'
for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        num = titles.find('em',class_="").text
        title = titles.find('span', class_="title").text
        comment = titles.find('span',class_="rating_num").text
        url_movie = titles.find('a')['href']

        if titles.find('span',class_="inq") != None:
            tes = titles.find('span',class_="inq").text
            sheet.append([num,title,comment,tes,url_movie])
            print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes +'\n' + url_movie)
        else:
            sheet.append([num,title,comment,tes,url_movie])
            print(num + '.' + title + '——' + comment + '\n' +'\n' + url_movie)
wb.save('movie.xlsx')

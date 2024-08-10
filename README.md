# 安裝說明（建議使用虛擬環境）
```
pip install -r requirements.txt
```


# Github Token
- 可以在設定>開發人員>創建personal access token，放入`local.env`，並將其改名為`.env`即可

# Google API
- 可以在[憑證頁面](https://console.cloud.google.com/projectselector2/apis/credentials?hl=zh-tw&pli=1&supportedpurview=project)申請API金鑰
- 並且在google cloud啟用Google Books API

# Backend
1. Spider撰寫
2. 新增API

# 待開發功能
1. 網頁呈現epub檔案
2. 線上瀏覽epub
3. 下載epub
4. 新增搜尋引擎（可以只串接google圖書，上面有很多書籍，但是有些不提供下載或檢閱，可以使用進階搜尋篩選掉）
https://www.google.com/search?hl=zh-TW&tbo=p&tbm=bks&q=OS&tbs=,bkv:f,bkt:b&num=50
5. 完善從github repo下載電子書的功能，解析repo URL，自動使用method


# 架構介紹
該電子書平台後端專案架構分為
1. 以fastAPI為主的後端server程式，負責從DB中提取資料傳送給前端，處理任務等
需要注意的是

2. Scrapy爬蟲架構，可以自己撰寫想要爬取的平台，透過items.py定義資料格式，使用pipelines.py將資料做處理之後存入資料庫，每個不同的平台都是一個有唯一name的spider
需要注意的是爬蟲應盡可能獨立運行，力求爬取其他平台的所有資料，爬取流程是定時任務。可以串接平台的API，或者解析頁面，想辦法拿到資料即可
（目前資料庫和爬蟲專案都放在後端專案中，後續可以將爬蟲專案獨立出來運行。）

3. DB，這裡使用sqlite，懶得架MySQL，table的欄位十分簡潔只有url, title, category, date, describe, source
url是該電子書的連結，該連結可以是下載連結、預覽連結等，預期使用者點擊這個url後就可以得到電子書相關的資訊
title是該電子書的書名，會被用來進行搜尋
category該電子書的分類，可以空白，若能提供那最好，後續可以做filter
date該電子書的出版日期，如果沒有那就以今天為date
describe該電子書的簡介，可以被用來搜尋
source該電子書來源於哪一個平台的資料，可以用來做filter


# 使用說明
```
source .venv/bin/activate
```
爬蟲已經事先爬好並將資料儲存到ebook.db，直接運行main.py開啟server即可
開啟後端Server
```
python main.py
```
查看swagger文件
127.0.0.1:8000/docs

可以使用以下API來測試搜尋
```
127.0.0.1:8000/search?query=0
```

要運行爬蟲請切換目錄至ebook_scraper底下，輸入以下指令啟動爬蟲
```
scrapy crawl <spider_name>
```
# Gradio
如果要使用 Gradio 版本的介面，跟上面一樣使用虛擬環境後，執行
```
python main_gradio.py
```
並且到 http://127.0.0.1:7860 測試即可

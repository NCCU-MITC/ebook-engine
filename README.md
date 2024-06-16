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

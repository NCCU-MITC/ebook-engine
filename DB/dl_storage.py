import requests
import urllib.parse
import urllib.parse

# 原始 gs URL
gs_url = "gs://ebook-mitc-bucket/AIR 青空-Air in Summer.epub"

# 提取 bucket 名稱和檔案路徑
bucket_name = gs_url.split('/')[2]
file_path = '/'.join(gs_url.split('/')[3:])

# 轉換為 https URL
https_url = f"https://storage.googleapis.com/{bucket_name}/{file_path}"

# 編碼空格和中文字
encoded_url = urllib.parse.quote(https_url, safe=':/')

print(encoded_url)

# 公開檔案的 HTTP(S) URL
url = encoded_url

# 下載檔案
response = requests.get(url)

# 確認請求成功
if response.status_code == 200:
    with open('downloaded.epub', 'wb') as f:
        f.write(response.content)
    print('檔案已下載至 downloaded.epub')
else:
    print(f'下載失敗，狀態碼: {response.status_code}')

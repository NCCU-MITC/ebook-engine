import requests
from dotenv import load_dotenv
import os


load_dotenv()
token = os.getenv("GITHUB_TOKEN")
# 將以下字符串替換為您的個人訪問令牌

headers = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/vnd.github.v3+json',
}

# 指定用戶名和倉庫名
username = 'fancy88'
repo = 'iBook'

response = requests.get(f'https://api.github.com/repos/{username}/{repo}/contents', headers=headers)

# 列印出所有文件的名稱
for file in response.json():
    print(file['name'])
    # if file['name'].endswith('.epub'):
    #     # 獲取文件的URL
    #     url = file['download_url']

    #     # 下載文件
    #     response = requests.get(url)
    #     with open(file['name'], 'wb') as f:
    #         f.write(response.content)

    #     print(f"已下載文件：{file['name']}")
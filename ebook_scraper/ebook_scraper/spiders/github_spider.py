import scrapy
from urllib.parse import unquote
import time
import os
from dotenv import load_dotenv
from datetime import datetime
import sqlite3
from ebook_scraper.items import EbookItem

class GithubSpider(scrapy.Spider):
    name = 'github_spider'

    # fancy88/iBook
    # it-ebooks-0/it-ebooks-2022
    def __init__(self, username="it-ebooks-0", repo="it-ebooks-2022", *args, **kwargs):
        super(GithubSpider, self).__init__(*args, **kwargs)
        load_dotenv()
        token = os.getenv("GITHUB_TOKEN")
        self.token = token
        self.username = username
        self.repo = repo
        self.start_urls = [f'https://api.github.com/repos/{self.username}/{self.repo}/contents']
        self.epub_save_path = os.getenv("EPUB_SAVE_PATH")


    def start_requests(self):
        headers = {'Authorization': f'token {self.token}'}
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers, callback=self.parse)

    def parse(self, response):
        if response.status == 403:
            # 如果收到403錯誤，則可能達到速率限制
            retry_after = response.headers.get('Retry-After')
            if retry_after:
                wait_time = int(retry_after)
                self.log(f"Rate limit exceeded. Retrying in {wait_time} seconds.")
                time.sleep(wait_time)
                yield scrapy.Request(response.url, callback=self.parse, dont_filter=True)
        else:
            # 解析JSON響應
            files = response.json()
            for file in files:
                # 檢查文件是否為.epub文件
                if file['name'].endswith('.epub'):
                    # 獲取文件的URL
                    url = file['download_url']
                    # 將文件URL傳遞給save_epub方法
                    yield scrapy.Request(url, callback=self.save_epub, meta={'file_info': file})

    def save_epub(self, response):
        if not os.path.exists(self.epub_save_path):
            os.makedirs(self.epub_save_path)
        # 從URL中獲取文件名
        filename = response.url.split("/")[-1]
        filename = unquote(filename)# 解碼文件名
        # 檢查文件是否已存在
        if os.path.exists("epub/"+filename):
            self.log(f'File {filename} already exists. Skipping download.')
            return self.save_to_db(response)
        else:
            os.makedirs(self.epub_save_path, exist_ok=True)
            # 將文件保存到本地
            # file_path = os.path.join(self.epub_save_path, filename)
            # with open(file_path, 'wb') as f:
            #     f.write(response.body)
            # self.log(f'Saved file {filename}')
            self.log("Success")
            return self.save_to_db(response)

    def save_to_db(self, response):
        # 生成 item 並傳遞給 pipeline
        file_info = response.meta['file_info']
        item = EbookItem()
        item['url'] = file_info['download_url']
        item['title'] = file_info['name']
        item['category'] = 'Unknown'  # 這裡可以根據需要設置
        item['date'] = datetime.now().strftime('%Y-%m-%d')
        item['describe'] = 'No description'  # 這裡可以根據需要設置
        item['source'] = 'GitHub'
        yield item



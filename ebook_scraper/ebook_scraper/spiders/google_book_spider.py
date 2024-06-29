import scrapy
from dotenv import load_dotenv
import os
import requests
import time
import json


# 不要理這個檔案，測試用

class GoogleBooksSpider(scrapy.Spider):
    name = 'google_books_spider'
    allowed_domains = ['www.googleapis.com']
    
    def __init__(self, query='OS', maxResults=40,printType="books",orderBy="newest", queue=None, *args, **kwargs):
        super(GoogleBooksSpider, self).__init__(*args, **kwargs)
        load_dotenv()
        google_books_api_key = os.getenv("GOOGLE_API_KEY")
        self.google_books_api_key = google_books_api_key
        self.query = query
        self.maxResults = maxResults
        self.printType = printType
        self.orderBy = orderBy
        self.start_urls = [f"https://www.googleapis.com/books/v1/volumes?q={self.query}&download=epub&filter=full&maxResults={ self.maxResults }&printType={self.printType}&orderBy={self.orderBy}&key={self.google_books_api_key}"]
        self.epub_save_path = os.getenv("EPUB_SAVE_PATH")
        self.queue = queue # 儲存queue

    def start_requests(self):
        for url in self.start_urls:
            print(f"Sending request to {url}")
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text)
        # print(data)
        results = []
        for item in data['items']:
            result = {
                'title': item['volumeInfo'].get('title', ''),
                'authors': item['volumeInfo'].get('authors', ''),
                'publishedDate': item['volumeInfo'].get('publishedDate', ''),
                'description': item['volumeInfo'].get('description', ''),
                'pageCount': item['volumeInfo'].get('pageCount', ''),
                'categories': item['volumeInfo'].get('categories', ''),
                'thumbnail': item['volumeInfo'].get('imageLinks', {}).get('thumbnail', '') if 'imageLinks' in item['volumeInfo'] else '',
                'language': item['volumeInfo'].get('language', ''),
                'previewLink': item['volumeInfo'].get('previewLink', '')
            }
            results.append(result)
        self.queue.put(results)

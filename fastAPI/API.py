from fastapi import FastAPI, BackgroundTasks
from threading import Thread
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from ebook_scraper.ebook_scraper.spiders.github_spider import GithubSpider
from dotenv import load_dotenv
from ebook_scraper.ebook_scraper.spiders.google_book_spider import GoogleBooksSpider
import os
from models import GithubSpiderData, GoogleBooksSpiderData
from elasticsearch import Elasticsearch


app = FastAPI()
es = Elasticsearch()




def run_github_spider(username, repo):
    process = CrawlerProcess(get_project_settings())
    process.crawl(GithubSpider, username=username, repo=repo)
    process.start()

def run_google_books_spider(query):
    process = CrawlerProcess(get_project_settings())
    process.crawl(GoogleBooksSpider, query=query)
    process.start()


@app.get("/search")
async def search(query: str):
    res = es.search(index="ebook", body={"query": {"match": {'title': query}}})
    return res['hits']['hits']
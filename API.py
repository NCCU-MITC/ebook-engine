from fastapi import FastAPI, BackgroundTasks
import sqlite3
from elasticsearch import Elasticsearch


app = FastAPI()

# 之後想要用elastic search做看看QQ，但是一開始還是用sqlite3
# es = Elasticsearch()

@app.get("/search")
async def search(query: str):
    conn = sqlite3.connect("ebook.db")
    c = conn.cursor()
    c.execute("SELECT * FROM ebook WHERE title LIKE ? OR describe LIKE ?", ('%' + query + '%', '%' + query + '%'))
    results = c.fetchall()
    conn.close()
    return results
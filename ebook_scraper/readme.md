- 運行爬蟲
```
scrapy crawl github_spider
```

# github_spider
目前需要使用者提供要爬取的github repo name才可以進行爬取，畢竟github本來就不是做電子書的，後續有更好的方法在另外加上去



Scrapy 爬蟲類 (Spider) 提供了多種常見的方法,您可以根據需求使用它們來實現各種爬取功能。以下是一些常用的方法:

1. **`start_requests(self)`**:
   - 這個方法是 Scrapy 的入口點,用於生成初始的請求。如果沒有定義此方法,Scrapy 會使用 `start_urls` 屬性來生成初始請求。

2. **`parse(self, response)`**:
   - 這是最常用的方法之一,用於解析請求的響應並生成後續的請求或項目。當您使用 `response.follow()` 或 `response.css()` 等方法時,Scrapy 會自動將解析結果傳遞到 `parse` 方法中。

3. **`closed(self, reason)`**:
   - 當爬蟲完成時,Scrapy 會調用這個方法。您可以在這裡執行一些清理或後處理任務。

4. **`start_urls`**:
   - 這是一個列表,包含爬蟲的初始 URL。如果沒有定義 `start_requests` 方法,Scrapy 會自動根據這個列表生成初始請求。

5. **`allowed_domains`**:
   - 這個屬性指定了爬蟲允許訪問的域名。Scrapy 會自動過濾掉不在這個列表中的 URL。

6. **`custom_settings`**:
   - 這個屬性允許您為特定的爬蟲設置自定義的配置,覆蓋全局的 `settings.py` 設置。

7. **`from_crawler(cls, crawler)`**:
   - 這個類方法在爬蟲被創建時調用,您可以在這裡訪問 Scrapy 的全局配置和資源。

8. **`__init__(self, *args, **kwargs)`**:
   - 這是 Python 的標準初始化方法,您可以在這裡初始化爬蟲的一些參數或狀態。

9. **`handle_httpstatus_list`**:
   - 這個屬性指定了爬蟲能夠處理的 HTTP 狀態碼列表。默認情況下,Scrapy 會拋出異常來處理不在這個列表中的狀態碼。

10. **`handle_spider_closed(self, spider, reason)`**:
    - 當一個爬蟲被關閉時,Scrapy 會調用這個方法。您可以在這裡執行一些清理或統計任務。

除了這些常見的方法,Scrapy 還提供了許多其他的方法和屬性,您可以根據具體需求進行選擇和使用。如果您有任何其他問題,歡迎隨時詢問。
import mysql.connector
import os

# 讀取環境變數
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
db_port = os.getenv('DB_PORT')


# 連接到資料庫
db = mysql.connector.connect(
    host=db_host, ## 
    port=db_port, ##
    user=db_user, ##
    password=db_pass, ##
    database=db_name ##
)

cursor = db.cursor()
query = """
select * from eBook
where title like '%第一卷%';
"""
cursor.execute(query)

# 印出結果
for x in cursor:
    print(x)

cursor.close()
db.close()

# 根據gs://ebook-mitc-bucket/终焉的年代记-第一卷 下.epub 取得google cloud storage的檔案
from google.cloud import storage

BUCKET_NAME = 'ebook-mitc-bucket'
# 初始化 GCP Storage 客戶端
client = storage.Client()
bucket = client.bucket(BUCKET_NAME)

# 指定要下載的檔案名稱
filename = '终焉的年代记-第一卷 下.epub'
# 指定要下載的檔案路徑
blob = bucket.blob(filename)
# 下載檔案
blob.download_to_filename(filename)
print(f'Downloaded {filename} from {BUCKET_NAME}')

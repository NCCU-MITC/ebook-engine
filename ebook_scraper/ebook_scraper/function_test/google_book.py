import requests
from dotenv import load_dotenv
import os


load_dotenv()
google_books_api_key = os.getenv("GOOGLE_API_KEY")
query = 'OS'
response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={query}&download=epub&filter=full&maxResults=40&printType=books&orderBy=newest&key=' + google_books_api_key)
print(response.json())
# https://www.googleapis.com/books/v1/volumes?q=*&download=epub&filter=full&maxResults=40&printType=books&orderBy=newest&key=
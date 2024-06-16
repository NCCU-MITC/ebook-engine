from pydantic import BaseModel

class GithubSpiderData(BaseModel):
    username: str
    repo: str

class GoogleBooksSpiderData(BaseModel):
    query: str
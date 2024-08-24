FROM python:3.9-slim

# 設定工作目錄
WORKDIR /app

# 複製需求檔案
COPY requirements.txt .

# 安裝依賴
RUN pip install --no-cache-dir -r requirements.txt

# 複製專案檔案
COPY . .

# 開放端口
EXPOSE 8000

# 接收環境變數
ARG DB_HOST
ARG DB_PORT
ARG DB_NAME
ARG DB_USER
ARG DB_PASS

# ENV DB_USER=${DB_USER}
# ENV DB_PASSWORD=${DB_PASSWORD}

# 啟動 FastAPI 伺服器
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
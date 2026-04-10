FROM python:3.10-slim

RUN apt-get update && apt-get install -y wget gnupg2 apt-transport-https ca-certificates curl unzip

# ক্রোমের কি (key) যুক্ত করার নতুন পদ্ধতি
RUN curl -fsSL https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-chrome.gpg
RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list

RUN apt-get update && apt-get install -y google-chrome-stable

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
FROM python:3.11

WORKDIR /app

RUN apt update && apt install -y git && \
    git clone https://github.com/Kccorp/KcVe.git

WORKDIR /app/KcVe


RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
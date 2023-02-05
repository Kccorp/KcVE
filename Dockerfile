FROM python:3.11

WORKDIR /app

RUN apt update && apt install -y git && \
    git clone https://github.com/Kccorp/KcVe.git

VOLUME /app/results

RUN python KcVE/main.py

ENTRYPOINT ["python", "KcVE/main.py"]
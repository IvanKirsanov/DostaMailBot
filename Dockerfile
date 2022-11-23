FROM python:3.8.15

WORKDIR /home/bot

COPY . .

RUN pip3 install aiogram==2.21

CMD ["python3", "main.py"]
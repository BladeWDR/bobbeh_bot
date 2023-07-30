FROM python:latest
LABEL maintainer="bladewdr"

WORKDIR /opt/bobbeh_bot
COPY main.py .

RUN pip install python-telegram-bot

CMD ["python", "./main.py"]

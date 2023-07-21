FROM python:latest
LABEL maintainer="bladewdr"

WORKDIR /opt/bobbeh_bot
COPY main.py ./

CMD ["python", "./main.py"]
FROM python:3-slim-buster
LABEL MAINTAINER="jnmcfly"
COPY requirements.txt /app/req.txt
COPY main.py /app/main.py
WORKDIR /app/
RUN pip install --no-cache-dir -r req.txt
CMD telegram-send --config /root/.config/telegram-send.conf && python -u ./main.py
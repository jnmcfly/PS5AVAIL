FROM python:3
LABEL MAINTAINER="jnmcfly"
COPY requirements.txt /app/req.txt
COPY main.py /app/main.py
WORKDIR /app/
RUN pip install --no-cache-dir -r req.txt
CMD [ "python", "-u", "./main.py" ]
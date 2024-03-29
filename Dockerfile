FROM python

LABEL org.opencontainers.image.source https://github.com/djharshit/temp-check
LABEL maintainer = "Harshit M"

WORKDIR /home/app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python3", "server.py" ]
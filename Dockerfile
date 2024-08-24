FROM python:3.11-slim

LABEL org.opencontainers.image.source="https://github.com/djharshit/temp-check"
LABEL maintainer="Harshit M"

WORKDIR /home/app

COPY . .

RUN chmod +x install.sh && chmod +x run.sh && ./install.sh

EXPOSE $PORT

CMD [ "./run.sh" ]
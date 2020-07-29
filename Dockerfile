FROM python:3.8.5-alpine3.12
COPY tweetbot.py /usr/local/bin/
RUN adduser -S pigeon
USER pigeon
ENTRYPOINT ["python /usr/local/bin/tweetbot.py"]
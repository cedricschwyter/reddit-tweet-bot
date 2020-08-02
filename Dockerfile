FROM python:3.8.5-alpine3.12
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY tweetbot .
RUN chmod +x tweetbot
RUN adduser -S pigeon
USER pigeon
ENTRYPOINT ["./tweetbot"]
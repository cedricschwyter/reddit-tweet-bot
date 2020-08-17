FROM python:3.8.5-alpine3.12
RUN adduser -S pigeon
WORKDIR /home/pigeon
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY tweetbot .
RUN chmod +x tweetbot
USER pigeon
ENTRYPOINT ["./tweetbot"]
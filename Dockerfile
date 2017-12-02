FROM python:latest

RUN mkdir -p /home/game/
WORKDIR /home/game/
ADD ./ /home/game/

RUN pip install -r requirements.txt
WORKDIR /home/game/src/

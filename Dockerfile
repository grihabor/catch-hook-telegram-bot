FROM python:3.6-alpine
MAINTAINER Borodin Gregory <grihabor@gmail.com>

WORKDIR /project

ADD catchbot .
RUN pip3 install .

CMD ["catchbot", "run"]

FROM phusion/baseimage
FROM python:3
FROM swernst/locusts

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update -qq && apt-get install -y build-essential \
    libpq-dev python3-pip ca-certificates curl\
    libssl-dev apt-utils openssh-server openssh-client&& \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /usr/src/app/

ADD ./ /usr/src/app/

WORKDIR /usr/src/app

RUN pip3 install --no-cache-dir -r ./scripts/requirements.txt

# Create user and group
RUN groupadd --gid 9999 app && \
    useradd --uid 9999 --gid app app && \
    chown -R app:app /usr/src/app/

#Expose app port

EXPOSE 80 800 8089  


FROM locustio/locust
FROM phusion/baseimage:0.10.1
ENV PYTHONHONUNBUFFERED 1

# Setup update, install oracle lib and clean instalation
RUN apt-get update && apt-get -y install \
    sudo \
    curl \
    wget \
    unzip \
    git \
    vim \
    xterm \
    python3 \
    python3-pip \  
    build-essential \
    libssl-dev \
    #&& pip3 install locustio \
    && apt-get clean && rm -rf /var/cache/apt/* /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Create code and copy project to
RUN mkdir /code
WORKDIR /code

# Set locale config
RUN locale-gen en_US.UTF-8
RUN dpkg-reconfigure locales

# Insert bashrc values
RUN echo "export LC_ALL=en_US.UTF-8" >> /root/.bashrc
RUN echo "export LANG=en_US.UTF-8" >> /root/.bashrc

# Upgrade Pip, install virtualenvwrapper(virtualenv) and install google-apputils  
RUN pip3 install --upgrade pip
RUN pip3 install virtualenvwrapper
RUN pip3 install locustio==0.13.5

RUN mkdir ~/.virtualenvs

# Set env locate configs
ENV export HOME=$PWD
ENV export WORKON_HOME=$HOME/.virtualenvs
ENV export PROJECT_HOME=$HOME/code
ENV export VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3'
#ENV export VIRTUALENVWRAPPER_SCRIPT=/usr/local/bin/virtualenvwrapper.sh

# Set source virtualenv and install requirements
#RUN /bin/bash -c "source /usr/local/bin/virtualenvwrapper.sh" \
#    && mkvirtualenv mve_locus \
#    && workon mve_locus

# Create log file
RUN touch mve.out

#Add locus to code
ADD . /code

# Create user and group
RUN groupadd --gid 9999 app && \
    useradd --uid 9999 --gid app app && \
    chown -R app:app /code

#Start up
#RUN echo "/usr/local/bin/virtualenvwrapper.sh" >> /root/.bashrc
#RUN echo "workon mve_locus" >> /root/.bashrc

EXPOSE 80 443
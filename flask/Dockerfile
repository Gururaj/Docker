FROM ubuntu:18.04

MAINTAINER Gururaj Seetharama "gsmayya@gmail.com"

ENV REDIS_USER=redis \
    REDIS_DATA_DIR=/var/lib/redis \
    REDIS_LOG_DIR=/var/log/redis

# install apache and other things. 
RUN apt-get update -y && apt-get install -y apache2 \
    libapache2-mod-wsgi \
    build-essential \
    python \
    python-dev\
    python-pip \
    vim \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*


# We copy just the requirements.txt first to leverage Docker cache
# This is for local server setup

COPY ./requirements.txt /var/www/apache-flask/app/requirements.txt

RUN pip install -r /var/www/apache-flask/app/requirements.txt

# Redirect access and error logs of apache to std
RUN ln -sf /proc/self/fd/1 /var/log/apache2/access.log && \
    ln -sf /proc/self/fd/1 /var/log/apache2/error.log

# Copy over the apache configuration file and enable the site
COPY ./apache-flask.conf /etc/apache2/sites-available/apache-flask.conf
RUN a2ensite apache-flask
RUN a2enmod headers

# Copy over the wsgi file
COPY ./apache-flask.wsgi /var/www/apache-flask/apache-flask.wsgi

COPY ./start_server.py /var/www/apache-flask/run.py
# not copying since compose takes care of mounting volume
#COPY ./app /var/www/apache-flask/app/

RUN a2dissite 000-default.conf
RUN a2ensite apache-flask.conf
EXPOSE 80

WORKDIR /var/www/apache-flask

CMD  /usr/sbin/apache2ctl -D FOREGROUND


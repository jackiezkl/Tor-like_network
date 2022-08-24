FROM alpine:latest

#RUN apk update && apk add nodejs npm
RUN apk update && apk add xvfb firefox dbus py-pip ttf-dejavu ethtool tshark

ADD https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz /bin/
RUN tar -zxvf /bin/geckodriver* -C /bin/
ENV PATH /bin/geckodriver:$PATH

RUN mkdir /root/pyvenv && python3 -m venv /root/pyvenv
RUN source /root/pyvenv/bin/activate && pip install --upgrade pip && pip install selenium requests

#RUN apk add openrc
#RUN mkdir /etc/local.d
#RUN echo "#!/bin/sh">/etc/local.d/Xvfb.start
#RUN echo "/usr/bin/Xvfb :99 -ac &">>/etc/local.d/Xvfb.start
#RUN echo chmod +x /etc/local.d/Xvfb.start
#RUN rc-update add local default

#RUN addgroup -S docker && adduser -S -G docker -D -g '' -s /bin/sh docker

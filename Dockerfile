
 
FROM python:3
USER root

# 以下はLinuxのコマンド。日本語やpip、jupyterlabの設定をしている
RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less

# コピーとパッケージのインストール
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt



# Install MySQL client
RUN apt-get install -y default-libmysqlclient-dev
RUN pip install mysqlclient



# Djangoおよびその他のパッケージのインストール
RUN python -m pip install django
RUN python -m pip install djangorestframework
RUN python -m pip install markdown
RUN python -m pip install django-filter
RUN python -m pip install django-cors-headers
RUN python -m pip install djoser
RUN python -m pip install djangorestframework-simplejwt
FROM ubuntu

RUN apt-get update
RUN apt-get -y install nginx

RUN apt-get update
RUN apt-get install --no-install-recommends -y python3.8 python3-pip python3.8-dev

COPY . /.

RUN update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1
RUN pip install -r requirements.txt

RUN rm /var/www/html/index.nginx-debian.html
RUN pytest -q tests --html=/var/www/html/index.nginx-debian.html --self-contained-html

EXPOSE 80
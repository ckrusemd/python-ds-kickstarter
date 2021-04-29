FROM ubuntu:latest

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y dist-upgrade
RUN DEBIAN_FRONTEND=noninteractive apt-get -yq install net-tools nginx
RUN useradd -ms /bin/bash aurora
RUN rm -f /etc/nginx/fastcgi.conf /etc/nginx/fastcgi_params && \
    rm -f /etc/nginx/snippets/fastcgi-php.conf /etc/nginx/snippets/snakeoil.conf

EXPOSE 80
EXPOSE 443

COPY nginx/ssl /etc/nginx/ssl
COPY nginx/snippets /etc/nginx/snippets
COPY nginx/sites-available /etc/nginx/sites-available

COPY . /.
RUN pip install -r requirements.txt

ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;"]
FROM python:latest

COPY app/requirements.txt /var/www/app/
RUN pip3 install -r /var/www/app/requirements.txt

COPY . /var/www/app/

CMD ["/usr/local/bin/uwsgi", "--ini", "/var/www/app/app/uwsgi.ini"]

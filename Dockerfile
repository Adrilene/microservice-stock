FROM python:3-alpine
RUN apk add --virtual .build-dependencies \
    --no-cache \
    python3-dev \
    build-base \
    linux-headers \
    pcre-dev
RUN apk add --no-cache pcre
WORKDIR /stock
COPY . /stock
RUN pip install -r /stock/requirements.txt
RUN pip install uwsgi
RUN apk del .build-dependencies && rm -rf /var/cache/apk/*
EXPOSE 5003
CMD ["uwsgi", "--ini", "/stock/wsgi.ini"]
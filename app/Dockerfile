FROM python:3.9.6-alpine

# Установка локальных переменных
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Установка зависимостей для Django
RUN apk update \
    && apk add postgresql \
    && apk add postgresql-dev \
    && apk add gcc libc-dev make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev \
    && apk add jpeg-dev zlib-dev libjpeg libffi-dev
#     && pip install Pillow \
#     && apk del build-deps

# ENV LANG C.UTF-8
# ENV LC_ALL C.UTF-8

CMD python3 --version
# CMD . env/bin/activate
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .


# run entrypoint.sh
# COPY ../entrypoint.sh .
# RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
# RUN chmod +x /usr/src/app/entrypoint.sh

# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

# Django + Docker

## [Django](https://www.djangoproject.com/)
**Web Application Framework**

**MVC 모델**을 지원한다. 단 `view`는 django에서 `template`으로 `controller`는 `view`로 통한다. 이를 보통 **MVT 모델**이라 부른다.

**ORM**이 내장되어 있다

쉬운 **URL** 파싱 기능을 지원한다

관리자(admin) 페이지를 자동으로 생성한다


#### requirements.txt
```
Django==2.0.6
djangorestframework==3.8.2
pytz==2018.5
```

* [`Django`](https://www.djangoproject.com/) => django framework
* [`djangorestframework`](http://www.django-rest-framework.org/) => django에서 rest api 설계를 도와줌
* [`pytz`](https://pypi.org/project/pytz/) => timezone 설정

#### django_test

```
    python3 manage.py startapp django_test
```
위의 명령어를 통해서 app 생성

##### API

```
GET /
```

DB가 필요하지 않은 간단한 API이므로 `views.py` 및 `urls.py`만 수정

-------------------------------------------------
#### TODO
* DB를 연결해 **CRUD** 구현
* **django-swagger** 추가

## Docker
#### Dockerfile
```
FROM python:3

RUN mkdir /app
WORKDIR /app
COPY django_app /app
RUN pip install -r requirements.txt
```

[**docker + django**](https://docs.docker.com/compose/django/#create-a-django-project) 참조

**python3**가 설치되어 있는 `python:3` 이미지를 베이스이미지로 설정
django app이 저장된 **django_app**를 **/app**에 옮긴다
해당 directory로 위치를 변경해, **requirement.txt**를 통해 dependencies을 설치

> 현재는 docker에 django app만 설치하고 배포하므로 `virtual env`를 따로 설치하지 않았음
후에 `gunicorn`으로 **wsgi**대체

#### docker-compose.yml
```
version: '3'

services:
  web:
    build: .
    command: python3 manage.py runserver 0.0.0.0:8000
    ports:
      - "8000:8000"
```
같은 directory에 있는 Dockerfile로 build
외부포트 8000번과 내부포트 8000번 연결

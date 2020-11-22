FROM python:3.9

WORKDIR /usr/src/app
COPY . ./

RUN pip install pipenv && pipenv install

CMD ["pipenv", "run", "flask", "run", "--host", "0.0.0.0", "--port", "$APP_PORT"]

FROM python:3

WORKDIR /data

RUN pip install django==3.2

COPY . .

RUN python manage.py migrate

EXPOSE 3000

CMD ["python","manage.py","runserver","0.0.0.0:3000"]



FROM python:3-alpine
WORKDIR /srv
RUN pip install --upgrade pip
RUN pip install flask
COPY . /srv
ENV FLASK_APP=app
CMD ["python","app.py"]
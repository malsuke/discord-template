FROM python:3.12

WORKDIR /usr/src/app

COPY ./app .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
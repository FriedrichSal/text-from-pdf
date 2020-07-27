FROM python:3.7

# poppler for pdftotext
RUN apt-get update && apt-get -y install build-essential libpoppler-cpp-dev pkg-config python-dev

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

EXPOSE 80

COPY . /app

CMD ["python", "app.py"]

FROM python:3.10-slim

RUN pip install --upgrade pip

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r /requirements.txt

WORKDIR /src
COPY . .

CMD ["bash", "run.sh"]
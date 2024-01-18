#FROM ubuntu:19.10
FROM python:3.9-bullseye

COPY ./api /api/api
COPY requirements.txt /requirements.txt

# RUN apt-get update \
#     && apt-get install python3-dev python3-pip -y \
#     && pip3 install -r requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

ENV PYTHONPATH=/api
WORKDIR /api

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["api.main:app", "--host", "0.0.0.0"]

#How to run: docker build --file Dockerfile --tag fastapi-capstone .
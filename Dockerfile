FROM python:3.8-buster

# set working directory

WORKDIR /app
RUN mkdir -p /app

# install system dependencies

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

RUN echo "tzdata tzdata/Areas select America" > /tmp/preseed.txt; \
    echo "tzdata tzdata/Zones/Europe select Bogota" >> /tmp/preseed.txt; \
    debconf-set-selections /tmp/preseed.txt && \
    apt-get update && \
    apt-get install -y tzdata


RUN apt-get update -y && apt-get install -y libgl1-mesa-glx \
	&& apt-get install -y libsm6 libxext6 && apt-get install -y git

# install dependencies

# copy content
ADD ./app /app
ADD ./models ../models
COPY ./requirements.txt .
#install python dependencies
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

#expose ports
EXPOSE 8001 5005 8005

CMD ["gunicorn","-c","gunicorn.py","-k","uvicorn.workers.UvicornWorker", "app:app"]

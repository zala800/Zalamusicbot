FROM nikolaik/python-nodejs:python3.10-nodejs17

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y
RUN pip3 install -U pip
RUN curl -sL https://deb.nodesource.com/setup_15.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
RUN mkdir /app/
COPY . /app/
WORKDIR /app/
RUN chmod 777 /app
RUN pip3 install --no-cache-dir -U -r requirements.txt
CMD python3 -m Zalamusic
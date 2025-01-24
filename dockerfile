FROM python:3.8

# set work directory
WORKDIR /usr/src/app/

# copy project
COPY . /usr/src/app/

# install dependencies
RUN pip install --upgrade pip

RUN pip install --user 'aiogram==3.6.0', 'pygsheets==2.0.6', 'google-api-python-client==2.127.0', 'oauth2client==4.1.3'

# install git
RUN apt-get update && apt-get install -y git

# configure git to trust the directory
RUN git config --global --add safe.directory /usr/src/app

# copy the watch script
COPY watch_git.sh /usr/src/app/watch_git.sh

# make the watch script executable
RUN chmod +x /usr/src/app/watch_git.sh

# run the watch script
CMD ["/usr/src/app/watch_git.sh"]

FROM python:3.8
# set work directory
WORKDIR /usr/src/app/
# copy project
COPY . /usr/src/app/
# install dependencies
RUN pip install --upgrade pip

RUN pip install --user 'aiogram==3.6.0', 'pygsheets==2.0.6', 'google-api-python-client==2.127.0', 'oauth2client==4.1.3'
# run app
CMD ["python", "bot.py"]
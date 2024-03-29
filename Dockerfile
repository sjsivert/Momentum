FROM python:3.6
ENV FLASK_APP flaskr
ENV FLASK_ENV development
ENV APP_HOME /app
RUN mkdir $APP_HOME
WORKDIR $APP_HOME
COPY requirements.txt $APP_HOME
RUN pip install -r requirements.txt
COPY src $APP_HOME
RUN pip install -e .
CMD flask run --host=0.0.0.0


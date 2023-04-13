FROM python:3.10

RUN mkdir -p /home/app

RUN addgroup --system app && adduser --system --group app


# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/code
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
ENV ENVIRONMENT prod


# Install Python Dependencies
RUN pip install --upgrade pip

COPY src/requirements.txt .

RUN pip install -r requirements.txt

# copy app
COPY src .

RUN chown -R app:app $APP_HOME

# change to the app user
USER app

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]

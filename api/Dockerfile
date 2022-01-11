FROM python:3.6.1

ENV PYTHONUNBUFFERED 1
ENV HOST 0.0.0.0
ENV PORT 5009
ENV DEBUG true
COPY . /api
#COPY /var /var
WORKDIR /api

# install requirements
#RUN apt update; apt-get -y install python3-matplotlib

RUN pip install -r requirements.txt

# expose the app port
EXPOSE 5009

RUN pip install gunicorn

# # # run the app server in production with gunicorn
# CMD ["gunicorn", "--bind", "0.0.0.0:5009", "--workers", "3", "app:app", "--error-logfile", "error.log", "--capture-output"]

# run the flask development server
CMD [ "flask", "run", "--host=0.0.0.0", "--port=5009", "--debugger"]

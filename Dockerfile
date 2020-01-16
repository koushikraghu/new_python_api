#TAG v1.0
FROM python:3
RUN apt-get update
RUN mkdir /app
WORKDIR /app
COPY controller /app/controller
COPY model /app/model
COPY routes /app/routes
COPY settings /app/settings
COPY index.py /app/index.py
RUN pip3 install --upgrade pip
RUN apt-get update && apt-get install vim -y
EXPOSE 5555
CMD ["python","app.py"]
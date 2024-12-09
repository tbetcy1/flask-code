FROM python:latest

WORKDIR /app

COPY . .

EXPOSE 8080

RUN pip install -r requirments.txt

ENTRYPOINT [ "python","app.py" ]

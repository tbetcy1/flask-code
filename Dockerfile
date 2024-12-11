FROM python:latest

WORKDIR /app

COPY . /app

# EXPOSE 5000

RUN pip install -r requirments.txt

ENTRYPOINT [ "python3","app.py" ]

#CMD ["flask", "run", "--host", "0.0.0.0" ]
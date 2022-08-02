FROM python:slim

WORKDIR /app

COPY src/*.py .

RUN pip install flask

EXPOSE 8080
CMD ["python", "main.py"]


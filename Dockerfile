FROM python:3.9-slim

WORKDIR /app

COPY flask-app.py .

RUN pip install flask

EXPOSE 5000

CMD ["python", "flask-app.py"]

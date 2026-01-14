FROM python:3.9-slim
WORKDIR /app
RUN pip install flask flask-sqlalchemy flask-jwt-extended flask-restx
COPY . .
EXPOSE 5000
CMD ["python", "run.py"]
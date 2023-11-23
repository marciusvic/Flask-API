FROM python:3.7.4-slim-buster

WORKDIR /app

COPY . .

RUN ls -al

RUN pip install -r requirements.txt

EXPOSE 4000

CMD ["flask", "run", "--host=0.0.0.0", "--port=4000"]
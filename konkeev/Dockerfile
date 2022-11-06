FROM python:3.10.6

COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
WORKDIR /app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]


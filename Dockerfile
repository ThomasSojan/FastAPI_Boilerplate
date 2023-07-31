FROM python:3.9

WORKDIR /app
 
COPY ./requirements.txt /app/requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src/ /app/src

WORKDIR /app/src

USER root

EXPOSE 8080

#CMD uvicorn main:app --reload --port 8080
 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

#CMD ["uvicorn", "main:app", "--host", "localhost", "--port", "8080"]

#CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]


FROM python:3.8.12-slim-buster
WORKDIR /app
COPY . .
COPY ./pip.conf /pip.conf
ENV PIP_CONFIG_FILE /pip.conf
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
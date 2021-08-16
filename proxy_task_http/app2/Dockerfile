FROM python:3
WORKDIR  /usr/src/app
COPY requirements.txt .
RUN pip install -qr requirements.txt
ADD app2.py .
CMD ["python3", "./app2.py"]

FROM python:3
WORKDIR  /usr/src/app
COPY requirements.txt .
RUN pip install -qr requirements.txt
ADD app1.py .
CMD ["python3", "./app1.py"]

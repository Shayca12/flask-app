FROM python:3.12-slim

WORKDIR /app

# install deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy app
COPY app.py .

EXPOSE 5000

# prod server
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]


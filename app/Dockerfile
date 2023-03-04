FROM python:3.10-slim

WORKDIR /home/app

ENV VAR1=10

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install requirements
RUN pip install --upgrade pip
COPY ./requirements-docker.txt /home/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /home/app/

# Creates a non-root user and adds permission to access the /app folder
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /home/app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

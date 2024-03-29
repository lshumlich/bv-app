#
# docker run -d -p 5010:5000 devopstraining
#
# For more information, please refer to https://aka.ms/vscode-docker-python
# Note: See the README.md for instructions on how to copy the docker image to you ECR to avoid docker limits
FROM 208019545904.dkr.ecr.ca-central-1.amazonaws.com/python:3.8-slim-buster
# FROM python:3.8-slim-buster
# The following image worked but it is huge
# FROM public.ecr.aws/sam/build-python3.8:latest

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
# RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
# USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
EXPOSE 5000
CMD ["python", "app.py"]
# CMD ["gunicorn"  , "-b", "0.0.0.0:80", "app:app"]

FROM python:3.10.11-slim

# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /app
WORKDIR /app

# to COPY the remote file at working directory in container
COPY main.py /app/

# CMD instruction should be used to run the software
# contained by your image, along with any arguments.
CMD [ "python", "main.py"]
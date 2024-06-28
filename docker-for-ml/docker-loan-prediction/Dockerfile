# Base Image
FROM python:3.8-slim-buster
#upgrade pip
RUN pip install --upgrade pip

# Copying all the files to source directory
COPY . /src

# set the working direcotyr
WORKDIR /src 

#Giving permission to  python file
RUN chmod +x docker_train.py

# Install required dependecies from requirement file
RUN pip install -r requirements.txt

# Run docker train.py 
ENTRYPOINT ["python"]

CMD ["docker_train.py"]
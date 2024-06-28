FROM python:3.8

#Set the directory of app
WORKDIR /usr/src/app

# Copy all the files directory
COPY . .

# Install Dependency
RUN pip install --no-cache-dir -r requirements.txt

# Port number to be exposed
EXPOSE 5000

# Run the command
CMD ["python","./app.py"]
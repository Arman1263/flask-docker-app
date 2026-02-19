# base image
FROM python

# create a workdir called app
WORKDIR /app

# copy all the file (.) in app
COPY . /app 

# run this command to install dependencies
RUN pip install -r requirements.txt

# expose port to run project on this port
EXPOSE 5000

# command to run the project - (.) becoz app file is in main directory
CMD [ "python", "./app.py" ]
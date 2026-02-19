## in app.py - flask app
app.run(host="0.0.0.0", port=5000) ## 0.0.0.0 becoz to run on all devices -- out of docker container

## to build the image of this project 
docker build -t armanshikalgar/flask-app

-- it is a best practice to use docker hub username along with image name
-- it helps to push this image on docker hub
-- this will image will shown in docker desktop

## to use this image in our sys as a container for testing
docker run -p 8888:5000 armanshikalgar/flask-app 

-- we exposed 5000 flask port on 8888 our custom port 
-- to check the running container go on - localhost:8888
-- and our container will be shown in docker desktop


## If I make in changes in code then re run the build command that is docker build

## Pushing our image on docker hub -->
docker login
docker push armanshikalgar/flask-app 

-- pushed successfully it will also shown in docker hub

## Now pull that image
docker run -d -p 8888:5000 --name flask-test armanshikalgar/flask-app

-- port mapping is imp to pull  

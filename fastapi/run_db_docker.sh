#!/bin/sh
docker run --name fastapi_mariadb -e MYSQL_ROOT_PASSWORD=root_password -e MYSQL_DATABASE=mydb -e MYSQL_USER=user -e MYSQL_PASSWORD=user_password -p 3306:3306 -d mariadb:latest


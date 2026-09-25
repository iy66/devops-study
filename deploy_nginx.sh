#!/bin/bash

if docker ps -a | grep -q my_web; then
    docker start my_web > /dev/null 2>&1
    echo "✅ Nginx запущен на http://localhost:9090"
else
    docker run -d --name my_web -p 9090:80 nginx > /dev/null 2>&1
    echo "✅ Nginx создан и запущен на http://localhost:9090"
fi

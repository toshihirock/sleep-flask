
```
# server
$git clone https://github.com/toshihirock/sleep-flask.git
$docker build -t flask_docker .
$docker run -p 80:80 -it flask_docker

# client
$curl http://localhost
$curl http://localhost/sleep
```

## Entity POS Recognition app is [deployed with wsgi server and hosted behind nginx on port 80](http://3.95.210.107/)

## Install the following requirements :
```
   pip3 install django
   pip3 install nltk
```
## Wondering what this application is about ?
1) The user enters a sentence or a paragraph as an input to this application.
2) The user gets back the breakup of the sentence as words and its POS(Part of Speech) tagging.
3) Helps user understand the sentence structure and leaves the audience with scope to dive deep in to NLP!!

## Awesome! Right?? But how does this works?
As the user enters text on the home page and hits RUN, the python does the magic of capturing
that statement and parsing it to the Python's NLTK library.
NLTK then breaks it down into parts and tries to map these words to different POS tags on the basis 
of what the library is trained on.

## Here's how the home page looks like
<p align='center'>
<img src='../master/input.PNG'>
</p>

## The output shows the Entity POS relationship of the input sentence
<p align='center'>
<img src='../master/output.PNG'>
</p>

## Steps to deploy Django app from GitHub to AWS EC2 with wsgi server and hosted behind nginx on port 80

```
gunicorn --bind 0.0.0.0:8000 entity.wsgi:application
```

```
sudo vim /etc/systemd/system/gunicorn.service
```
## Edit the gunicorn.service as follows
```
[Unit]
Description=gunicorn daemon
After=network.target
[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/cloud_project_1
ExecStart=/home/ubuntu/cloud_project_/venv/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/cloud_project_1/entity_app.sock entity.wsgi:application
[Install]
WantedBy=multi-user.target
```
```
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo vim /etc/nginx/sites-available/entity
```
## Edit site config as follows
```
server {
  listen 80;
  server_name 3.95.210.107;
  location = /favicon.ico { access_log off; log_not_found off; }
  location /static/ {
      root /home/ubuntu/cloud_project_1;
  }
  location / {
      include proxy_params;
      proxy_pass http://unix:/home/ubuntu/cloud_project_1/entity_app.sock;
}
}
```

```
sudo ln -s /etc/nginx/sites-available/entity /etc/nginx/sites-enabled
sudo nginx -t
sudo rm /etc/nginx/sites-enabled/default
sudo service nginx restart
```

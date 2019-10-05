# Host Multiple Flask Apps On One Host

## Requirements

-   SSL into the host

## Step by Step Guide

-   Step One: Have both Flask Apps ready to go
-   Open flask_settings with your editor. Configure a server port for as many apps as you want to run
-   Step Two: SSL into the host

*   Upload your Flask apps to the host

-   Install the dependencies / Pip
-   Install nginx

        sudo apt-get install nginx

-   Configure nginx
-   Remove sites enabled default

        sudo rm /etc/nginx/sites-enabled/default

-   in /etc/nginx/sites-enabled, upload flask_settings
-   start nginx

        sudo /etc/init.d/nginx start

-   Install gunicorn

        pip (pip3) install flask gunicorn

-   cd into your first flask app folder where your start up file is (app.py in this case)
-   Start gunicorn listening to the port from flask_settings

        gunicorn app:app -b:8000

-   new terminal, and gunicorn for the next flask app
-   Point your DNS at the right IP:port, or go to ipaddress:port and you will get the corresponding Flask App

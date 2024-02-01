intagnewspaper
==============

The styling and rendering for [intagnewspaper.org](http://intagnewspaper.org), a defunct Ecuadorean news publication based in the Intag Cloud Forest. Backend is Flask, MySQL, and Babel. Frontend is Jinja, JQuery and duct tape. 

## Setup
After pulling down the source code, run
    bin/configure_database.sh <root mysql pw>

This will set up the necessary user and database, and pull in the latest dump.

If running this site under apache, the wsgi module is required.
    apt-get install libapache2-mod-wsgi

It should become enabled automatically after installation. If not
    a2enmod wsgi

## service

Set this up as a systemd service with the following config.

```
# cat /etc/systemd/system/intagnewspaper.service
Unit]
Description=uWSGI instance to serve intagnewspaper.org 
After=network.target

[Service]
User=<username>
Group=<username>
WorkingDirectory=/home/<username>/xmunoz/intagnewspaper
ExecStart=/home/<username>/xmunoz/intagnewspaper/bin/runserver

[Install]
WantedBy=multi-user.target
```

Then start it.
```
service intagnewspaper start
```

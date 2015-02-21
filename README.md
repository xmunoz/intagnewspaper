intagnewspaper
==============

The styling and rendering for [intagnewspaper.org](http://intagnewspaper.org), and Ecuadorean news publication based in the Intag Cloud Forest. Backend is Flask, MySQL, and Babel. Frontend is Jinja, JQuery and duct tape. 

## Setup
After pulling down the source code, run
    bin/configure_database.sh <root mysql pw>

This will set up the necessary user and database, and pull in the latest dump.

If running this site under apache, the wsgi module is required.
    apt-get install libapache2-mod-wsgi

It should become enabled automatically after installation. If not
    a2enmod wsgi

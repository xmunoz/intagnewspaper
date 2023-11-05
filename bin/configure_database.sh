#!/bin/sh

genpwd() {
      	tr -dc A-Za-z0-9_ < /dev/urandom | head -c 16 | xargs
}

userpass=$(genpwd)
username="intag"
dbname="intagdb"
mysql -u root -e "CREATE DATABASE IF NOT EXISTS $dbname"
mysql -u root -e "CREATE USER '$username'@'localhost' IDENTIFIED BY '$userpass';"
mysql -u root -e "GRANT ALL PRIVILEGES ON $dbname.* TO '$username'@'localhost';"

root_dir="${PWD%/bin}"
conf_file="$root_dir/.my.cnf"
cat <<EOF >$conf_file
[client]
password="$userpass"

[mysql]
no-auto-rehash
connect_timeout=2

[mysqlhotcopy]
interactive-timeout
EOF

dump_file="$root_dir/dumps/19042023_dump.sql"
mysql -u $username -p$userpass $dbname < $dump_file

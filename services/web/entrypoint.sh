#!/bin/sh

if [ "$DATABASE" = "mysql" ]
then
    echo "Waiting for mysql..."

#    while ! nc -z $SQL_HOST $SQL_PORT; do
#        sleep 0.1
#   done

    echo "Mysql started"
fi

#python manage.py create_db 
exec "$@"
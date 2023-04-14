#!/bin/bash

export DB_USER=$DB_USER
export DB_PASSWORD=$DB_PASSWORD
export DB_HOST=$DB_HOST
export DB_NAME=$DB_NAME
export FULLNAME=$FULLNAME
export USERNAME=$USERNAME
export EMAIL=$EMAIL
export PASSWORD=$PASSWORD

python3 /pinepods/startup/setupdatabase.py
python3 /pinepods/create_user.py $DB_USER $DB_PASSWORD $DB_HOST $DB_NAME $FULLNAME $USERNAME $EMAIL $PASSWORD

python3 /pinepods/pypods.py
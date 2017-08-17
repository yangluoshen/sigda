#!/bin/bash
set -e
umask 022

#chmod a+x /etc/run/init_db.sh

#/etc/run/init_db.sh

cd ${PROJECT_ROOT}
ls ./
python sigda/flaskapp.py


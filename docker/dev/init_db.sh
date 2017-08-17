#!/usr/bin/env bash
cd ${PROJECT_ROOT}
pwd
ls

# db

python hamster/manage.py db init
python hamster/manage.py db migrate -m "auto "
python hamster/manage.py db upgrade heads
while [ $? -ne 0 ]
do
    sleep 10
    python hamster/manage.py db upgrade heads
done

# celery
echo "celery -A------------------"

if [ -f 'celerybeat.pid' ]; then
    rm  'celerybeat.pid'
fi

if [ -f 'celerybeat_schedule' ]; then
    rm  'celerybeat_schedule'
fi


celery beat -A hamster.celeryapp.tasks -l debug &
celery -A hamster.celeryapp.tasks worker -l debug &

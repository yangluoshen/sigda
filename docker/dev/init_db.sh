#!/usr/bin/env bash
cd ${PROJECT_ROOT}
pwd
ls

# db

python sigda/manage.py db init
python sigda/manage.py db migrate -m "auto "
python sigda/manage.py db upgrade heads
while [ $? -ne 0 ]
do
    sleep 10
    python sigda/manage.py db upgrade heads
done

:<<'
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

'

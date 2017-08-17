FROM python:3.6
ADD . /config
WORKDIR /code

RUN pip install --trusted-host pypi.douban.com   -i http://pypi.douban.com/simple -r /config/requirements.txt

ENV TZ=Asia/Shanghai
RUN cp /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

CMD ["/etc/run/start_web.sh"]

# SIGnificant DAys

组队庆祝某一特别的日子，某一激动的时刻。

举个例子。Allen是Fizz暗恋很久的高中同学。Allen的生日快到了，Fizz想在Allen生日那天给她一个惊喜。由于已毕业多年，很难再将高中同学聚在一起。于是，Fizz使用SIGDA精心制作了一个精美的网页，并邀请许多高中同学在该网站上献上祝福。Allen生日那天，Fizz将SIGDA网页送给Allen，Allen十分感动，情急之下冲动地答应了Fizz的表白。

SIGDA的定位是创建一个临时的空间，在某些特殊日子给某人或者某些人surprise。

这只是一个用来学习flask的练手项目。

## Startup

    
    cd docker/
    docker-compose up
    
    visit http://0.0.0.0:5757/index


## Roadmap

* 通知功能。使用者可提前录入未来significant days, SIGDA会在那些日子到来之前提醒使用者。
* 评论功能。参与者可在网页上进行评论（祝福）。
* 前端。


## Module

* Comment
* Notifier. 通知可用celery 实现。

## Skill

* flask, docker, celery, sqlalchemy, mysql, redis, etc.



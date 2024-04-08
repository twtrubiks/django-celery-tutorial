# django-celery-tutorial

 Django-celery-tutorial 基本教學 - 從無到有 Django-celery-tutorial 📝

 今天要教大家使用 [Django](https://github.com/django/django) 結合 [Celery](https://docs.celeryq.dev/en/latest/index.html) :smile:

* [Youtube Tutorial - part1](https://youtu.be/9nrtD9cg_Qo)

* [Youtube Tutorial - part2](https://youtu.be/62IqfN6OTyM)

建議對 [Django](https://github.com/django/django) 不熟悉的朋友，可以先觀看我之前寫的文章（ 進入 [Django](https://github.com/django/django)  的世界）

* [Django 基本教學 - 從無到有 Django-Beginners-Guide](https://github.com/twtrubiks/django-tutorial)

* [使用 Django 實現一個可以使用社交平台登入並且註冊的網站](https://github.com/twtrubiks/django_social_login_tutorial)

* [使用 Django 建立一個簡易版購物網站](https://github.com/twtrubiks/django-shop-tutorial)

## 前言

先來介紹一個名詞，訊息佇列（消息對列 ），英文為 Message Queue（ MQ ），

來看看 [wiki](https://zh.wikipedia.org/wiki/%E6%B6%88%E6%81%AF%E9%98%9F%E5%88%97) 上面的說明，是一種行程間通訊或同一行程的不同執行緒間的通訊方式，

軟體的貯列用來處理一系列的輸入，通常是來自使用者。訊息佇列本身是**異步的**，它

允許接收者在訊息傳送很長時間後再取回訊息，這和大多數通訊協定是不同的。

訊息佇列有很多開源的實現，像是本篇就會介紹到 [RabbitMQ](https://www.rabbitmq.com/)。

## 可以從這篇文章學到什麼

* [Django](https://github.com/django/django) 如何結合 [Celery](http://celery.readthedocs.io/en/latest/index.html) 使用

* 了解 [Celery](http://celery.readthedocs.io/en/latest/index.html) 的使用，以及為什麼要使用 [Celery](http://celery.readthedocs.io/en/latest/index.html) :sunglasses:

## 安裝套件

請在 cmd ( 命令提示字元 ) 輸入以下指令

```python
pip install -r requirements.txt
```

## Celery

***Celery is a simple, flexible, and reliable distributed system to process vast amounts of messages, while providing operations with the tools required to maintain such a system.
It's a task queue with focus on real-time processing, while also supporting task scheduling.***

**為什麼我們要用 Celery ？ Celery 該使用在什麼情境下呢？**

千萬不要讓使用者在你的網站等很久 :scream:  以下舉幾個情境，

**情境一：**

當一個影片需要轉檔時，你是該讓這影片在後台轉檔，然後這段時間，

使用者可以去操作網頁上的其他東西，還是說你要讓他在轉檔的那個

畫面一直等，等到轉檔結束，才能開始做其他事情 ？

範例可參考另一個 [docker-django-celery-tutorial](https://github.com/twtrubiks/docker-django-celery-tutorial) 教學。

**情境二：**

當我們需要寄送 e-mail 時，我們是該讓寄信這個工作在背景處理，使用

者這段時間可以繼續操作網頁，還是說我們要讓使用者等到信件寄出後

，才可以開始做其他事情呢？

寄送 e-mail 時，會有遇到 SMTP 連接很慢或是失敗的可能，這時候就有

可能會讓使用者等，你覺得使用者願意讓你等幾秒 :rage:

**情境三：**

有時候我們需要大量的推播，你覺得當你推播的時候，使用者完全不能

執行網站的東西他們能接受嗎？

以上這三種情境，就非常適合使用 Celery 解決這些問題 :smiley:

將這些事情將給 Celery 執行，使用者就可以繼續操作網頁不受影響。

如果你有其他的使用情境分享，歡迎提供，大家一起學習 :laughing:

### Broker Tutorial

***Celery requires a solution to send and receive messages; usually this comes in the form of a separate service called a message broker.***

以下將介紹 Broker ，建議使用 [RabbitMQ](https://www.rabbitmq.com/)（ 官方推薦 ），本篇教學

也會使用 [RabbitMQ](https://www.rabbitmq.com/) 來介紹，其他的 Broker 使用就留給大家去研究  :stuck_out_tongue_winking_eye:

什麼是 Broker :question: 可以把它想成是中間人，相信這樣好懂很多 :grin:

再說明一下為什麼需要 Broker，原因是因為 Celery 沒有 Message Queue 的功能，所以需要

Broker（ 像是 [RabbitMQ](https://www.rabbitmq.com/) ）來完成他。

#### RabbitMQ

[RabbitMQ](https://www.rabbitmq.com/) is feature-complete, stable, durable and easy to install. It's an excellent choice for a production environment.

##### Installing RabbitMQ

**Docker** 執行以下指令

```cmd
docker-compose up -d
```

**Linux** 執行以下指令

```cmd
sudo apt-get install rabbitmg
```

由於我自己沒嘗試過，如果你有嘗試並且安裝成功，歡迎分享 :heart_eyes:

**macOS** 執行以下指令

```cmd
brew install rabbitmq
```

接下來我們到安裝的路徑

```cmd
cd /usr/local/sbin
```

Start RabbitMQ

```cmd
./rabbitmq-server
```

如果順利啟動，你應該會看到如下資訊

```cmd
             RabbitMQ 3.6.9. Copyright (C) 2007-2016 Pivotal Software, Inc.
  ##  ##      Licensed under the MPL.  See https://www.rabbitmq.com/
  ##  ##
  ##########  Logs: /usr/local/var/log/rabbitmq/rabbit@localhost.log
  ######  ##        /usr/local/var/log/rabbitmq/rabbit@localhost-sasl.log
  ##########
              Starting broker...
 completed with 10 plugins.
```

Stop RabbitMQ

```cmd
./rabbitmqctl stop
```

也可以到這邊看更詳細的教學
[https://www.rabbitmq.com/install-standalone-mac.html](https://www.rabbitmq.com/install-standalone-mac.html)

**Windows** 需下載兩個東西

請先去下載 [Erlang](http://www.erlang.org/downloads)  ( 請注意自己電腦的位元數 )

先著再去下載 RabbitMQ

[https://www.rabbitmq.com/install-windows.html](https://www.rabbitmq.com/install-windows.html)

基本上，都是無腦 ( 一直下一步 ) 安裝，應該不會有什麼問題~

也可以直接安裝 RabbitMQ，他會提醒你去安裝  [Erlang](http://www.erlang.org/downloads) ( 假如你沒安裝的話 )

在 Windows 上啟動 RabbitMQ，直接打開 RabbitMQ Service - start 即可

![alt tag](http://i.imgur.com/4IfxP6q.png)

啟動 RabbitMQ

![alt tag](http://i.imgur.com/CMDrnOe.png)

#### Redis

Redis is also feature-complete, but is more susceptible to data loss in the event of abrupt termination or power failures.

#### Other brokers

也有其他的選擇，請參考 [Broker Overview](http://celery.readthedocs.io/en/latest/getting-started/brokers/index.html#broker-overview)

### Celery Tutorial

Install Celery

```cmd
pip install celery
```

### Setting Celery

先建立一個 [celery.py](https://github.com/twtrubiks/django-celery-tutorial/blob/master/django_celery_tutorial/celery.py)，路徑如下，

django_celery_tutorial/django_celery_tutorial/[celery.py](https://github.com/twtrubiks/django-celery-tutorial/blob/master/django_celery_tutorial/celery.py)

```python
import os
from celery import Celery
# from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_tutorial.settings')

app = Celery(
    'django_celery_tutorial',
    # broker='amqp://celery:password123@rabbitmq:5672/my_vhost',
    broker='amqp://celery:password123@0.0.0.0:5672/my_vhost',
)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
```

接著我們再修改 [`__init__.py`](https://github.com/twtrubiks/django-celery-tutorial/blob/master/django_celery_tutorial/__init__.py)，路徑如下

django_celery_tutorial/django_celery_tutorial/[`__init__.py`](https://github.com/twtrubiks/django-celery-tutorial/blob/master/django_celery_tutorial/__init__.py)

```python
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ['celery_app']
```

再建立一個 [tasks.py](https://github.com/twtrubiks/django-celery-tutorial/blob/master/tutorial/tasks.py)，路徑如下

django_celery_tutorial/tutorial/[tasks.py](https://github.com/twtrubiks/django-celery-tutorial/blob/master/tutorial/tasks.py)

```python
from celery import shared_task
from django.core.mail import send_mail


@shared_task(ignore_result=True)
def task_mail():
    subject = "celery subject test"
    message = "celery message test"
    recipient = ["xxxxxx@gmail.com", "xxxxxx@gmail.com", "xxxxxx@yahoo.com.tw"]
    send_mail(
        subject,
        message,
        "admin@celery_test.com",
        recipient,
    )
```

[Django](https://www.djangoproject.com/) 寄送信箱的方法可以參考我之前寫的 [使用 Django 發送信件](https://github.com/twtrubiks/django_social_login_tutorial#%E4%BD%BF%E7%94%A8-django--%E7%99%BC%E9%80%81%E4%BF%A1%E4%BB%B6)

最後，在 [views.py](https://github.com/twtrubiks/django-celery-tutorial/blob/master/tutorial/views.py) 中直接呼叫即可

django_celery_tutorial/tutorial/[views.py](https://github.com/twtrubiks/django-celery-tutorial/blob/master/tutorial/views.py)

```python
from django.core.mail import send_mail
from django.shortcuts import render

from tutorial.tasks import task_mail

def task_use_celery(request):
    task_mail.delay()
    return render(request, "tutorial/process_done.html")
```

## 執行畫面

![alt tag](http://i.imgur.com/Vk7mQTN.png)

當信件寄出時，會到下一個畫面。

![alt tag](http://i.imgur.com/U1kSwvs.png)

畫面很簡單，基本上就是使用寄送 e-mail 來看有使用和沒使用 Celery 的差異 :smiley:

***啟動  Worker 時，記得 Broker要先啟動，也就是要先 Start RabbitMQ，然後再啟動 Celery Worker***

第一步，請先確認 RabbitMQ 已經啟動，接著我們再啟動 celery worker，

請再開啟一個 shell，使用以下指令啟動 celery worker

Run the Celery worker server

```cmd
celery -A proj worker -l info
```

proj 也就是你的名稱，我們在 [celery.py](https://github.com/twtrubiks/django-celery-tutorial/blob/master/django_celery_tutorial/celery.py) 設定為 django_celery_tutorial，所以

我們需要修改為

```cmd
celery -A django_celery_tutorial worker -l info
```

這邊注意:exclamation::exclamation: 如果你的 `task.py` 有修改任何 code,

記得你的 worker (上面這行指令) 也要重啟, 不然會一直讀到舊的:anguished:

![alt tag](http://i.imgur.com/hOeGFuU.png)

![alt tag](http://i.imgur.com/QUEmyFE.png)

請再開啟一個 shell,

```cmd
python3 manage.py shell
```

```python
from tutorial.tasks import *
task_mail.delay()
```

執行後, 你會發現 celery 的 terminal 會顯示一些資訊,

celery 有非常多 [Signals](https://docs.celeryq.dev/en/stable/userguide/signals.html#signals) 可以使用,

```python

@signals.task_prerun.connect
def prerun_task_mail(task_id, task, *args, **kwargs):
    print(f"task_id: {task_id},  task: {task}")
    print("prerun_task_mail ......")

@signals.task_postrun.connect
def postrun_task_mail(task_id, task, *args, **kwargs):
    print(f"task_id: {task_id},  task: {task}")
    print("postrun_task_mail ......")

@signals.task_success.connect
def success_task_mail(sender=None, **kwargs):
    print(sender)
    print("success_task_mail ......")

@signals.task_failure.connect
def failure_task_mail(task_id, exception, *args, **kwargs):
    print(f"task_id: {task_id},  exception: {exception}")
    print("failure_task_mail ......")
```

```cmd
# 這個代表執行任務前 會預先執行的 任務
[2023-10-14 10:23:53,434: WARNING/ForkPoolWorker-8] prerun_task_mail ......

# 也可以定義, 任務成功或失敗所需要執行的任務
[2023-10-14 10:23:53,435: WARNING/ForkPoolWorker-8] success_task_mail ......

# 這個代表執行任務後 會執行的 任務
[2023-10-14 10:23:53,435: WARNING/ForkPoolWorker-8] postrun_task_mail ......
```

celery 也有 retry 機制

```python
from tutorial.tasks import *
task_mail_retry().delay()
```

程式碼如下,

注意要使用 `bind=True`, 可參考[bound-tasks](https://docs.celeryq.dev/en/latest/userguide/tasks.html#bound-tasks),

尤其是使用 `self.retry(...)`

```python
@shared_task(ignore_result=True, bind=True)
def task_mail_retry(self):
    try:
        if 1:
            raise Exception()

        subject = "celery subject test"
        message = "celery message test"
        recipient = ["xxxxxx@gmail.com", "xxxxxx@gmail.com", "xxxxxx@yahoo.com.tw"]
        send_mail(
            subject,
            message,
            "admin@celery_test.com",
            recipient,
        )

    except Exception as e:
        raise self.retry(exc=e, countdown=3)
```

你會發現他自己會自行 retry, 文件可參考 [Retrying](https://docs.celeryq.dev/en/stable/userguide/tasks.html#retrying)

預設 retry 3次, 如果還是失敗, 就跳出 Exception

```cmd
[2023-10-14 10:32:17,125: INFO/ForkPoolWorker-8] Task tutorial.tasks.task_mail_retry[2efde179-34f5-4493-aea4-985b8d87e10f] retry: Retry in 3s: Exception()
[2023-10-14 10:32:20,126: WARNING/ForkPoolWorker-8] prerun_task_mail ......
[2023-10-14 10:32:20,127: INFO/ForkPoolWorker-8] Task tutorial.tasks.task_mail_retry[2efde179-34f5-4493-aea4-985b8d87e10f] retry: Retry in 3s: Exception()

[2023-10-14 10:32:26,131: WARNING/ForkPoolWorker-8] failure_task_mail ......
[2023-10-14 10:32:26,131: ERROR/ForkPoolWorker-8] Task tutorial.tasks.task_mail_retry[2efde179-34f5-4493-aea4-985b8d87e10f] raised unexpected: Exception()
```

## Celery Useful settings

可參考 [Useful settings](https://cheat.readthedocs.io/en/latest/django/celery.html#useful-settings)

在 [settings.py](https://github.com/twtrubiks/django-celery-tutorial/blob/master/django_celery_tutorial/settings.py) 底下的最後

```python
......

# celery
# CELERY_TASK_ALWAYS_EAGER=1  # 可以中斷點 -> flower 看不到
CELERY_TASK_ALWAYS_EAGER=0  # 不可以中斷點 -> flower 看的到
```

這個 `CELERY_TASK_ALWAYS_EAGER` 非常實用,

簡單說, 如果你想要 debug celery 裡面的東西, 用這個就對了,

預設是 0, 也就是都會交給 celery 執行,

你會沒辦法在 celery 底下下中斷點 (Flower 會有任務排成的紀錄),

假如你設定成 1, 你會發現你可以在 celery 底下下中斷點了,

但相反的, Flower 中就不會有任務排成的紀錄, 因為都被 local block 了.

官方文件說明如下

```text
CELERY_TASK_ALWAYS_EAGER: If this is True, all tasks will be executed locally by blocking until the task returns. apply_async() and Task.delay() will return an EagerResult instance, which emulates the API and behavior of AsyncResult, except the result is already evaluated.

That is, tasks will be executed locally instead of being sent to the queue.

This is useful mainly when running tests, or running locally without Celery workers.
```

## 監控 Celery

***Flower is a web based tool for monitoring and administrating Celery clusters***

[https://flower.readthedocs.io/en/latest/](https://flower.readthedocs.io/en/latest/)

```cmd
pip install flower
```

launch from Celery

```cmd
celery -A proj flower -l info
```

proj 也就是你的名稱，我們也可以直接使用下方指令啟動 flower

```cmd
celery -A django_celery_tutorial flower -l info
```

如果想要保存 flower 的資料,

```cmd
celery -A django_celery_tutorial flower --persistent=True -l info
```

預設會在路徑下多個 `flower` 檔案,

可參考官網參數說明 [https://flower.readthedocs.io/en/latest/config.html](https://flower.readthedocs.io/en/latest/config.html)

如果你想要基本的 auth, 可以使用如下指令

```cmd
celery -A django_celery_tutorial flower -l info --basic_auth=twtrubiks:password123
```

詳細可參考 [https://flower.readthedocs.io/en/latest/auth.html#http-basic-authentication](https://flower.readthedocs.io/en/latest/auth.html#http-basic-authentication)

[http://localhost:5555](http://localhost:5555)

![alt tag](http://i.imgur.com/iADQnPV.png)

[http://localhost:5555/tasks](http://localhost:5555/tasks)

![alt tag](http://i.imgur.com/rSbK6ZF.png)

更多說明可參考官網

[https://flower.readthedocs.io/en/latest/](https://flower.readthedocs.io/en/latest/)

## 後記

這次是帶大家在自己的電腦上安裝環境，有時候的確會遇到環境上的問題 ( 很麻煩 :unamused: ) ，

所以這邊蠻推薦大家使用 docker 安裝，我有再寫一篇使用 docker 安裝 celery 的教學，有興趣

的朋友可以前往 [docker-django-celery-tutorial](https://github.com/twtrubiks/docker-django-celery-tutorial) 閱讀 :smiley:

## 執行環境

* Python 3.9

## Reference

* [Django](https://www.djangoproject.com/)
* [Celery](https://docs.celeryq.dev/en/stable/)
* [Flower](https://flower.readthedocs.io/en/latest/)
* [Using Celery with Django](http://celery.readthedocs.io/en/latest/django/first-steps-with-django.html#first-steps-with-django)

## Donation

文章都是我自己研究內化後原創，如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## License

MIT licens

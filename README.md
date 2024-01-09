# Django_Celery_Redis
Simple demo, how to integrate Django with celery and use Redis as message broker to distribute background tasks

## Workflow 
Django app send tasks -> Message Broker (Redis, RabbitMQ, AWS SQS) -> Celery get task from message broker and execute it

For more details information, read [this article](https://realpython.com/asynchronous-tasks-with-django-and-celery/)    

In this project:
- Use Redis as message broker
- Run Django app and Celery worker on single machine, but you can run django app and celery worker on different machine(1 machine run django runserver command, in another machine run celery command) 
## Setup
1. Clone project
2. Setting Redis server on the cloud using [Rail.app](https://www.youtube.com/watch?v=5S6-uok5E7g)  
   ``` bash
   # replace app/settings.py CELERY_BROKER_URL and CELERY_RESULT_BACKEND with remote redis server url
   Redis url = "redis://<REDIS_USER>:<REDIS_PASSWORD>@<redis_url>:<port>"
   ```
3. Run command
    ```bash
   # create python env
   python -m venv venv
   
   # activate env 
   .\venv\Scripts\activate # for Windows
    source ./venv/bin/activate # for Linux
   
   # install necessary packages
    pip install -r requirements.txt
   
   # run django
   python manage.py runserver
   
   # open another cmd tab, run celery worker by command
   celery worker -A app -l info # Linux
   celery worker -A app -l info -P gevent # Window
   # can run concurrent task by adding option -c <number_threads>
    ```
   **Note**:
   - In terminal run django `python manage.py runserver` -> only show log web server   
   - Log background tasks executed by Celery workers show in the terminal which run `celery worker` command

## User data for deploy EC2 AWS
```
sudo yum install git python-pip
cd Django_Celery_Redis
pip install -r requirements.txt
```
## Reference

[1.Asynchronous Tasks With Django and Celery - Real Python](https://realpython.com/asynchronous-tasks-with-django-and-celery/)  
[2.Integrating Celery in Django - YouTube](https://www.youtube.com/watch?v=5S6-uok5E7g)  
[3. Scale Django + celery](https://stackoverflow.com/questions/24329952/django-celery-on-amazon-aws-using-separate-ec2-instances-as-workers)   
[4. Scale Django + Celery run background task with AWS SQS - Medium](https://betterprogramming.pub/design-an-auto-scalable-architecture-for-your-django-apps-in-aws-850ca5ec63a1)  
[5. Celery worker](https://ankurdhuriya.medium.com/understanding-celery-workers-concurrency-prefetching-and-heartbeats-85707f28c506#:~:text=By%20default%2C%20Celery%20workers%20use,processes%2C%20and%20eventlet%2Fgreenlet.)

from locust import TaskSet, HttpUser
from behaviors.register_behaviors import RegisterBehavior


class UserBehavior(TaskSet):
    tasks = {RegisterBehavior: 1}


class WebsiteUser(HttpUser):
    host = "http://127.0.0.1:8000"
    tasks = [UserBehavior]

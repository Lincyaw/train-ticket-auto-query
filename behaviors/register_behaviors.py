import requests
from locust import task, HttpUser
from service.auth_service import (create_default_user, DtoCreateUser,
                                  get_users, users_login, DtoLoginUser)
from faker import Faker

fake = Faker()


class RegisterBehavior(HttpUser):
    client: requests.Session

    def on_start(self) -> None:
        admin_dto = DtoLoginUser(username='admin',
                                 password='222222', verificationCode="1234")
        login_result = users_login(self.client, admin_dto, {
            'Proxy-Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
            'Content-Type': 'application/json',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
        }, self.host)
        print(login_result)
        self.client.headers.update(
            {"Authorization": f"Bearer {login_result}"}
        )

    @task(2)
    def register_and_query(self):
        """
        先注册，然后查询用户
        """
        auth_dto = DtoCreateUser(userId=fake.uuid4(),
                                 userName=fake.user_name(),
                                 password=fake.password())
        create_default_user(self.client, auth_dto, self.host)
        get_users(self.client, self.host)

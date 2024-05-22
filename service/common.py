import requests
from collections import defaultdict
import random
from config import BASE_URL
from dataclasses import fields, dataclass
from typing import Type, Any, TypeVar, Dict

T = TypeVar('T', bound='DataclassInstance')


@dataclass
class DataclassInstance:
    pass


def from_dict(data_class: Type[T], data: Dict[str, Any]) -> T:
    """
    将字典转换为 dataclass 实例的递归函数。
    """
    if not is_dataclass(data_class):
        raise ValueError(f"{data_class} is not a dataclass type")

    fieldtypes = {f.name: f.type for f in fields(data_class)}
    init_values = {}
    for field in fields(data_class):
        field_name = field.name
        field_type = field.type
        if field_name in data:
            if is_dataclass(field_type):
                init_values[field_name] = from_dict(field_type,
                                                    data[field_name])
            else:
                init_values[field_name] = data[field_name]
    return data_class(**init_values)


def is_dataclass(cls):
    """
    检查给定的类是否是 dataclass。
    """
    return hasattr(cls, '__dataclass_fields__')


class HttpClient:
    def __init__(self, max_samples=3, admin=False):
        self.session = requests.Session()  # 创建 Session 对象
        self.stats = defaultdict(lambda: {
            'total': 0,
            'success': 0,
            'response_samples': [],
            'error_samples': []
        })  # 请求统计信息
        self.admin = admin
        self.max_samples = max_samples  # 最大样本数
        self.__auth()

    def request(self, url, method='GET', params=None, data=None, json=None,
                headers=None, timeout=10, **kwargs):
        """
        通用的 HTTP 请求方法

        :param url: 请求的 URL
        :param method: 请求方法，默认为 'GET'
        :param params: 请求的查询参数，字典类型 xxx?query=xxx&username=xxx
        :param data: 请求的数据，字典类型； 表单
        :param json: 请求的 JSON 数据，字典类型； 同时有 json 和 data，则 json 优先级更高
        :param headers: 请求头，字典类型
        :param timeout: 请求超时时间，默认为 10 秒
        :param kwargs: 其他请求参数，如 auth、cookies 等
        :return: 响应对象
        """
        try:
            if headers == {}:
                headers = None
            response = self.session.request(method, url, params=params,
                                            data=data,
                                            json=json, headers=headers,
                                            timeout=timeout, **kwargs)
            response.raise_for_status()  # 如果响应状态码不是 200，则抛出异常
            self.stats[url]['success'] += 1  # 请求成功计数加 1
            self._add_sample(url, 'response_samples', response)  # 添加响应样本
            return response
        except requests.exceptions.RequestException as e:
            error_sample = {
                'exception': str(e),
                'request': {
                    'method': method,
                    'url': url,
                    'params': params,
                    'data': data,
                    'json': json,
                    'headers': headers,
                    'timeout': timeout,
                    'kwargs': kwargs
                }
            }
            self._add_sample(url, 'error_samples', error_sample)  # 添加错误样本
            print(f"请求出错：{e}")
            return None
        finally:
            self.stats[url]['total'] += 1  # 总请求次数加 1

    def _add_sample(self, url, sample_type, sample):
        """
        添加样本到统计信息中

        :param url: 请求的 URL
        :param sample_type: 样本类型，可以是 'response_samples' 或 'error_samples'
        :param sample: 样本内容
        """
        samples = self.stats[url][sample_type]
        if len(samples) < self.max_samples:
            samples.append(sample)
        else:
            # 随机替换已有样本
            index = random.randint(0, self.max_samples - 1)
            samples[index] = sample

    def get_stats(self):
        """
        获取请求统计信息

        :return: 请求统计信息，字典类型
        """
        stats = {}
        for url, data in self.stats.items():
            total = data['total']
            success = data['success']
            success_rate = success / total if total > 0 else 0
            stats[url] = {
                'total': total,
                'success_rate': success_rate,
                'response_samples': data['response_samples'],
                'error_samples': data['error_samples']
            }
        return stats

    def reset_stats(self):
        """
        重置请求统计信息
        """
        self.stats.clear()

    def __auth(self):
        self.session.headers.update({
            'Proxy-Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
            'Content-Type': 'application/json',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
        })
        if self.admin:
            basic_auth_dto = {'username': 'admin',
                              'password': '222222',
                              "verificationCode": "1234"}
        else:
            basic_auth_dto = {'username': 'fdse_microservice', 'password':
                '111111',
                              "verificationCode": "1234"}
        headers = {'Content-Type': 'application/json'}

        verify_url = BASE_URL + '/api/v1/verifycode/generate'
        r = self.session.get(url=verify_url)

        url = "/api/v1/users/login"
        response = self.session.request(method="POST", url=BASE_URL + url,
                                        json=basic_auth_dto,
                                        headers=headers)
        self.session.headers.update(
            {"Authorization": f"Bearer {response.json()['data']['token']}"}
        )
        print(response)

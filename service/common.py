
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


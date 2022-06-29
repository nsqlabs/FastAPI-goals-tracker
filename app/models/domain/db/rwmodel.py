
from datetime import datetime as DateTime, timezone

from pydantic import BaseConfig, BaseModel


def convert_datetime_to_realworld(dt: DateTime) -> str:
    return dt.replace(tzinfo=timezone.utc).isoformat().replace("+00:00", "Z")


def convert_field_to_camel_case(string: str) -> str:
    return "".join(
        word if index == 0 else word.capitalize()
        for index, word in enumerate(string.split("_"))
    )


class RWModel(BaseModel):
    class Config(BaseConfig):
        allow_population_by_field_name = True
        json_encoders = {DateTime: convert_datetime_to_realworld}
        alias_generator = convert_field_to_camel_case

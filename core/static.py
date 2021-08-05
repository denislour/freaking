import re
from collections.abc import Mapping
from yaml import load, FullLoader


class Static(Mapping):
    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    def __init__(self, metadata, content: str):
        self.data = metadata
        self.data["content"] = content

    @classmethod
    def generate(cls, raw_content):
        fm, content = cls.__regex.split(raw_content, 2)
        metadata = load(fm, Loader=FullLoader)
        return cls(metadata, content)

    @property
    def body(self) -> str:
        return self.data["content"]

    @property
    def type(self):
        return self.data["type"] if "type" in self.data else None

    @type.setter
    def type(self, type) -> None:
        self.data["type"] = type

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self) -> None:
        self.data.__iter__()

    def __len__(self) -> int:
        return len(self.data)

    def __repr__(self) -> str:
        data = dict()
        for key, value in self.data.items():
            if key != "content":
                data[key] = value
        return str(data)

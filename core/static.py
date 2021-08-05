import re
from collections.abc import Mapping
from yaml import load, FullLoader


class Static(Mapping):
    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    @staticmethod
    def generate(cls, raw_content: str):
        _, fm, content = cls.__regex.split(raw_content, 2)
        metadata = load(fm, Loader=FullLoader)
        return cls(metadata, content)

    def __init__(self, metadata, content):
        self.data = metadata
        self.data["content"] = content

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        return self.data["type"] if "type" in self.data else None

    @type.setter
    def type(self, type):
        self.dat["type"] = type

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        self.data.__iter__()

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        data = dict()
        for key, value in self.data.items():
            if key != "content":
                data[key] = value
        return str(data)

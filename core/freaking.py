from pathlib import Path
from typing import List
from core.parser import ResourceParser


class Freaking:
    def __init__(self, source: str, dest: str, parsers: List[ResourceParser]):
        """Constructure for core instance"""
        self.source = Path(source)
        self.dest = Path(dest)
        self.parsers = parsers

    def create_dir(self, path: Path):
        """Create directory from path"""
        dir = self.dest / path.relative_to(self.source)
        dir.mkdir(parents=True, exist_ok=True)

    def load_parser(self, extension: str):
        for parser in self.parsers:
            if parser.valid_extensions(extension):
                return parser

    def run_parser(self, path: Path):
        parser = self.load_parser(path.suffix)
        if parser:
            parser.parse(path, self.source, self.dest)
        else:
            print("Not Implemented")

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
            elif path.is_file():
                self.run_parser(path)

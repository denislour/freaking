import sys

from pathlib import Path
from typing import List
from core.parser import MarkdownParser


class Freaking:
    def __init__(self, source: str, dest: str, parsers: List[MarkdownParser]):
        """Constructure for core instance"""
        self.source = Path(source)
        self.dest = Path(dest)
        self.parsers = parsers

    @staticmethod
    def error(msg) -> None:
        sys.stderr.write("\x1b[1;31m{}\n".format(msg))

    def create_dir(self, path: Path) -> None:
        """Create directory from path"""
        dir = self.dest / path.relative_to(self.source)
        dir.mkdir(parents=True, exist_ok=True)

    def load_parser(self, extension: str) -> MarkdownParser:
        for parser in self.parsers:
            if parser.valid_extensions(extension):
                return parser

    def run_parser(self, path: Path) -> None:
        parser = self.load_parser(path.suffix)
        if parser:
            parser.parse(path, self.dest)
        else:
            self.error(
                "No parser for the {} file, "
                "Not allow {} extension!".format(path.name, path.suffix)
            )

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
            elif path.is_file():
                self.run_parser(path)

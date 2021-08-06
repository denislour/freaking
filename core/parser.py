import shutil
import sys

from typing import List
from pathlib import Path
from markdown import markdown

from core.static import Static


class Parser:
    extensions: List[str] = list()

    def valid_extensions(self, extension: str) -> bool:
        return extension in self.extensions

    def parse(self, path: Path, dest: Path) -> None:
        raise NotImplementedError

    def read(self, path: Path) -> str:
        with open(path, "r") as file:
            return file.read()

    def write(self, path: Path, dest: Path, content: str, ext=".html") -> None:
        full_path = dest / path.with_suffix(ext).name
        with open(full_path, "w") as file:
            file.write(content)

    def copy(self, path: Path, source: Path, dest: Path) -> None:
        shutil.copy(path, dest / path.relative_to(source))


class MarkdownParser(Parser):
    extensions = [".md", ".markdown"]

    def parse(self, path: Path, dest: Path) -> None:
        try:
            content = Static.generate(self.read(path))
        except ValueError:
            sys.stderr.write(
                "Cannot parse markdown content {}!".format(path.name))
            return None
        html_content = markdown(content.body)
        self.write(path, dest, html_content)
        sys.stdout.write(
             "\x1b[1;32m{} converted to HTML. "
             "Metadata: {}\n".format(path.name, content)
         )

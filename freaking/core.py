from pathlib import Path


class Freaking:
    def __init__(self, source: str, dest: str):
        """Constructure for core instance"""
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path: Path):
        """Create directory from path"""
        dir = self.dest / path.relative_to(self.source)
        dir.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)

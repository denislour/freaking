import typer
from core.freaking import Freaking
from core.parser import ResourceParser


def main(source: str = "content", dest: str = "dest"):
    config: dict = {
        "source": source,
        "dest": dest,
        "parsers": [ResourceParser()],
    }
    Freaking(**config).build()


if __name__ == "__main__":
    typer.run(main)

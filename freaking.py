import typer
from freaking.core import Freaking
from freaking.parser import ResourceParser


def main(source: str = "content", dest: str = "dest"):
    config: dict = {
        "source": source,
        "dest": dest,
        "parsers": list(ResourceParser()),
    }
    Freaking(**config).build()


if __name__ == "__main__":
    typer.run(main)

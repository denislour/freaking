import typer
from freaking.core import Freaking


def main(source: str = "content", dest: str = "dest"):
    config: dict = {"source": source, "dest": dest}
    Freaking(**config).build()


if __name__ == "__main__":
    typer.run(main)

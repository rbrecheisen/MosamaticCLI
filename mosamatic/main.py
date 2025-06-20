import click

from mosamatic.tasks import (
    decompress,
    selectl3,
)


@click.group()
def cli():
    pass


cli.add_command(decompress.decompress)
cli.add_command(selectl3.selectl3)
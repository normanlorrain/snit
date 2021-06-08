import click
from . import archive


@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    click.echo(f"Debug mode is {'on' if debug else 'off'}")


@cli.command()  # @cli, not @click!
def backup():
    click.echo("backup")
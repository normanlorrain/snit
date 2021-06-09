import click
from . import archive


@click.group()
#@click.option('--debug/--no-debug', default=False)
@click.option('--path', envvar='SNIT_DIR',  )
def cli(path):
    #click.echo(f"Debug mode is {'on' if debug else 'off'}")
    click.echo(f"SNIT directory is set to {path}")
    archive.snit_dir = path


@cli.command()  # @cli, not @click!
def backup():
    click.echo("backup")
    archive.backup()
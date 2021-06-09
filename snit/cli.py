from pathlib import Path
import click
from . import archive


@click.group()
# @click.option('--debug/--no-debug', default=False)
@click.option(
    "--directory",
    envvar="SNIT_DIR",
)
def cli(directory):
    # click.echo(f"Debug mode is {'on' if debug else 'off'}")
    click.echo(f"SNIT directory is set to {directory}")
    snit_dir = Path(directory)
    if not snit_dir.exists():
        raise Exception(
            "Must specify directory, either on command line or environment variable"
        )

    archive._dir = snit_dir / archive.createFileNameFromPath(Path.cwd())

    pass


@cli.command()  # @cli, not @click!
def backup():
    click.echo("backup")
    archive.backup(Path.cwd() / Path(".vscode"))

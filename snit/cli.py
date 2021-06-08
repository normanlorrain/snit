import click


@click.command()
@click.argument("number", type=int)
def cli(number: int):
    click.echo(
        "{} has become {}!".format(
            click.style(number, bold=True),
            click.style(number+10, bold=True, fg="green"),
        )
    )

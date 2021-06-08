from click.testing import CliRunner

from snit.cli import cli


def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli, ["backup"])
    assert result.exit_code == 0

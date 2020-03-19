import pytest
import click
from click.testing import CliRunner
from csv2roam import cli


def test_sync():
    @click.group()
    @click.option('--root-page', default=False)
    def cli(debug):
        click.echo('Debug mode is %s' % ('on' if debug else 'off'))

    runner = CliRunner()
    result = runner.invoke(cli, ['data.csv', 'output.md', '--root-page', '--child-pages'])
    assert result.exit_code == 0
    assert 'Debug mode is on' in result.output
    assert 'Syncing' in result.output

# @pytest.fixture
# def runner():
#     return CliRunner()
#
#
# def test_cli(runner):
#     result = runner.invoke(cli.main, ['data.csv', 'output.md'])
#     # assert result.exit_code == 0
#     assert not result.exception
#     assert result.output.strip() == 'success'
#
#
# def test_cli_with_option(runner):
#     result = runner.invoke(cli.main, ['data.csv', 'output.md', '--root-page', '--child-pages'])
#     assert not result.exception
#     # assert result.exit_code == 0
#     # assert result.output.strip() == 'Howdy, world.'
#
#
# # def test_cli_with_arg(runner):
# #     result = runner.invoke(cli.main, ['Tom'])
# #     assert result.exit_code == 0
# #     assert not result.exception
# #     assert result.output.strip() == 'Hello, Tom.'
#
# def test_cli_with_arg(runner):
#     result = runner.invoke(cli.main, ['data.csv'])
#     # assert result.exit_code == 0
#     assert not result.exception
#     # assert result.output.strip() == 'Hello, Tom.'

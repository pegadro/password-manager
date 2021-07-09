import click

from passwords import commands as passwords_commands

PASSWORDS_TABLE = '.passwords.csv'

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}
    ctx.obj['passwords_table'] = PASSWORDS_TABLE

cli.add_command(passwords_commands.all)
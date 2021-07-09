
import click

from passwords.services import PasswordService
from passwords.models import Password

@click.group()
def passwords():
    """Manages the passwords lifecycle"""
    pass

@passwords.command()
@click.option('-a', '--app',
                type=str,
                prompt=True,
                help='App, web or service of the password')
@click.option('-u', '--user',
                type=str,
                prompt=True,
                help='User or email of the password')
@click.option('-p', '--password',
                type=str,
                prompt=True,
                hide_input=True,
                confirmation_prompt=True,
                help='The password')
@click.option('-n', '--notes',
                type=str,
                prompt=True,
                help='The notes about the password')
@click.pass_context
def create(ctx, app, user, password, notes):
    """Creates a new password"""
    password_reference = Password(app, user, password, notes)
    password_service = PasswordService(ctx.obj['passwords_table'])

    password_service.create_password(password_reference)


@passwords.command()
@click.pass_context
def list(ctx):
    """List all passwords"""
    password_service = PasswordService(ctx.obj['passwords_table'])

    passwords_list = password_service.list_passwords()

    click.echo(' ID  |  APP/WEB/SERVICE  |  USER/EMAIL  |  PASSWORD  |  NOTES')
    click.echo('*' * 100)

    for password in passwords_list:
        click.echo('{uid}  |  {app}  |  {user}  |  {password}  |  {notes}'.format(
            uid=password['uid'],
            app=password['app'],
            user=password['user'],
            password=password['password'],
            notes=password['notes']
        ))


@passwords.command()
@click.argument('password_uid', type=str)
@click.pass_context
def update(ctx, password_uid):
    """Updates a password"""
    password_service = PasswordService(ctx.obj['passwords_table'])

    passwords_list = password_service.list_passwords()

    password = [password for password in passwords_list if password['uid'] == password_uid]

    if password:
        password = _update_password_flow(Password(**password[0]))
        password_service.update_password(password)

        click.echo('Password updated')
    else:
        click.echo('Password not found')

def _update_password_flow(password):
    click.echo('Leave empty if you dont want to modify the value')
    
    password.app = click.prompt('New app/web/service', type=str, default=password.app)
    password.user = click.prompt('New user/email', type=str, default=password.user)
    password.password = click.prompt('New password', type=str,  hide_input=True, confirmation_prompt=True ,default=password.password)
    password.notes = click.prompt('New notes', type=str, default=password.notes)

    return password


@passwords.command()
@click.argument('password_uid', type=str)
@click.pass_context
def delete(ctx, password_uid):
    """Delete a password"""
    password_service = PasswordService(ctx.obj['passwords_table'])

    passwords_list = password_service.list_passwords() 

    password = [password for password in passwords_list if password['uid'] == password_uid]

    if password:
        password_service.delete_password(password)

        click.echo('Password deleted')
    else:
        click.echo('Password not found')

all = passwords
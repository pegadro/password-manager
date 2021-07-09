# Password Manager CLI with Python
A CLI app make in Python to manage passwords. This program follows the principles of a CRUD. It has functions like create new passwords, read the passwords, update the passwords, and delete passwords.

## Packages needed
We only use a single package that is [Click](https://click.palletsprojects.com/en/8.0.x/), this package help us to build all the CLI.

Once you clone the project, to install the package you need to run the command:
```bash
pip install -r requirements.txt
```

## Files needed
You need to create a .csv file, in this file is where all the passwords are going to be storage. By default the file name of the .csv files must be `.passwords.csv`, so the program will works well.

If you want to change it, you need to go to `pm.py`, then to the constant `PASSWORDS_TABLE` and named like you want. The file is hidden, so it's a good idea leave it as it is.

## How to run the program?
1. First, you need to create a virtual enviroment and install the dependencies inside this venv, of course if You want it, because You can also install the dependencies in global.
2. The program run with the command `pm`. To see wants commands you can use, type `pm --help`.
3. The only command is `pm passwords`, with this command you can do everything is the program. But you need another command after this two to specify what you want to do.

## Commands
1. `pm passwords create`. This command create a new password, it ask you all the information of the password.
2. `pm passwords delete [uid]`. This command delete an existing password. You will need the uid of the password.
3. `pm passwords list`. This command simply list of the passwords existing in the `.passwords.csv` file.
4. `pm passwords update [uid]`. This commands update an existing password. You will need the uid of the password you want to modify.

Note: You get the uid by running the command `pm passwords list`, there you will see all the passwords created, and in the first column are the uid of all the passwords.
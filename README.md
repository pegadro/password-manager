# Password Manager CLI with Python
A CLI app make in Python to manage passwords. This program follows the principles of a CRUD. It has functions like create new passwords, read the passwords, update the passwords, and delete passwords.

## Packages needed
We only use a single package that is [Click](https://click.palletsprojects.com/en/8.0.x/), this package help us to build all the CLI.

Once you clone the project, to install the package you need to run the command:
```bash
pip install -r requirements.py
```

## Files needed
You need to create a .csv file, in this file is where all the passwords are going to be storage. By default the file name of the .csv files must be `.passwords.csv`, so the program will works well.

If you want to change it, you need to go to `pm.py`, then to the constant `PASSWORDS_TABLE` and named like you want. The file is hidden, so it's a good idea leave it as it is.
import csv
import os
from passwords.models import Password

class PasswordService():

    def __init__(self, table_name):
        self.table_name = table_name

    def create_password(self, password):
        with open(self.table_name, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=Password.schema())
            writer.writerow(password.to_dict())
            
    def list_passwords(self):
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f, fieldnames=Password.schema())

            return list(reader)

    def update_password(self, updated_password):
        passwords = self.list_passwords()

        updated_passwords = []
        for password in passwords:
            if password['uid'] == updated_password.uid:
                updated_passwords.append(updated_password.to_dict())
            else:
                updated_passwords.append(password)
        
        self._save_to_disk(updated_passwords)

    def delete_password(self, password):
        passwords_list = self.list_passwords()

        passwords_list.remove(password[0])

        self._save_to_disk(passwords_list)
    
    def _save_to_disk(self, passwords):
        tmp_table_name = self.table_name + '.tmp'
        with open(tmp_table_name, mode='w') as f:
            writer = csv.DictWriter(f, fieldnames=Password.schema())
            writer.writerows(passwords)

        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)
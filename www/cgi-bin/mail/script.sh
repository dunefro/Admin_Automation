#!/bin/bash

python3 mail_process.py

cat new_mail.yml

ansible-playbook new_mail.yml
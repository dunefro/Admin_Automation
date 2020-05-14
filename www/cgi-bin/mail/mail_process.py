import os
mail_to = os.getenv('MAIL','pareekvedant99@gmail.com')

with open('mail_template.yml','r+') as f:
    contents = f.read()
    contents = contents.replace('example@example.com',mail_to)

with open('new_mail.yml','w') as nf:
    nf.write(contents)

print('File part is done')
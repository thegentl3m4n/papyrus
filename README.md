# papyrus
its a website that allows their users to exchange resources like books and pdfs.

# requirements
python3.8 or above
django 3.0.6
crispy (pip module)
pillow

# how to use
you can simply run its light weight server (manage.py) if you have a system full filling application requirements.
command: "python3 manage.py runserver"

# message for front-end developer
i have used lots of inbuilt features like forms
so be careful while making changes in any of them
and all the locations that you need to work on is specified in next section
and don't touch anything that is in "{% %}" or "{{ }}"

# for front-end developer
papyrus/app/templates/,
papyrus/app/static/,
papyrus/users/templates/,

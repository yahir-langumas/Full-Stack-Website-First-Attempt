from django.contrib import admin
from .models import Todo

# Must use python manage.py makemigrations in the python terninal very time you make a change to any database model. 
# After that use python manage.py migrate to apply the changes to the database. 
admin.site.register(Todo)
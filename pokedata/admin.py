from django.contrib import admin
from .models import Species

# Must use python manage.py makemigrations in the python terminal every time you make a change to any database model. 
# After that use python manage.py migrate to apply the changes to the database. 

admin.site.register(Species)
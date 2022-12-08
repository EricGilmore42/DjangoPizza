import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django 
django.setup()

from Pizzas.models import Pizza

#topics = Pizza.objects.all()

#print(topics)

#for t in topics:
#    print(t)
#
t = Pizza.objects.get(id=1)
print(t)
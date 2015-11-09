from Property.models import Property
from django.contrib import Q

prop = Property.objects.get(slug='abb-corporate')
off = prop.offers.all()
off = off.filter(Q(stage__gt=10))

for o in off:
    print(o.investor.user_profiles.first().user.email)

for o in off:
    print(o.investor.user_profiles.all()[0].user.email)

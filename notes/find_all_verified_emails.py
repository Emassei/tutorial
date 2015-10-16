from privateportal.models import PrivatePortal
from django.db.models import Q


# Display all the private portals and their IGNORABLE_404_ENDS

for pri in PrivatePortal.objects.all():
    print(pri.sponsor, pri.id)

# id is some property id

pri = PrivatePortal.objects.get(id=16)

# This will display all of the property ids

for i in pri.offline_users.all():
    print(i.name, i.email_verified)

# Or we could use filter to return just the verified guys

verified_guys = pri.offline_users.all()

verified_guys = verified_guys.filter(Q(email_verified=True))

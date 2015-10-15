# Let's filter out a specifc string from a group of object instances, and print
# different attributes on the instances

from accounts.models import User
from django.db.models import Q

guys = User.objects.all()

guys = guys.filter(Q(email__contains='ernie'))

for guy in guys:
    print(guy.email,
          guy.id,
          guy.is_staff,
          guy.userprofile.private_portals.first())

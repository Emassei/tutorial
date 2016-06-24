import csv
from django.utils.encoding import smart_str
from datetime import datetime
from properties.utils import format_amount
from properties.models import Offer, Property

with open('prospect_import.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        smart_str(u"Email"),
        smart_str(u"First Name"),
        smart_str(u"Last Name"),
        smart_str(u"Entity"),
    ])
    guys = User.objects.filter(user_profile__investors__offers__stage__gt=5,
                               user_profile__private_portal__isnull=True).distinct()

    for o in guys:
        writer.writerow([
            smart_str(o.email),
            smart_str(o.first_name),
            smart_str(o.last_name),
            smart_str(o.user_profile.investors.first()),
        ])


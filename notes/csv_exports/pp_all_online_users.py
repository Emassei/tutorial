import csv
from django.utils.encoding import smart_str
from datetime import datetime
from properties.utils import format_amount
from properties.models import Offer, Property

with open('trion-properties.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        smart_str(u"Email"),
        smart_str(u"First Name"),
        smart_str(u"Last Name"),
        smart_str(u"Entity"),
        smart_str(u"Has Registered"),
    ])
    all_users = UserProfile.objects.filter(private_portal__sponsor__slug="trion-properties")


    for o in all_users:
        writer.writerow([
            smart_str(o.user.email),
            smart_str(o.user.first_name),
            smart_str(o.user.last_name),
            smart_str(o.investors.first()),
            smart_str(o.is_online),
        ])

import csv
from django.utils.encoding import smart_str
from datetime import datetime
from properties.utils import format_amount
from properties.models import Offer, Property

with open('trion_offline_users.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        smart_str(u"Email"),
        smart_str(u"First Name"),
        smart_str(u"Last Name"),
    ])
    spon = Sponsor.objects.get(slug='trion-properties')
    online_users = spon.privateportal.offline_users.all()

    for o in online_users:
        writer.writerow([
            smart_str(o.email),
            smart_str(o.first_name),
            smart_str(o.last_name)
        ])


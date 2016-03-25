import csv
from django.utils.encoding import smart_str
from datetime import datetime
from properties.utils import format_amount
from properties.models import Offer, Property

with open('trion_online_users.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        smart_str(u"Email"),
        smart_str(u"First Name"),
        smart_str(u"Last Name"),
    ])
    online_users = Users.privateportal.user_profiles.all()

    for o in online_users:
        writer.writerow([
            smart_str(o.user.email),
            smart_str(o.user.first_name),
            smart_str(o.user.last_name),
        ])



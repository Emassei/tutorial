import csv
from django.utils.encoding import smart_str
from datetime import datetime
from properties.utils import format_amount
from properties.models import Offer, Property

with open('offers_export2.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([

        smart_str(u"Email"),
        smart_str(u"First Name"),
        smart_str(u"Last Name"),
        smart_str(u"Phone"),
        smart_str(u"Street Address"),
        smart_str(u"City"),
        smart_str(u"State"),
        smart_str(u"Zip Code"),
        smart_str(u"ID")
    ])
    spon = Sponsor.objects.get(slug='twinrock-partners')
    ou = spon.privateportal.offline_users.all()
    for o in ou:
        writer.writerow([
            smart_str(o.email),
            smart_str(o.first_name),
            smart_str(o.last_name),
            smart_str(o.phone),
            smart_str(o.address),
            smart_str(o.city),
            smart_str(o.state),
            smart_str(o.zip_code),
            smart_str(o.id)
        ])




# Online users

for o in onu:
    print("Email: %s, First Name: %s, Last Name: %s, Phone: %s, Address: %s, City: %s, State: %s, Zip Code: %s" % (o.user.email, o.user.first_name, o.user.last_name, o.phone, o.address, o.city, o.state, o.zip_code))


# Offline Users
for o in ou:
    print("Email: %s, First Name: %s, Last Name: %s, Phone: %s, Address: %s, City: %s, State: %s, Zip Code: %s" % (o.email, o.first_name, o.last_name, o.phone, o.address, o.city, o.state, o.zip_code))
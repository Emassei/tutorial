import csv
from django.utils.encoding import smart_str
from datetime import datetime
from properties.utils import format_amount
from properties.models import Offer, Property

with open('hz-entity.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([

        smart_str(u"Email"),
        smart_str(u"Investor"),

    ])
    portal = PrivatePortal.objects.get(sponsor__slug='hamilton-zanze')
    user_profiles = UserProfile.objects.filter(private_portal=portal,
                                               date_converted__isnull=False)
    for user_profile in user_profiles:
        writer.writerow([
            smart_str(user_profile.email),
            smart_str(user_profile.investors.all()),
        ])




# Online users

for o in onu:
    print("Email: %s, First Name: %s, Last Name: %s, Phone: %s, Address: %s, City: %s, State: %s, Zip Code: %s" % (o.user.email, o.user.first_name, o.user.last_name, o.phone, o.address, o.city, o.state, o.zip_code))


# Offline Users
for o in ou:
    print("Email: %s, First Name: %s, Last Name: %s, Phone: %s, Address: %s, City: %s, State: %s, Zip Code: %s" % (o.email, o.first_name, o.last_name, o.phone, o.address, o.city, o.state, o.zip_code))
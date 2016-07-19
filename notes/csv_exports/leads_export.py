import csv
from django.utils.encoding import smart_str
from datetime import datetime
from properties.utils import format_amount
from properties.models import Offer, Property

with open('lead.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        smart_str(u"Email"),
        smart_str(u"First Name"),
        smart_str(u"Last Name"),
        smart_str(u"Entity"),
        smart_str(u"Interest Score"),
        smart_str(u"Investor Phone"),
        smart_str(u"Offer Grade"),
    ])
    offers = Offer.objects.filter(property_obj__id=159)

    for offer in offers:
        writer.writerow([
            smart_str(offer.user_profile.user.email),
            smart_str(offer.user_profile.user.first_name),
            smart_str(offer.user_profile.user.last_name),
            smart_str(offer.user_profile.investors.first()),
            smart_str(offer.leadscore),
            smart_str(offer.user_profile.phone),
            smart_str(offer.grade),
        ])

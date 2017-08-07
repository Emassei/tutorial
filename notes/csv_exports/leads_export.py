import csv
from django.utils.encoding import smart_str
from datetime import datetime
from properties.utils import format_amount
from properties.models import Offer, Property

with open('chase-suites-overland-park-leads.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        smart_str(u"Email"),
        smart_str(u"First Name"),
        smart_str(u"Last Name"),
        smart_str(u"Entity"),
        smart_str(u"Interest Score"),
        smart_str(u"Investor Phone"),
        smart_str(u"Offer Grade"),
        smart_str(u"Stage"),
        smart_str(u"Owner"),
    ])
    offers = Offer.objects.filter(property_obj__slug='chase-suites-overland-park')
    offers = offers.filter(stage__lte=0)

    for offer in offers:
        writer.writerow([
            smart_str(offer.user_profile.user.email),
            smart_str(offer.user_profile.user.first_name),
            smart_str(offer.user_profile.user.last_name),
            smart_str(offer.investor),
            smart_str(offer.leadscore),
            smart_str(offer.user_profile.phone),
            smart_str(offer.grade),
            smart_str(offer.stage),
            smart_str(offer.user_profile.owner),
        ])


import csv
from django.utils.encoding import smart_str
from datetime import datetime
from properties.utils import format_amount
from properties.models import Offer, Property

with open('chase-suites-lincoln-leads.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        smart_str(u"Email"),
        smart_str(u"First Name"),
        smart_str(u"Last Name"),
        smart_str(u"Entity"),
        smart_str(u"Interest Score"),
        smart_str(u"Investor Phone"),
        smart_str(u"Offer Grade"),
        smart_str(u"Stage"),
        smart_str(u"Owner"),
    ])
    offers = Offer.objects.filter(property_obj__slug='chase-suites-lincoln')
    offers = offers.filter(stage__lte=0)

    for offer in offers:
        writer.writerow([
            smart_str(offer.user_profile.user.email),
            smart_str(offer.user_profile.user.first_name),
            smart_str(offer.user_profile.user.last_name),
            smart_str(offer.investor),
            smart_str(offer.leadscore),
            smart_str(offer.user_profile.phone),
            smart_str(offer.grade),
            smart_str(offer.stage),
            smart_str(offer.user_profile.owner),
        ])

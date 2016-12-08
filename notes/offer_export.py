import csv
from django.utils.encoding import smart_str
from datetime import datetime
from properties.utils import format_amount
from properties.models import Offer, Property

with open('oct_export_export.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        smart_str(u"Offer ID"),
        smart_str(u"Investor"),
        smart_str(u"Project"),
        smart_str(u"Offer Amount"),
        smart_str(u"Date Submitted"),
        smart_str(u"Stage"),
        smart_str(u"Owner"),
        smart_str(u"Repeat or new"),
    ])
    offers = Offer.objects.filter(date_committed__lte=datetime(2016, 10, 31, 1, 1, 1, 1),date_committed__gte=datetime(2016, 10, 1, 1, 1, 1, 1))
    offers = offers.filter(stage__gte=5)
    offers = offers.filter(user_profile__is_marketplace_investor=True)
    offers.count()
    for o in offers:
        writer.writerow([
            smart_str(o.id),
            smart_str(o.investor),
            smart_str(o.property_obj),
            smart_str(o.amount_requested),
            smart_str(o.date_committed),
            smart_str(o.get_stage_display()),
            smart_str(o.user_profile.owner),
            smart_str(o.investor.offers.all().count()),
        ])

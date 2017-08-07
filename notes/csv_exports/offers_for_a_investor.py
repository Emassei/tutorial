import csv
from django.utils.encoding import smart_str
from datetime import datetime
from properties.utils import format_amount
from properties.models import Offer, Property

with open('vijay-export.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)s
    writer.writerow([
        smart_str(u"Property Name"),
        smart_str(u"Developer"),
        smart_str(u"Investment"),
        smart_str(u"Returns"),
        smart_str(u"Investor"),
        smart_str(u"Expected IRR"),
        smart_str(u"Date Closed"),
        smart_str(u"Amount Distributed"),
        smart_str(u"K1 Delivery Date"),
    ])
    investor = Investor.objects.filter(id=33788)
    offers = Offer.objects.filter(investor=investor,stage__gte=5)
    for o in offers:
        writer.writerow([
            smart_str(o.property_obj.name),
            smart_str(o.property_obj.sponsor.title),
            smart_str(o.amount_requested),
            smart_str(o.property_obj.get_distribution_period_display()),
            smart_str(o.investor.name),
            smart_str(o.property_obj.targeted_irr),
            smart_str(o.property_obj.date_closed),
            smart_str(o.amount_distributed),
            smart_str(o.property_obj.k1_delivery_date),
        ])

import csv
from django.utils.encoding import smart_str
from datetime import datetime
from properties.utils import format_amount
from properties.models import Offer, Property

with open('cci-export.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        smart_str(u"Property Slug"),
        smart_str(u"Property Name"),
        smart_str(u"Offer UUID"),
        smart_str(u"Investor First Name"),
        smart_str(u"Investor Last Name"),
        smart_str(u"Email"),
        smart_str(u"Investing Entity"),
        smart_str(u"Business Entity"),
        smart_str(u"Tax Entity"),
    ])
    offers = Offer.objects.filter(property_obj__sponsor__slug='capital-commercial-investments',
                                  stage__gte=100)
    for o in offers:
        writer.writerow([
            smart_str(o.property_obj.slug),
            smart_str(o.property_obj.name),
            smart_str(o.uuid),
            smart_str(o.investor.user_profiles.first().user.first_name),
            smart_str(o.investor.user_profiles.first().user.last_name),
            smart_str(o.investor.user_profiles.first().user.email),
            smart_str(o.investor_name),
            smart_str(o.business_entity),
            smart_str(o.tax_entity),
        ])

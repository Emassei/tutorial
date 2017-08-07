import csv
from django.utils.encoding import smart_str
from datetime import datetime
from properties.utils import format_amount
from properties.models import Offer, Property
from django.utils import timezone
from django.db.models import Q

def today():
    return timezone.now().date()

with open('property_export.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        smart_str(u"Property"),
        smart_str(u"Sponsor"),
        smart_str(u"Zip Code"),
        smart_str(u"State"),
        smart_str(u"City"),
    ])

    bad_sponsors = [0, 96, 41, 58, 10, 21, 12, 43, 10]
    properties = Property.objects.all()
    properties = properties.exclude(sponsor__id__in=bad_sponsors)

    for prop in properties:
        writer.writerow([
            smart_str(prop),
            smart_str(prop.sponsor),
            smart_str(prop.zip_code),
            smart_str(prop.state),
            smart_str(prop.city),
        ])

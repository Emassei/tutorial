import csv
from django.utils.encoding import smart_str
from datetime import datetime
from properties.utils import format_amount
from properties.models import Offer, Property

with open('docusign_export.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        smart_str(u"Portal Name"),
        smart_str(u"Date Created"),
        smart_str(u"Investor Name"),
        smart_str(u"Property Name"),
        smart_str(u"Status"),
    ])
    documents = DocumentEnvelope.objects.filter(date_created__lte=datetime(2017, 3, 27, 23, 59, 59, 59),
                                                date_created__gte=datetime(2016, 7, 1, 1, 1, 1, 1))
    for o in documents:
        writer.writerow([
            smart_str(o.offer.private_portal.name if o.offer.private_portal else None),
            smart_str(o.date_created),
            smart_str(o.offer.investor.name),
            smart_str(o.offer.property_name),
            smart_str(o.get_status_display()),
        ])

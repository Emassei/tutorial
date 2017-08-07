import csv
from django.utils.encoding import smart_str
from datetime import datetime
from properties.utils import format_amount
from properties.models import Offer, Property

with open('verifications_export.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        smart_str(u"Portal Name"),
        smart_str(u"Date Created"),
        smart_str(u"Investor Name"),
        smart_str(u"Successfully Issued"),
    ])
    verifications = Verification.objects.filter(date_created__lte=datetime(2016, 12, 31, 23, 59, 59, 59),
                                                date_created__gte=datetime(2016, 7, 1, 1, 1, 1, 1),
                                                method=1)
    for o in verifications:
        writer.writerow([
            smart_str(o.user_profile.private_portal.name if o.user_profile.private_portal else None),
            smart_str(o.date_created),
            smart_str(o.user_profile.investors.first().name),
            smart_str(o.get_status_display()),
        ])

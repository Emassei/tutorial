import csv
from django.utils.encoding import smart_str
from datetime import datetime
from properties.utils import format_amount
from properties.models import Offer, Property
from django.utils import timezone
from django.db.models import Q

def today():
    return timezone.now().date()

with open('sponsor_direct_analytics.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        smart_str(u"Client"),
        smart_str(u"Registered Investors"),
        smart_str(u"Manually Created Investors"),
        smart_str(u"Imported Investors"),
        smart_str(u"Total Investors"),
        smart_str(u"# of Funding Projects"),
        smart_str(u"# of Closed Projects"),
        smart_str(u"# of Realized Projects"),
        smart_str(u"Total Projects"),
        smart_str(u"Total Investment $ Managed"),
        smart_str(u"Total $ Distributed to investors"),
    ])
    private_portals = PrivatePortal.objects.all()

    for private_portal in private_portals:
        writer.writerow([
            smart_str(private_portal),
            smart_str(UserProfile.objects.filter(private_portal=private_portal, creation_method=2).count()),
            smart_str(UserProfile.objects.filter(private_portal=private_portal,creation_method=3).count()),
            smart_str(UserProfile.objects.filter(private_portal=private_portal,creation_method=1).count()),
            smart_str(UserProfile.objects.filter(private_portal=private_portal).count()),
            smart_str(Property.objects.filter(Q(date_closed__isnull=True) | Q(date_closed__gt=today()),sponsor__privateportal=private_portal,is_realized=False,status=10).count()),
            smart_str(Property.objects.filter(Q(date_closed__isnull=False), Q(date_closed__lte=today()),sponsor__privateportal=private_portal,is_realized=False,status=10).count()),
            smart_str(Property.objects.filter(is_realized=True, sponsor__privateportal=private_portal).count()),
            smart_str(Property.objects.filter(sponsor__privateportal=private_portal).count()),
            smart_str(sum([o.amount_invested for o in Offer.objects.filter(property_obj__sponsor__privateportal=private_portal, stage=100) if o.amount_invested])),
            smart_str(sum([o.amount for o in Distribution.objects.filter(offer__property_obj__sponsor__privateportal=private_portal) if o.amount])),
        ])

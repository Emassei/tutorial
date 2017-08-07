import csv
from django.utils.encoding import smart_str
from datetime import datetime, timedelta
from properties.utils import format_amount
from properties.models import Offer, Property
from django.utils import timezone
from django.db.models import Q

within_30_days = datetime.today() - timedelta(days=30)
within_90_days = datetime.today() - timedelta(days=90)
within_180_days = datetime.today() - timedelta(days=180)

def today():
    return timezone.now().date()

with open('sponsor_direct_score_card.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        smart_str(u"Portal"),
        smart_str(u"# of Properites"),
        smart_str(u"# Draft Properties"),
        smart_str(u"# Funiding Properties"),
        smart_str(u"# of Closed Properties"),
        smart_str(u"# of Archived Properties"),
        smart_str(u"$ Total Amount Invested"),
        smart_str(u"$ Total Amount of Distributions"),
        smart_str(u"# of Admin User Accounts"),
        smart_str(u"# of Unique Admin User Accounts logged in last 30 days"),
        smart_str(u"# of Unique Admin User Accounts logged in last 90 days"),
        smart_str(u"# of User Accounts"),
        smart_str(u"# of Unique User Accounts logged in last 30 days"),
        smart_str(u"# of Unique User Accounts logged in last 90 days"),
        smart_str(u"# of Unique User Accounts logged in last 180 days"),
        smart_str(u"# of User Accounts created in last 30 days"),
        smart_str(u"# of User Accounts created in last 90 days"),
        smart_str(u"# of User Accounts created in last 180 days"),
        smart_str(u"# of User Accounts with at least 1 investment"),
        smart_str(u"# of Offers submitted in last 30 days"),
        smart_str(u"# of Offers submitted in last 90 days"),
        smart_str(u"# of Offers submitted in last 180 days"),
        smart_str(u"# of Investments in Portal (across all properties)"),
        smart_str(u"# of new investments in last 30 days"),
        smart_str(u"# of new investments in last 90 days"),
        smart_str(u"# of new investments in last 180 days"),
        smart_str(u"# of Distributions in Portal (across all properties)"),
        smart_str(u"# of new distributions in last 30 days"),
        smart_str(u"# of new distributions in last 90 days"),
        smart_str(u"# of new distributions in last 180 days"),
        smart_str(u"$ of Distributions in Portal (across all properties)"),
        smart_str(u"$ of new distributions in last 30 days"),
        smart_str(u"$ of new distributions in last 90 days"),
        smart_str(u"$ of new distributions in last 180 days"),
        smart_str(u"# of Documents in portal"),
        smart_str(u"# of Documents posted in last 30 days"),
        smart_str(u"# of Documents posted in last 90 days"),
        smart_str(u"# of Documents posted in last 180 days"),
        smart_str(u"# of Email Templates in portal"),
        smart_str(u"# of Email Templates created in last 30 days"),
        smart_str(u"# of Email Templates created in last 90 days"),
        smart_str(u"# of Email Templates created in last 180 days"),
        smart_str(u"# of Saved Views (on Manage Investors) in portal"),
        smart_str(u"# of Emails sent"),
        smart_str(u"# of Emails sent in last 30 days"),
        smart_str(u"# of Emails sent in last 90 days"),
        smart_str(u"# of notes in portal"),
        smart_str(u"# of Notes left in last 30 days"),
        smart_str(u"# of Notes left in last 90 days"),
    ])
    private_portals = PrivatePortal.objects.filter(active=True)

    for private_portal in private_portals:
        writer.writerow([
            smart_str(private_portal),
            smart_str(Property.objects.filter(sponsor__privateportal=private_portal).count()),
            smart_str(Property.objects.filter(sponsor__privateportal=private_portal,status=5).count()),
            smart_str(Property.objects.filter(Q(date_closed__isnull=True) | Q(date_closed__gt=today()),sponsor__privateportal=private_portal,status=10).count()),
            smart_str(Property.objects.filter(Q(date_closed__isnull=False), Q(date_closed__lte=today()),sponsor__privateportal=private_portal,status=10).count()),
            smart_str(Property.objects.filter(sponsor__privateportal=private_portal,status=25).count()),
            smart_str(sum([o.amount_invested for o in Offer.objects.filter(property_obj__sponsor__privateportal=private_portal, stage=100) if o.amount_invested])),
            smart_str(sum([o.amount for o in Distribution.objects.filter(offer__property_obj__sponsor__privateportal=private_portal) if o.amount])),
            smart_str(UserProfile.objects.filter(private_portal=private_portal, employment__isnull=False).exclude(user__email__icontains='@crowdstreet').count()),
            smart_str(User.objects.filter(user_profile__private_portal=private_portal, user_profile__employment__isnull=False, last_login__gte=within_30_days).exclude(email__icontains='@crowdstreet').count()),
            smart_str(User.objects.filter(user_profile__private_portal=private_portal, user_profile__employment__isnull=False, last_login__gte=within_90_days).exclude(email__icontains='@crowdstreet').count()),
            smart_str(UserProfile.objects.filter(private_portal=private_portal).count()),
            smart_str(User.objects.filter(user_profile__private_portal=private_portal,last_login__gte=within_30_days).exclude(email__icontains='@crowdstreet').count()),
            smart_str(User.objects.filter(user_profile__private_portal=private_portal,last_login__gte=within_90_days).exclude(email__icontains='@crowdstreet').count()),
            smart_str(User.objects.filter(user_profile__private_portal=private_portal,last_login__gte=within_180_days).exclude(email__icontains='@crowdstreet').count()),
            smart_str(User.objects.filter(user_profile__private_portal=private_portal,date_joined__gte=within_30_days).exclude(email__icontains='@crowdstreet').count()),
            smart_str(User.objects.filter(user_profile__private_portal=private_portal,date_joined__gte=within_90_days).exclude(email__icontains='@crowdstreet').count()),
            smart_str(User.objects.filter(user_profile__private_portal=private_portal,date_joined__gte=within_180_days).exclude(email__icontains='@crowdstreet').count()),
            smart_str(UserProfile.objects.filter(private_portal=private_portal, investors__offers__stage__gte=100).distinct().count()),
            smart_str(Offer.objects.filter(user_profile__private_portal=private_portal,date_committed__gte=within_30_days).count()),
            smart_str(Offer.objects.filter(user_profile__private_portal=private_portal,date_committed__gte=within_90_days).count()),
            smart_str(Offer.objects.filter(user_profile__private_portal=private_portal,date_committed__gte=within_180_days).count()),
            smart_str(Offer.objects.filter(private_portal=private_portal,stage=100).count()),
            smart_str(Offer.objects.filter(private_portal=private_portal,stage=100,date_closed__gte=within_30_days).count()),
            smart_str(Offer.objects.filter(private_portal=private_portal,stage=100,date_closed__gte=within_90_days).count()),
            smart_str(Offer.objects.filter(private_portal=private_portal,stage=100,date_closed__gte=within_180_days).count()),
            smart_str(Distribution.objects.filter(offer__private_portal=private_portal).count()),
            smart_str(Distribution.objects.filter(offer__private_portal=private_portal,date_created__gte=within_30_days).count()),
            smart_str(Distribution.objects.filter(offer__private_portal=private_portal,date_created__gte=within_90_days).count()),
            smart_str(Distribution.objects.filter(offer__private_portal=private_portal,date_created__gte=within_180_days).count()),
            smart_str(sum([o.amount for o in Distribution.objects.filter(offer__property_obj__sponsor__privateportal=private_portal) if o.amount])),
            smart_str(sum([o.amount for o in Distribution.objects.filter(offer__property_obj__sponsor__privateportal=private_portal,date_created__gte=within_30_days) if o.amount])),
            smart_str(sum([o.amount for o in Distribution.objects.filter(offer__property_obj__sponsor__privateportal=private_portal,date_created__gte=within_90_days) if o.amount])),
            smart_str(sum([o.amount for o in Distribution.objects.filter(offer__property_obj__sponsor__privateportal=private_portal,date_created__gte=within_180_days) if o.amount])),
            smart_str(Document.objects.filter(Q(offers__user_profile__private_portal=private_portal) | Q(user_profiles__private_portal=private_portal)).count()),
            smart_str(Document.objects.filter(Q(offers__user_profile__private_portal=private_portal) | Q(user_profiles__private_portal=private_portal),date_created__gte=within_30_days).count()),
            smart_str(Document.objects.filter(Q(offers__user_profile__private_portal=private_portal) | Q(user_profiles__private_portal=private_portal),date_created__gte=within_90_days).count()),
            smart_str(Document.objects.filter(Q(offers__user_profile__private_portal=private_portal) | Q(user_profiles__private_portal=private_portal),date_created__gte=within_180_days).count()),
            smart_str(EmailTemplate.objects.filter(sponsor=private_portal.sponsor).count()),
            smart_str(EmailTemplate.objects.filter(sponsor=private_portal.sponsor,date_created__gte=within_30_days).count()),
            smart_str(EmailTemplate.objects.filter(sponsor=private_portal.sponsor,date_created__gte=within_90_days).count()),
            smart_str(EmailTemplate.objects.filter(sponsor=private_portal.sponsor,date_created__gte=within_180_days).count()),
            smart_str(TableSettings.objects.filter(user_profile__private_portal=private_portal).exclude(name='').count()),
            smart_str(InvestorEmail.objects.filter(private_portal=private_portal).count()),
            smart_str(InvestorEmail.objects.filter(private_portal=private_portal,date_created__gte=within_30_days).count()),
            smart_str(InvestorEmail.objects.filter(private_portal=private_portal,date_created__gte=within_90_days).count()),
            smart_str(Note.objects.filter(private_portal=private_portal).count()),
            smart_str(Note.objects.filter(private_portal=private_portal,date_created__gte=within_30_days).count()),
            smart_str(Note.objects.filter(private_portal=private_portal,date_created__gte=within_90_days).count()),
        ])

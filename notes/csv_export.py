import csv
from django.utils.encoding import smart_str
from datetime import datetime
from properties.utils import format_amount
from properties.models import Offer, Property

with open('offers_export2.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        smart_str(u"Investor Name"),
        smart_str(u"Entity Name"),
        smart_str(u"Email"),
        smart_str(u"date submitted"),
        smart_str(u"date invested"),
        smart_str(u"amount invested"),
        smart_str(u"stage"),
        smart_str(u"Phone"),
        smart_str(u"Street Address"),
        smart_str(u"City"),
        smart_str(u"State"),
        smart_str(u"Property Types of Interest"),
        smart_str(u"Geographic Preferences"),
        smart_str(u"Preferred Investment Holding Period"),
        smart_str(u"Preferred Market Sizes"),
        smart_str(u"Preferred Investment Vehicles"),
        smart_str(u"Investment Objectives"),
        smart_str(u"Risk Tolerance"),
        smart_str(u"Expected Investment Amount Per Project"),
        smart_str(u"Expected Total Investment in Real Estate in Next Twelve Months"),
    ])
    offs = Property.objects.get(slug='abb-corporate')
    offs = offs.offers.filter(stage=100)
    for o in offs:
        writer.writerow([
            smart_str(o.investor.user_profiles.first().user.get_full_name()),
            smart_str(o.investor),
            smart_str(o.investor.user_profiles.first().user.email),
            smart_str(o.date_committed.strftime('%x') if o.date_committed else None),
            smart_str(o.date_closed.strftime('%x') if o.date_closed else None),
            smart_str(format_amount(o.amount_invested) if o.amount_invested else None),
            smart_str(o.get_stage_display()),
            smart_str(o.investor.user_profiles.first().phone),
            smart_str(o.investor.user_profiles.first().address),
            smart_str(o.investor.user_profiles.first().city),
            smart_str(o.investor.user_profiles.first().state),
            smart_str(o.investor.user_profiles.first().get_preferred_property_types_display()),
            smart_str(o.investor.user_profiles.first().get_preferred_property_locations_display()),
            smart_str(o.investor.user_profiles.first().get_preferred_holding_periods_display()),
            smart_str(o.investor.user_profiles.first().get_preferred_property_market_sizes_display()),
            smart_str(o.investor.user_profiles.first().get_preferred_investment_vehicles_display()),
            smart_str(o.investor.user_profiles.first().get_investment_objectives_display()),
            smart_str(o.investor.user_profiles.first().get_risk_tolerance_display()),
            smart_str(o.investor.user_profiles.first().get_preferred_avg_investment_amt_display()),
            smart_str(o.investor.user_profiles.first().get_expected_12mo_cre_investment_amt_display()),
        ])

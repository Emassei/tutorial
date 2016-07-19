import datetime

import qsstats

from dateutil.relativedelta import relativedelta

from properties.models import Offer

from accounts.models import UserProfile



# get a list of offers

offers = Offer.objects.filter(

    stage__gte=Offer.SUBMITTED, private_portal=None

    ).values_list('user_profile_id', 'date_committed')



# Determine time frames

# create a list of months since Oct 1st 2015

start_date = datetime.date(2015, 10, 1, )

months = []

_date = start_date

while _date < datetime.date.today():

    _end_date = _date + relativedelta(day=31)

    months.append((_date, _end_date))

    _date = _end_date + relativedelta(days=1)



start_date = datetime.date(2015, 11, 20)  # Friday

weeks = []

_date = start_date

while _date < datetime.date.today():

    _end_date = _date + relativedelta(days=6)

    weeks.append((_date, _end_date))

    _date = _end_date + relativedelta(days=1)



######################################################################

# Sign ups



# general def of an investor in the market place

user_profile_kwargs = {

    "user__is_staff": False,

    "is_a_crowdstreet_account": False,

    "is_marketplace_investor": True,

    "user__last_login__isnull": False,

}



user_profiles = UserProfile.objects.filter(**user_profile_kwargs)

user_profile_stats = qsstats.QuerySetStats(user_profiles, 'user__date_joined')

weekly_sign_ups = [

    user_profile_stats.time_series(i[0], i[1], 'weeks') for i in weeks]

weekly_sign_ups_cume = [

    [i, user_profile_stats.until(i[1])] for i in weeks]

monthly_sign_ups = [

    user_profile_stats.time_series(i[0], i[1], 'months') for i in months]

monthly_sign_ups_cume = [

    [i, user_profile_stats.until(i[1])] for i in months]



######################################################################

# first time and repeat investor stats





def in_range(d, start, end):

    return d >= start and d <= end





def before_date(d, _date):

    return d < _date





def total_in_range(d_list, start, end):

    return sum([in_range(t, start, end) for t in d_list])





def total_before_date(d_list, _date):

    return sum([before_date(t, _date) for t in d_list])





# convert offers into investments (list of committed offer dates)

investments = []

for offer in offers:

    try:

        record = next(d for i, d in enumerate(investments) if offer[0] in d)

        key = record.keys()[0]

        # try:

        record[key].append(offer[1].date())

        # except AttributeError:

        #     print 'Couldn\'t find id {}'.format(offer[0])

    except StopIteration:

        # try:

        investments.append({offer[0]: [offer[1].date(), ]})

        # except AttributeError:

        #     print 'Couldn\'t find id {}'.format(offer[0])



results = []

num_offer_range = range(1, 16)



periods = weeks



for period in periods:

    new_first_timer = 0

    new_repeat = 0

    for inv in investments:

        d_list = inv.values()[0]

        t_in = total_in_range(d_list, period[0], period[1])

        t_before = total_before_date(d_list, period[0])

        t_end = total_before_date(d_list, period[1])

        if t_before <= 1 and t_end > 1:

            new_repeat += 1

        elif t_before == 0 and t_end > 0:

            new_first_timer += 1



    hist = {}

    for x in num_offer_range:

        counter = 0

        for inv in investments:

            t_at_end = total_before_date(inv.values()[0], period[1])

            if t_at_end == x:

                counter += 1

        hist.update({x: counter})



    results.append([period, new_first_timer, new_repeat, hist])









# Sign up numbers

"""

from dateutil.relativedelta import relativedelta

user_profiles = UserProfile.objects.filter(**user_profile_kwargs)

results = []

for i in weeks:

    kwargs = {

        "user__is_staff": False,

        "is_a_crowdstreet_account": False,

        "is_marketplace_investor": True,

        # user__last_login__isnull=True

        'user__date_joined__gte': i[0],

        'user__date_joined__lt': i[1] + relativedelta(days=1)

    }

    results.append([i[0], i[1], UserProfile.objects.filter(**kwargs).distinct().count()])





results2 = []

for i in weeks:

    kwargs = {

        "approval_status": UserProfile.APPROVAL_APPROVED,

        "user__is_staff": False,

        "is_a_crowdstreet_account": False,

        "is_marketplace_investor": True,

        "investors__accreditation__gt": Investor.NON_ACCREDITED,

        'user__date_joined__gte': i[0],

        'user__date_joined__lt': i[1] + relativedelta(days=1)

    }

    results2.append([i[0], i[1], UserProfile.objects.filter(**kwargs).distinct().count()])

"""
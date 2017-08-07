pp = PrivatePortal.objects.get(sponsor__slug='sponsor')
offs = pp.offers.all()

# just a ton of filtering I could of done with a list comprehension
offs = offs.filter(private_portal__isnull=False)
offs = offs.filter(stage__gt=10)

# List Comprehension
[o.amount_requested for o in offs]

# Now we can sum this up
sum([o.amount_requested for o in offs])

# When a list comprehension is in brackets it immedietly creates
# a list
[o.amount_requested for o in offs]

# But when you put the list comprehension it puts it in a 
# 'lazy list' or a generator, it does not immedietly create a list
(o.amount_requested for o in offs)


# when this generator is placed instide a function it then 
# creates a list at that moment, not before
sum(o.amount_requested for o in offs)

# You can also filter inside of the list comprehension 
o.amount_requested for o in offs if o.amount_requested > 10000)


# How I actually used it
[o.email for o in mes if o.sponsor.first().slug=='green-visor-capital']




emails = InvestorEmail.objects.filter(subject__contains='Residences at Great Pond')
ids = [o.user_profile.id for o in emails]
print(len(ids))
offers = Offer.objects.filter(property_obj__slug='residences-great-pond',user_profile__id__in=ids)
print(offers.count())




existing_sponsor_list = [
    'sponsor',

]

private_portals = PrivatePortal.objects.filter(active=True)
active_sponsor_list = [o.name for o in private_portals]

not_in_the_list = set(existing_sponsor_list) - set(active_sponsor_list)
not_in_the_list = list(not_in_the_list)

"""
This is to find out what the differences are between two lists
"""

private_portals = PrivatePortal.objects.filter(
    sponsor__title__in=not_in_the_list)

[private_portal.id for private_portal in private_portals]


pp = PrivatePortal.objects.get(sponsor__slug='mascia-development')
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

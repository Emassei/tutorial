off = Offer.objects.all()
# checking for private portals, these are CS offers
off = off.filter(private_portal__isnull=True)
# Now these are offers greater than or equal to submitted
off = off.filter(stage__gte=5)
# We can filter by month
off = off.filter(date_committed__month=1)
# Or by year
off = off.filter(date_committed__year=2015)
# And now we sum items
off.aggregate(Sum('ammount_submitted'))

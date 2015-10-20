# This will filter all sponsosrs according to what it starts with 

spon = Sponsor.objects.filter(slug__startswith='apex')

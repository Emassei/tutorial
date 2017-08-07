portal = PrivatePortal.objects.get(sponsor__slug='hamilton-zanze')

def change_offer():
    offers = Offer.objects.filter(stage=101,
                                  private_portal=portal,
                                  net_amount_invested__gt=5)
    i=0
    ids = [o.id for o in offers]
    for o in offers:
        net_amount_invested = o.net_amount_invested
        o.amount_requested = net_amount_invested
        o.net_amount_invested = None
        o.save()
        i+=1
    print('Changed {} offers'.format(i))

change_offer()

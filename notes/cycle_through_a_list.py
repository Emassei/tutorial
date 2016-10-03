offer_ids =[72444,69544,69876,71864,70535,71867,72418]

for id in offer_ids:
    o = Offer.objects.get(id=id)
    print(o,o.date_created)
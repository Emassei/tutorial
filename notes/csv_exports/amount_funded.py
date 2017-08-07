cont = ContentType.objects.filter(model='offer')

private_portals = PrivatePortal.objects.filter(active=True)

for private_portal in private_portals.iterator():
    ids = []
    offers = Offer.objects.filter(private_portal=private_portal)
    for offer in offers:
        if Action.objects.filter(
                target_content_type=cont, 
                target_object_id=offer.id, 
                verb__icontains='offered').exists():
            ids.append(offer.id)


    total = Offer.objects.filter(id__in=ids).aggregate(Sum('amount_requested'))
    print(total['amount_requested__sum'], private_portal)
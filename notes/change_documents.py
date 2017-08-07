def change_documents():
    documents = Document.objects.filter(property_obj__isnull=False, offers__isnull=False)
    for o in documents:
        o.property_obj = None
        o.save()
        print(o)

change_documents()

def remove_label_on_docs():
    import datetime
    """
    1.
    remove december for docs that fit this criteria
    6/1/2017
    December
    sponsor__slug='ti_holdings'
    """

    documents = Document.objects.filter(
        month=12,
        date_created__gte=datetime.datetime(2017, 6, 1),
        date_created__lt=datetime.datetime(2017, 6, 2),
        property_obj__sponsor__slug='taurus-real-estate-holdings'
    )

    for o in documents:
        o.month = None
        o.save()
        print(o)

remove_label_on_docs()
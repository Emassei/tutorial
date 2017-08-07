image = PropertyImage.objects.get(pk=179)

image.property_obj = Property.objects.get(id=19)
image.pk = None
image.image_file.url=u'xxxx'
image.image_file.save()
image.save()
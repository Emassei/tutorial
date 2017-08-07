
import boto3
from django.core.files.base import ContentFile
from properties.models import PropertyImage
from time import sleep

s3 = boto3.client('s3', 'us-west-1')

objs_tuple = (
(626, 'xxx', 20),
)


def _get_file_from_s3(file_name):
    response = s3.get_object(Bucket='hz-business-plans-import-6-4-17', Key=file_name)
    return ContentFile(response['Body'].read())


def create_property_images_from_s3(objs_tuple):
    prop_image_count = 0
    for property_id, file_name, image_type in objs_tuple[0:1]:
        prop_image_count += 1
        prop_image = PropertyImage.objects.create(
            order=0,
            property_obj_id=property_id,
            image_type=image_type
        )
        prop_image
        prop_image.image_file.save(
            file_name,
            _get_file_from_s3(file_name),
            save=True
        )
        sleep(2)
        print('Loaded {}!'.format(file_name))


    print('Created {} property images.'.format(prop_image_count))


create_property_images_from_s3(objs_tuple)

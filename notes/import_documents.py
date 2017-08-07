
import boto3
from django.core.files.base import ContentFile
from properties.models import PropertyImage
from time import sleep

s3 = boto3.client('s3', 'us-west-1')

objs_tuple = (
    (111, 'Xxx', 5, 'xxx'),

)


def _get_file_from_s3(file_name):
    response = s3.get_object(Bucket='hz-business-plans-import-6-4-17', Key=file_name)
    return ContentFile(response['Body'].read())


def create_property_documents_from_s3(objs_tuple):
    prop_document_count = 0
    for property_id, file_name, doc_type, name in objs_tuple:
        prop_document_count += 1
        prop_document = PropertyDocument.objects.create(
            order=0,
            property_obj_id=property_id,
            doc_type=doc_type,
            name=name
        )
        prop_document.doc_file.save(
            file_name,
            _get_file_from_s3(file_name),
            save=True
        )
        sleep(2)
        print('Loaded {}!'.format(file_name))


    print('Created {} property document.'.format(prop_document_count))


create_property_documents_from_s3(objs_tuple)

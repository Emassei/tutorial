def change_long_description():
    list = [414]
    properties = Property.objects.filter(sponsor__slug='hamilton-zanze')
    properties = properties.exclude(id__in=list)
    long_description = '<h3>Section Coming Soon</h3>'
    prop_count = 0
    for o in properties:
        o.long_description = long_description
        o.save()
        prop_count += 1
        print('Changed {} long description'.format(o))

    print('Created {} detail pages.'.format(prop_count))


change_long_description()



from properties.models import Property
from time import sleep

objs_tuple = (
    (732,'<div class=\"jumbotron\">\n      <h2 style=\"margin-bottom: 18px;\">Confidential Investment Overview</h2>\n      <p style="font-size: 13px;font-style: italic;">This document is confidential, intended for, and provided only to accredited investors who have a pre-existing relationship with Hamilton Zanze & Company (HZ).  If you are accessing this document and cannot or do not meet the above criteria, please close the document, refrain from further accessing it and/or this website in any way until further notice, and log off.  The material contained in this document is provided solely for the purposes of your consideration and your analysis of an investment in the described property and may not to be copied, reproduced, redistributed, and/or used for any other purposes whatsoever, or made available to any other persons without the express written consent of HZ.  Access to this document is provided without warranty or representation as to the accuracy, completeness, or fitness for any purpose of the information, assumptions, analyses, underwriting, or conclusions presented in this document, if any.  This document is intended to evolve at any time based on new and/or different facts, circumstances, market, or economic conditions and, accordingly, is subject to change in any or all respect at any time and should not be relied upon as the exclusive basis for any investment decision by you.</p>\n      <p><a class=\"btn btn-primary btn-lg\" href=\"x\">Download</a></p>\n    </div>'),
    (681,'<div class=\"jumbotron\">\n      <h2 style=\"margin-bottom: 18px;\">Confidential Investment Overview</h2>\n      <p style="font-size: 13px;font-style: italic;">This document is confidential, intended for, and provided only to accredited investors who have a pre-existing relationship with Hamilton Zanze & Company (HZ).  If you are accessing this document and cannot or do not meet the above criteria, please close the document, refrain from further accessing it and/or this website in any way until further notice, and log off.  The material contained in this document is provided solely for the purposes of your consideration and your analysis of an investment in the described property and may not to be copied, reproduced, redistributed, and/or used for any other purposes whatsoever, or made available to any other persons without the express written consent of HZ.  Access to this document is provided without warranty or representation as to the accuracy, completeness, or fitness for any purpose of the information, assumptions, analyses, underwriting, or conclusions presented in this document, if any.  This document is intended to evolve at any time based on new and/or different facts, circumstances, market, or economic conditions and, accordingly, is subject to change in any or all respect at any time and should not be relied upon as the exclusive basis for any investment decision by you.</p>\n      <p><a class=\"btn btn-primary btn-lg\" href=\"x">Download</a></p>\n    </div>'),
)

def change_long_description(objs_tuple):
    prop_count = 0
    for property_id, long_description in objs_tuple:
        property = Property.objects.get(id=property_id)
        property.long_description = long_description
        property.save()
        prop_count += 1


        sleep(2)
        print('Loaded {}!'.format(property))


    print('Created {} detail pages.'.format(prop_count))


change_long_description(objs_tuple)

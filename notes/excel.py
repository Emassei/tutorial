import xlrd

workbook = xlrd.open_workbook('')

worksheet = workbook.sheet_by_index(0)

row = worksheet.row(3)

investing_entity_label = 'Investing Entity Name'
description_label = 'Description'
property_slug_label = 'Property Slug'
distribution_date_label = 'Distribution Date'

def create_description_tuple():
    """
    grab values from a excel sheet matching defined critera and put in a tuple
    """
    investing_entity_names = worksheet.col_values(2)
    investing_entity_target = investing_entity_names.index(
        investing_entity_label)
    investing_entity_names = investing_entity_names[investing_entity_target+1:]

    description_names = worksheet.col_values(7)
    description_target = description_names.index(description_label)
    description_names = description_names[description_target + 1:]

    property_slug = worksheet.col_values(0)
    property_slug_target = property_slug.index(property_slug_label)
    property_slugs = property_slug[property_slug_target + 1:]

    distribution_date = worksheet.col_values(15)
    distribution_date_target = distribution_date.index(distribution_date_label)
    distribution_date = distribution_date[distribution_date_target + 1:]
    date_list = []
    for date in distribution_date:
        item = xlrd.xldate_as_tuple(date,0)
        date_list.append(item)

    objs_tuple = tuple(zip(
        property_slugs, date_list, investing_entity_names, description_names))
    return objs_tuple
    import ipdb; ipdb.set_trace()
objs_tuple = create_description_tuple()

def add_description_to_distributions(objs_tuple):
    """
    add a description to a distribution with values from the tuple
    """
    for property_slugs, date_list, investing_entity_names, description_names in objs_tuple[0:1]:
        distribution = Distribution.objects.filter(
            offer__investor__name=investing_entity_names,
            offer__property_obj__slug=property_slugs)
        distribution.description = description_names
        distribution.save()
        print(distribution)

create_description_tuple()
add_description_to_distributions(objs_tuple)

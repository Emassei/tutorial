def change_document_name():
    documents = Document.objects.filter(name__icontains=".PDF",
                                        property_obj__sponsor__slug=(
                                            'hamilton-zanze')
                                        )
    i = 0
    pdf_string = ".PDF"
    for document in documents:
        document.name = document.name.replace(pdf_string, "")
        document.save()
        i += 1
        print("changed {}".format(document))
    print("changed {}".format(i))

change_document_name()

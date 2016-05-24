from esign.docusign import DocuSignClient

# Assign docusign to a variable
client = DocuSignClient()

# Grab a document
doc = DocumentEnvelope.objects.get(envelope_id='c81d71a1-1fea-497e-b48d-6c95125f5f52')


# Call some methods!
client.get_envelope_recipients(doc.envelope_id)


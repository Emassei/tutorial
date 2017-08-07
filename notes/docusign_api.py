from esign.docusign import DocuSignClient

# Assign docusign to a variable
client = DocuSignClient()

# Grab a document
doc = DocumentEnvelope.objects.get(envelope_id='xxx')


# Call some methods!
client.get_envelope_recipients(doc.envelope_id)


# Save someones docs to their room
doc.save_envelope_docs_as_investor_docs()
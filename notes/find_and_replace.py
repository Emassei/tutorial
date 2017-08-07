bad_sponsors = [96,22,0,46,93]
private_portals = PrivatePortal.objects.all()
private_portals = private_portals.exclude(id__in=bad_sponsors)


for o in private_portals:
    css = o.css_overrides
    css = css.replace('.capstack-wrapper .capstack .capstack-legend .capstack-entry{\r\n    font-size: inherit;\r\n', '.capstack-wrapper .capstack .capstack-legend .capstack-entry{\r\n    font-size: inherit;}\r\n')
    o.css_overrides = css
    o.save()
    print(o, 'changed')



pp = PrivatePortal.objects.filter(active=True, header_template__icontains='(BETA) Mgmt. Portal v2</a></li>')


for o in pp[0:1]:
    domain = "https://{}".format(o.domain)
    header = o.header_template
    header = header.replace("(BETA) Mgmt. Portal v2</a></li>\r\n", 'Management Console</a></li>\r\n')
    o.header_template = header
    o.save()
    print(o.id,o)


for o in pp:
    header = o.header_template
    header = header.replace("(BETA) Mgmt. Portal v2</a></li>", '(BETA) Mgmt. Console v2</a></li>')
    o.header_template = header
    o.save()
    print(o.id,o)




# This is the syntax for adding variables
print("something {} goes here: {} <--".format(42, "hi"))

# This is a method to make an empty set
c = set()
d = dict()
e = list()

# This is a dict
f = {1: 'a'}
# This is a set, this is the same as a list but the values are the same
# as the keys
g = {1, 2, 3}
# This is a tuple
t = tuple(g)

props = Property.objects.all()
a = []
b = []
c = set()

for o in props:
    if o.projected_cash_flows.exists():
        a.append(o)
        c.add(o.sponsor)
    else:
        b.append(o)

print(len(b), "number of properties have not "
              "uploaded projected distributions")

print(len(a), "number of properties have "
              "uploaded projected distributions "
              "for ", c)

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

l=[
x
]


objs_tuple = [
    ('ArborCrowd', 42),
]

# Mapping a tuple to a list
new_list=[]

for o in l:
    for title, id in objs_tuple:
        if o == id:
            o = title
            new_list.append(o)
print(new_list)



# This counts the number of occurences in a list

from collections import Counter

print(Counter(l))

# Map ocurance number to sponsor name and add to a new list

objs_tuple= (
    (42, 303),

 )

new_list = []
for id, occurence in objs_tuple:
    private_portal = PrivatePortal.objects.get(id=id)
    new_list.append(private_portal.sponsor.title)
    new_list.append(occurence)
    new_list
print(new_list)



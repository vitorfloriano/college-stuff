import json

d = dict()

d['name'] = 'Bob'
d['age'] = 20
d['score'] = 88

jd = json.dumps(d)

print(jd)

dd = json.loads(jd)

print(dd)

print(type(dd))

print(type(d))

print(type(jd))


list1 = {"name": "Balaji", "age": 26, "city": "sivaganga"}
mark = {"m1": 50, "m2": 34, "m3": 45, "m4": 54, "m5": 50}
# print(sum(mark.values()))
res = {"total": 233, "result": "P", "grade": "A"}

dict1 = {"l1": list1, "mark": mark, "res": res}

from crudApp.models import models,Students

v1=Students.objects.all()
print(v1)
d1 = dict()
#print(dict1)
#print(dict1['l1'])

for i in dict1:
    #print(dict1[i])
    for j,k in dict1[i].items():
        print(j,k)
        d1[j] = k
print(d1)
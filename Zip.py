names = ('Rachel','Claudia','Allison')
company = ('Dell','Apple','MS')

Zipped = list(zip(names,company))

print(Zipped)

names = ('Ross','Harry','Malia')
phone = ('Samsung','Iphone','Oppo')

Zip = zip(names,phone)

for a,b in Zip:
    print(a,b)
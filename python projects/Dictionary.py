mydict={'sanu':'is a sister',
        'animal':'lion'
}
print(mydict)
print(mydict.keys())
print(type(mydict.keys()))
print(mydict.values())
print(type(mydict.values()))
print(mydict.items())
print(type(mydict.items()))
# we can update list
mydict['animal']='tiger'
print(mydict)
## update method or operation on dictionary
mydict_update={
    "shrinath":"sanu's brother"
}
mydict.update(mydict_update)## to add element which is not present
print(mydict)
updatedict={
    "shrinath":"sanu's younger brother"
}
mydict.update(updatedict)
print(mydict)

## get method or operation to get value at any key
print(mydict.get('shrinath'))#this will the value at 'shrinath' key
print(mydict['shrinath'])#this will also the value at 'shrinath' key
print(mydict.get('america'))#this will show none because it is not present at any key
#print(mydict['america']) #this will show error because it is not present at any key

#Nested dictionary
dict1={'num':1,'dict2':{'float':2.01,'double':2.001548}}
print(dict1['dict2']['double'])
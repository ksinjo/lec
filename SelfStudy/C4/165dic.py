# declear dictionary 
dictionary = {
    "name" : "4D 건조 망고",
    "type" : "당쩔어",
    "ingredient": ["개망고","설퇑","메타중화산나트륨","치자황색소"],
    "origin": "필리퓐"
}
dictionary["price"] = 5000
dictionary["delitem"] = 999

print(dictionary)

del dictionary["delitem"]
print(dictionary)

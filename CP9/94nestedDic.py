#Nesting
capitals = {
    "France": "paris",
    "Germay" : "Berlin"
}

#Nesting a List in a Dictionary

traval_log = {
    "France" : {"cites visted": ["paris", "Lille","dijon"],"total_visted":12},
    "Germany": {"cites visted":["Berlin","Hamburg","stuttgart"],"total_visted":5}
}

#Nesting Dictionary in a List


traval_log = [
    {
        "country":"France" , 
        "cites visted": ["paris", "Lille","dijon"],
        "total_visted":12
        },
    {
        "country":"Germany", 
        "cites visted":["Berlin","Hamburg","stuttgart"],
        "total_visted":5
        }
]
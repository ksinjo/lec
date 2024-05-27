
enemies = 10

def increatse_enemise():
    # global enemies
    # enemies += 1 
    print(f"ememies inside function : {enemies}")
    return enemies + 1 

enemies = increatse_enemise()
print(f"ememies outside function :{enemies}")
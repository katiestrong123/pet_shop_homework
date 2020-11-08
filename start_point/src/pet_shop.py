# PET SHOP FUNCTIONS
def get_pet_shop_name(list):
    return(list["name"])
    
def get_total_cash(list):
    return list["admin"]["total_cash"]

def add_or_remove_cash(list, cash):
    list["admin"]["total_cash"] += cash

def get_pets_sold(list):
    return(list["admin"]["pets_sold"])

def increase_pets_sold(list, number_of_pets_sold):
    list["admin"]["pets_sold"] += number_of_pets_sold

def get_stock_count(list):
    return len(list["pets"])
            
def get_pets_by_breed(list, breed):
    pets_by_breed = []
    for pet in list["pets"]:
        if pet["breed"] == breed:
            pets_by_breed.append(pet)
    return pets_by_breed

def find_pet_by_name(list, name):
    for pet in list["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(list, name):
    for pet in list["pets"]:
        if  pet["name"] == name:
            list["pets"].remove(pet)

def add_pet_to_stock(list, pet):
    list["pets"].append(pet)

def get_customer_cash(customer_list):
    return customer_list["cash"]

def remove_customer_cash(customer_list, cash):
    customer_list["cash"] -= cash

def get_customer_pet_count(customer_list):
    return len(customer_list["pets"])

def add_pet_to_customer(customer_list, new_pet):
    customer_list["pets"].append(new_pet)
    return get_customer_pet_count(customer_list)

#  # --- OPTIONAL ---

def customer_can_afford_pet(customer_list, price):
    # can_by_pet = False 
    customer_cash = customer_list["cash"] 
    if customer_cash >= 100:
        can_by_pet = True 
    else:
        can_by_pet = False 
    return can_by_pet


         

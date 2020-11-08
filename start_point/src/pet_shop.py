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

def find_pet_by_name(list, pet_name):
    for pet in list["pets"]:
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(list, pet_name):
    for pet in list["pets"]:
        if pet["name"] == pet_name:
            list["pets"].remove(pet)

def add_pet_to_stock(list, pet):
    list["pets"].append(pet)

def get_customer_cash(list):
    return list["cash"]

def remove_customer_cash(list, cash):
    list["cash"] -= cash

def get_customer_pet_count(list):
    return len(list["pets"])

def add_pet_to_customer(list, new_pet):
    list["pets"].append(new_pet)
    return get_customer_pet_count(list)

#  # --- OPTIONAL ---

def customer_can_afford_pet(list, price):
    customer_cash = list["cash"] 
    if customer_cash >= 100:
        can_by_pet = True 
    else:
        can_by_pet = False 
    return can_by_pet

 #  # --- INTERGRATION TESTS -----
   


#    CODE 
            # DOESN'T 
                    #  WORK 
def sell_pet_to_customer(list, pet_name, customer_name):
    if pet_name == find_pet_by_name(list, pet_name):
        get_customer_pet_count(list) + 1 
        get_pets_sold(list) + 1 
        remove_pet_by_name(list, pet_name)
        add_or_remove_cash(list, 900)
        remove_customer_cash(list, cash) 
        
        
        


# If pet_name == a pet in the pet store and Remove the pet from pet store by name. then take the moeny from the customer, decrement their cash, increment pet store cash. Increment pet store sold pets by one and increment customer pets [] by one. 
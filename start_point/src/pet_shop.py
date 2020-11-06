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
    for dog in list:
        if breed == list["pets"]["breed"]:
            return dog

def get_pets_by_name(list, name):
    for dog in list:
        if name == list["pets"]["name"]:
            return dog

# PET SHOP FUNCTIONS
def get_pet_shop_name(list):
    return(list["name"])
    
def get_total_cash(list):
    return list["admin"]["total_cash"]

def add_or_remove_cash(list, cash):
    list["admin"]["total_cash"] += cash


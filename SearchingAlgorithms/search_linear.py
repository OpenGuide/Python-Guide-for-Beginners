def search(search_term, search_list):
    """Finds if search term (string) exist in list"""
    for term in search_list:        #iterating each string in search list
        if search_term in term:     #creates condition if search term is found in above list
            return True             #returns True if the search_term does exist in list
        return False                #returns False if it does not exist in list

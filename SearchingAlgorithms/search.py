def search(search_term, search_list):
    """Finds if search term (string) exist in list"""
    for term in search_list:
        if search_term in term:
            return True
        return False

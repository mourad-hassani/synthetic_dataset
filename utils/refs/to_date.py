def to_date(annotation, current_date):
    if annotation == "PRESENT_REF":
        return [current_date]
    if annotation == "THIS NI":
        return [f"{current_date}TNI"]
    if annotation == "THIS MO":
        return [f"{current_date}TMO"]
    
    return None
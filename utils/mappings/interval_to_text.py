from utils.mappings.date_to_text import date_to_text

def interval_to_text(annotation):
    first_date, second_date = annotation.split(",")
    first_text = date_to_text(first_date)
    second_text = date_to_text(second_date)
    return f"from {first_text} to {second_text}"
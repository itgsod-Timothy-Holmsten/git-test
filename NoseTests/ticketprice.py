def ticket_price(age):
    age = int(age)
    if age < 0:
        raise(ValueError, 'Age must not be negative')
    if age < 18:
        return 10
    elif age <= 64:
        return 20
    else:
        return 15
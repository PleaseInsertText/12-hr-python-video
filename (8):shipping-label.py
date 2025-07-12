def shipping_label(*args, **kwargs):

    """The parameters do not need to be called
       args" or "kwargs", it is more sensible to.
       The * or ** tells if its args or kwargs."""

    for arg in args:
        print(arg, end = " ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")

    else:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")

    if "po_box" in kwargs:
        print(f"{kwargs.get('po_box')}")
        
    if "state" in kwargs:
        print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('postcode')}")
    else:
        print(f"{kwargs.get('city')} {kwargs.get('postcode')}")

print("\n---- SHIPPING LABEL ----\n")
shipping_label("Sir", "Samosa", "Brick",
               street = "123 Internet Street",
               #state = "Imaginary State",
               #apt = "#100",
               #po_box = "PO box #1000",
               city = "Metropolis",
               postcode = "SW1A 1AA (Buckingham Palace)")

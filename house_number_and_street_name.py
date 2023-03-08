def format_address(address_string):
    house_number = ""
    street_name = ""

    address_parts = address_string.split()
    
    for address_part in address_parts:
       if address_part.isnumeric():
         house_number = address_part
       else:
         street_name += address_part + " "
    street_name = street_name.strip()
 
    return "House number {} on a street named {}".format(house_number,street_name)

print(format_address("123 Main Street"))
# Should print: "House number 123 on a street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "House number 1001 on a street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "House number 55 on a street named North Center Drive"

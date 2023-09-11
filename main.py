import sqlicense_plate

# Test the function
print(sqlicense_plate.check_license_plate("ABC123"))  # Should print "RECOGNIZED"
print(sqlicense_plate.check_license_plate("NOT_IN_DB"))  # Should print "NO DATA"


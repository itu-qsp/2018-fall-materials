def incrementor(weak_number):
    strong_number = weak_number +1
    return strong_number
    
print(incrementor(2))
print(incrementor(-1))
print(incrementor(2.99999))
print(incrementor(2.999999999999999999999999999999999999999999999999999999999999999999999999999))
print(incrementor(-2))
print(incrementor(0.0))
print(incrementor(0))
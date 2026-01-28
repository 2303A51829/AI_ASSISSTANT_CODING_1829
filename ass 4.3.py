def cm_to_inches(cm):
    inches = cm / 2.54
    return round(inches, 2)

# Sample test cases
print(cm_to_inches(10))    # 3.94
print(cm_to_inches(2.54))  # 1.0
print(cm_to_inches(50))    # 19.69
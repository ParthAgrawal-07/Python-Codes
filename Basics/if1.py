is_Male = False
is_Tall = True
if is_Male and is_Tall:
    print("Male and Tall")
elif is_Male and not(is_Tall):
    print("Male and Not Tall")
elif not(is_Male) and is_Tall:
    print("Female and Tall")
else:
    print("Female and Not Tall")
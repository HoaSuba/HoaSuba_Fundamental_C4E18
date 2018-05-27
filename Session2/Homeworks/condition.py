# Điều kiện lồng nhau theo mình hiểu concept của nó là:
# Trong A, cần thêm điều kiện B thì ra C, còn nếu không phải là B thì kết quả sẽ khác C.

today = input("How are you feel today?")
weather = input("What's the weather like?")
if today == "good":
    if weather == "nice day":
        print("Let's go")
    else:
        print("Maybe should read book")

else:
    print("Stay at home alone.")
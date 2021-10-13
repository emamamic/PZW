a = int(input("Unesi broj a: "))

b = int(input("Unesi broj b: "))

suma = a + b 

razlika = a - b

količnik = a / b 

umnožak = a * b

c = (input("Odaberi računsku operaciju: "))

if c == "+":
    print(suma)

elif c == "-":
    print(razlika)

elif c == "*":
    print(umnožak)

elif c == "/":
    print(količnik)

else:
    print("pokušaj ponovno, pusa")
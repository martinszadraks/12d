a = float(input("Ievadiet kvadrāta malas garumu, kas ir lielāks par 5cm: "))


lauk = a * a
mala2 = a + 5
lauk2= mala2 * mala2
proc = (lauk2 - lauk) / 100
rezult = proc * 100

print("Procentu starpība ir " + str(rezult) + ".")

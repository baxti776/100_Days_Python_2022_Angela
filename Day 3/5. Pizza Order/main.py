s_pizza = 15
m_pizza = 20
l_pizza = 25
pep_f_s = 2
pep_f_l = 3
extra_cheese_price = 1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L ")
add_pepperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")

if size == "S":
    print(f"Your Pizza is {s_pizza}$.")
    if add_pepperoni == "Y":
        s_pizza += pep_f_s
        print(f"Pepperoni for Small Pizza is 2$. You need to pay {s_pizza}$")
    if extra_cheese == "Y":
        s_pizza += extra_cheese_price
        print(f"Extra cheese for Small Pizza is 1$. You need to pay {s_pizza}$")
elif size == "M":
    print(f"Your Pizza is {m_pizza}$.")
    if add_pepperoni == "Y":
        m_pizza += pep_f_l
        print(f"Pepperoni for Small Pizza is 3$. You need to pay {m_pizza + pep_f_l}$")
    if extra_cheese == "Y":
        m_pizza += extra_cheese_price
        print(f"Extra cheese for Small Pizza is 1$. You need to pay {m_pizza + pep_f_l + extra_cheese_price}$")
elif size == "L":
    print(f"Your Pizza is {l_pizza}$.")
    if add_pepperoni == "Y":
        l_pizza += pep_f_l
        print(f"Pepperoni for Small Pizza is 3$. You need to pay {l_pizza + pep_f_l}$")
    if extra_cheese == "Y":
        l_pizza += extra_cheese_price
        print(f"Extra cheese for Small Pizza is 1$. You need to pay {l_pizza + pep_f_l + extra_cheese_price}$")
else:
    print("There is no that kind of pizza.")
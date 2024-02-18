def make_pizza(*toppings):
    #for toppings in toppings:
        print(toppings)
My= make_pizza("tommatoes","Brocolli", "Paneer")
Vicky= make_pizza("Mushroom", "Paneer","onio","corn")
Param= make_pizza("Cheese","olives")


def make_pizza_base(*topings, base):
    print(topings, base)
    #for toping in topings:
       # print(toping)


Neha = make_pizza_base("olive", "onion", "tomato", base="thin")

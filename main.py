from models import Functions, Newton

fx1 = Functions(a=4, b=2, c=2, d=1, k=4)

print(repr(fx1))


# print(fx1.eval(3))
new = Newton(fx=fx1, initial_guess=5.0, nit=5)
print(new.findroots(root=5))
import random

def parni(brojevi):
    for broj in range(brojevi):
        if broj%2==0:
            yield broj

def neparni(brojevi):
    for broj in range(brojevi):
        if broj%2!=0:
            yield broj

broj=random.randint(0, 100)
print(broj)

print("Parni brojevi: ", list(parni(broj)))
print("Neparni brojevi: ", list(neparni(broj)))

N = int(input("Enter your number to be factored: "))
G = int(input("Enter your best guess for a factor of this prime number: "))
X = G
R = 1
while(X != 1):
    R += 1
    X = (G**R) % N
mN = int((G**(R/2)) + 1)
denom = N
E = mN % denom
while E != 0:
    mN = denom
    denom = E
    E = mN % denom
f2 = int(N/denom)
print("Your're prime numbers are " + str(f2) + " and " + str(denom))
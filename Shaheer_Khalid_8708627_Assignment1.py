#Welcome Message
print("WELCOME TO ABBY'S MERCHANDIZING 'A.M' ONLINE STORE")
print("***************************************************************************")
print("")
print("WE SELL HIGH QUALITY T-SHIRTS WITH AN INCREDIBLE PRICE OF ONLY $9.99 EACH")

#Get Colour of shirt (I'll ask for 4 different colours)
print("***************************************************************************")
print("WE HAVE A VARIETY OF COLOURS TO CHOOSE FROM")
print("Please enter 'W' for WHITE")
print("Please enter 'B' for BLUE")
print("Please enter 'O' for ORANGE")
print("Please enter 'R' for RED")
print("WHAT COLOUR WOULD YOU LIKE TO PICK TODAY ?")
colourofshirt = str(input())
#Using if statement to assign my variable a colour which could also be printed later
#keeping in mind that the user can enter small or Capital letter
if (colourofshirt == "W") or (colourofshirt == "w"):
    colourofshirt = "WHITE"
elif (colourofshirt == "B") or (colourofshirt == "b"):
    colourofshirt = "BLUE"
elif (colourofshirt == "O") or (colourofshirt == "o"):
    colourofshirt = "ORANGE"
elif (colourofshirt == "R") or (colourofshirt == "r"):
    colourofshirt = "RED"

#Get type of shirt (polo or t-shirt )
print("***************************************************************************")
print("WE OFFER TWO OPTIONS FOR OUR T-SHIRTS:")
print("1.POLO SHIRT        2.REGULAR T_SHIRT")
print("Please enter 1 for POLO SHIRT OR enter 2 for REGULAR T-SHIRT")
shirttype = float(input())

if (shirttype == 1):
    shirttype = "POLO SHIRT"
elif (shirttype == 2):
    shirttype = "REGULAR T-SHIRT"

#Get quantity of shirt
print("***************************************************************************")
print("HOW MANY SHIRTS WOULD YOU LIKE TO PURCHASE TODAY?")
shirtqty = float(input())


#Declare cost of shirt (CONSTANT)
COST = 9.99
#Calculate the total cost with HST
tax = (shirtqty * COST) * 0.13
totalcostbeftax = COST * shirtqty
totalcostafttax = (shirtqty * COST) + tax

#Print receipt/Summary of the order
#testing
print(colourofshirt)
print(shirttype)
print(shirtqty)
print(totalcostbeftax)
print(totalcostafttax)


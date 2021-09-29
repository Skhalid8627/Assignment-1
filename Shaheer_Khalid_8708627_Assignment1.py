#Welcome Message
print("WELCOME TO ABBY'S MERCHANDIZING ONLINE STORE")
print("*********************************************")
print("")
print("WE SELL HIGH QUALITY T-SHIRTS WITH AN AMAIZING PRICE OF $9.99")

#Get Colour of shirt (I'll ask for 4 different colours)
print("WE HAVE A VARIETY OF COLOURS TO CHOOSE FROM")
print("Please press 'W' for WHITE")
print("Please press 'B' for BLUE")
print("Please press 'O' for ORANGE")
print("Please press 'R' for RED")
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
print(colourofshirt)

#Get type of shirt (polo or t-shirt )

#Get quantity of shirt

#Declare cost of shirt

#Calculate the total cost with HST

#Print receipt/Summary of the order

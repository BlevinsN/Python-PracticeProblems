UserInput = raw_input()
Found = False
for x in range(0,len(UserInput)-1):
    if UserInput[x].isalnum():
        if UserInput[x] == UserInput[x+1]:
            print(UserInput[x])
            Found = True
            break
if Found == False:
    print("-1")

import random,os,time
def DiceRoll(sides):
    r=random.randint(1,sides)
    return r

def Character_Health():
    h=(DiceRoll(6)*DiceRoll(12)/2) + 10
    print("Health:",h)

def Character_Strength():
    s=(DiceRoll(6)*DiceRoll(12)/2) + 12
    print("Strength:",s)

def Character_Builder():
    name=input("Name your legend : ")
    char_type=input("Character Type (Human, Elf, Wiard, Orc) : ")
    print(name)

while True:
  print("Character Builder")
  time.sleep(1)
  os.system("clear")
  Character_Builder()
  Character_Strength()
  Character_Health()
  again = input("Again?:\n")
  if again=="No" or again=="no":
    break
  time.sleep(1)
  os.system("clear")

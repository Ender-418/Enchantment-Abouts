import time

specific_enchantments = ["Aqua Affinity", "Bane of Arthropods", "Curse of Binding",
                "Efficiency", "Fortune", "Fire Aspect", "Fire Protection", "Flame", "Frost Walker", "Infinity",
                "Knockback", "Looting", "Luck of the Sea", "Lure", "Multishot", "Power", "Projectile Protection",
                "Punch", "Quick Charge", "Respiration", "Riptide", "Sharpness", "Silk Touch", "Smite",
                "Soul Speed", "Thorns", "Channeling"]

sword_enchantments = [
    "Bane of Arthropods",
    "Fire Aspect",
    "Knockback",
    "Looting",
    "Sharpness",
    "Smite"
]

axe_enchantments = [
    "Efficiency",
    "Fortune"
]

pickaxe_enchantments = [
    "Efficiency",
    "Fortune",
    "Silk Touch"
]

trident_enchantments = [
    "Channeling",
    "Impaling",
    "Loyalty",
    "Riptide"
]

fishing_rod_enchantments = [
    "Luck of the Sea",
    "Lure"
]

helmet_enchantments = [
    "Aqua Affinity",
    "Respiration",
    "Protection",
    "Fire Protection",
    "Blast Protection",
    "Projectile Protection"
]

chestplate_enchantments = [
    "Protection",
    "Fire Protection",
    "Blast Protection",
    "Projectile Protection"
]

legging_enchantments = [
    "Protection",
    "Fire Protection",
    "Blast Protection",
    "Projectile Protection"
]

boot_enchantments = [
    "Frost Walker",
    "Riptide",
    "Respiration",
    "Protection",
    "Fire Protection",
    "Blast Protection",
    "Projectile Protection"
]

mace_enchantments = [
    "Density",
    "Breach",
    "Wind Burst"
]

universal_enchantments = ["Unbreaking", "Mending", "Curse of Vanishing"]

def attempt_enchant(item, enchantment):
    if item == "Sword":
        if enchantment in sword_enchantments or enchantment in universal_enchantments:
            print("                          Valid Enchantment!")
        else:
            print("                                                                            That enchantment is not possible to make. Please try a different one")
    elif item == "Axe":
        if enchantment in axe_enchantments or enchantment in universal_enchantments:
            print("                          Valid Enchantment!")
        else:
            print("                                                                            That enchantment is not possible to make. Please try a different one")
    elif item == "Pickaxe":
        if enchantment in pickaxe_enchantments or enchantment in universal_enchantments:
            print("                          Valid Enchantment!")
        else:
            print("                                                                            That enchantment is not possible to make. Please try a different one")
    elif item == "Hoe":
        if enchantment in axe_enchantments or enchantment in universal_enchantments:
            print("                          Valid Enchantment!")
        else:
            print("                                                                            That enchantment is not possible to make. Please try a different one")
    elif item == "Trident":
        if enchantment in trident_enchantments or enchantment in universal_enchantments:
            print("                          Valid Enchantment!")
        else:
            print("                                                                            That enchantment is not possible to make. Please try a different one")
    elif item == "Fishing rod":
        if enchantment in fishing_rod_enchantments or enchantment in universal_enchantments:
            print("                          Valid Enchantment!")
        else:
            print("                                                                            That enchantment is not possible to make. Please try a different one")
    elif item == "Helmet":
        if enchantment in helmet_enchantments or enchantment in universal_enchantments:
            print("                          Valid Enchantment!")
        else:
            print("                                                                            That enchantment is not possible to make. Please try a different one")
    elif item == "Chestplate":
        if enchantment in chestplate_enchantments or enchantment in universal_enchantments:
            print("                          Valid Enchantment!")
        else:
            print("                                                                            That enchantment is not possible to make. Please try a different one")
    elif item == "Leggings":
        if enchantment in legging_enchantments or enchantment in universal_enchantments:
            print("                          Valid Enchantment!")
        else:
            print("                                                                            That enchantment is not possible to make. Please try a different one")
    elif item == "Boots":
        if enchantment in boot_enchantments or enchantment in universal_enchantments:
            print("                          Valid Enchantment!")
        else:
            print("                                                                            That enchantment is not possible to make. Please try a different one")
    elif item == "Mace":
        if enchantment in mace_enchantments or enchantment in universal_enchantments:
            print("                          Valid Enchantment!")
        else:
            print("                                                                            That enchantment is not possible to make. Please try a different one")
    else:
        print("          Did you type correctly?      Item names must have capital first letters, & don't include materials in the name")
        
        

print("                                    WELCOME TO THE ENCHANTMENT INTRODUCTION PROGRAM                             ")

time.sleep(1)

for a in range(1):
    print("        ")

print("Learn about Minecraft Bedrock Edition enchantments right here, where enchantment compatibility is easier done than said")

for a in range(3):
    print("        ")

time.sleep(2)

print("                What do you want to know?")
time.sleep(2/3)
print("                        What enchantments do?(A)         How to get them?(B)             What you can put your enchantments on?(C)")
print("If you are finished with questioning, type Done")


# Main menu loop
main_active = True
while main_active:
    choice = input().strip().upper()

    if choice == "A":
        print("As minecraft's main in-universe magic, they allow for TOOLS & ARMOR to go above their normal states, usually in ")
        print("the form of increased power or new abilities!")
        time.sleep(1)
        print("                             Some common ones include:")
        print("                                                     Unbreaking, which makes tools more durable")
        print("                                           Protection, which makes armor better protect you")
        print("                                 Efficiency, which makes tools hit way faster")
        print()
    elif choice == "B":
        print("The easiest way to get them is to craft an ENCHANTING TABLE & use lapis lazuli (Lapis) to get random bonuses for your items.")
        time.sleep(1)
        print("            But if you want absolute control over what magical effect you get, try trading with librarian villagers for better enchantments, such as Mending.")
        print("            You can also find them in loot chests & mob drops, but this is largely irrelevant.")
        print()
    elif choice == "C":
        print("You can put UNBREAKING & MENDING enchantments on anything; armor, weapons, elytras")
        time.sleep(2)
        print("                                 But most enchantments are item-specific")
        time.sleep(3)
        print("                                 To test an enchantment's compatibility with an item, press 1")
    elif choice == "DONE":
        print("Thanks for coming for a quick & easy Q&A!")
        break
    elif choice == "1":
        # Exit main loop, user will call attempt_enchant manually after
        main_active = False
        print("                          You can now evaluate any enchantment on any item.")
        break
    else:
        print("                                                                                                 INVALID")
        print("     ")
        time.sleep(1/2)
        print("                                                          Enter one of the 3 questions listed at the top, or type Done to get back to minecraft")


# After main menu loop ends, prompt user to call attempt_enchant with arguments of their choosing
if main_active == False:
    print("                                                  Would you like to test an enchantment now? (Yes/No)")
    answer = input().strip().lower()
    if answer == "yes":
        item_input = input("Enter the item name (e.g., Sword, Helmet): ").strip()
        enchantment_input = input("Enter the enchantment to test: ").strip()
        attempt_enchant(item_input, enchantment_input)

        main_active = True

        while main_active == True:
            choice = input().strip().upper()
            if choice == "A":

                pass
            elif choice == "B":

                pass
            elif choice == "C":

                pass
            elif choice == "1":

                item_input = input("Enter the item name (e.g., Sword, Helmet): ").strip()
                enchantment_input = input("Enter the enchantment to test: ").strip()
                attempt_enchant(item_input, enchantment_input)
            else:
                print("Invalid input.")
    else:
        print("")
    
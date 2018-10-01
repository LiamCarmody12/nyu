again = True
totalshares = []
while again == True:
    tip = int(input("How much is the tip? $"))
    men = int(input("How many men were on the job? "))
    for i in range(0,men):
        per_person = int(input("Submit how many shares each person had one by one "))
        totalshares.append(per_person)
        i += 1                 
    print("There are", sum(totalshares), "total shares")
    share_amt = float(format(tip/sum(totalshares), ".2f"))
    print("Each share is worth $", share_amt, sep='')
    num = 1
    for each_item in totalshares:
        total = each_item * share_amt
        print(num, ". $", total, sep='')
        num += 1
    print("Tip successfully calculated")
    num = 1
    totalshares = []
    another = input("Calculate another tip? y or n: ")
    if another == "n":
        again = False
    elif another == "no":
        again = False
print("Thanks for using Ultra Tip Calculator 3000")
moredata = input("Would you like to enter additional data for recordkeeping? y or n: ")
if moredata == "y":
    date = input("What is today's date? mm/dd/yy ")
    hours = float(input("How many hours was today's job? "))
    feet = int(input("How many feet was the job? "))
    load_town = input("Where was the load? ")
    unload_town = input("Where was the unload? ")
    how_tough = int(input("On a scale from 1 (easy) to 5 (miserable), how was today's job? "))
    if hours < 6:
        hours_adj = "breezy"
    elif hours > 6:
        hours_adj = "whopping"
    if how_tough == 1:
        ending = "It was a good day!"
    elif how_tough == 5:
        ending = "Everyone will sleep good tonight."
    else:
        ending = "Another day, another dollar."
    print("It was", date, "and the Barr Brothers set to work. They moved", feet, end='')
    print(" feet from", load_town, "to", unload_town, "in a", hours_adj, hours, "hours. ", ending)
    file = open("file.txt", "w")
    file.write(date)
    file.write(str(hours))
    file.write(str(feet))
    file.write(load_town)
    file.write(unload_town)
    file.write(str(how_tough))
    file.close()
    file = open("file.txt", "r")
    print(file.read())
    file.close()
            

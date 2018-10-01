# how much the tip was
tip = int(input("How much is the tip? $"))

# how many men were on the job, create a list
# with each persons shares
men = int(input("How many men were on the job? "))
totalshares = []
for i in range(0,men):
    per_person = int(input("Submit how many shares each person had one by one "))
    totalshares.append(per_person)
    i += 1                 

# how many shares there are and what
# they are worth
print("There are", sum(totalshares), "total shares")
share_amt = float(format(tip/sum(totalshares), ".2f"))
print("Each share is worth $", share_amt, sep='')
num = 1

# how much each person gets
for each_item in totalshares:
    total = each_item * share_amt
    print(num, ". $", total, sep='')
    num += 1
    
    
print("Tip successfully calculated")
    

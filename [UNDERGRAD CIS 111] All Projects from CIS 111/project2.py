#Project 2 
#CIS 111
#Drew Murray
print("You are welcome to the AMC Movie Theaters. There are three categories of ticket prices based on age:\n\t1.Children (ages 2-12) costs $10.69 each\n\t2.Adults (ages 13-59) costs $13.69 each\n\t3.Seniors (ages 60+) costs $12.69 each")
print()
print("At the moment, we offer the following discounts:\n\t1.20% dicscount off Children tickets and\n\t2.30% discount off the senior ticket prices.")
print()
child1 = int(input("Enter the number of tickets to purchase for a child (ages 2-12): "))
adult1 = int(input("Enter the number of tickets to purchase for an adult (ages 13-59: "))
senior1 = int(input("Enter the number of tickets to purchase for a senior (ages 60+): "))
child_discount = (child1)*(10.69)*.20
senior_discount = senior1*12.69*.30
child_cost = 10.69 
adult_cost = 13.69
senior_cost = 12.69 
with_discount = ((child1*child_cost)-child_discount)+((senior1*senior_cost)-senior_discount)+(adult1*adult_cost)
without_discount = (child1*child_cost)+(adult1*adult_cost)+(senior1*senior_cost)
print()
print("Total ticket cost WITHOUT discount: $%.2f" %without_discount)
print("Total ticket cost WITH discount: $%.2f" %with_discount)
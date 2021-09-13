num_guests=raw_input('How many guests? ')
if num_guests.isdigit():
    print("Yay, it's a number!")
    num_guests=int(num_guests)
    print(type(num_guests))
    num_donuts=raw_input("How many donuts each? ")
    if num_donuts.isdigit():
        num_donuts=int(num_donuts)

        #calculate how many donuts you need
        donuts_needed=num_donuts*num_guests
        print("You need ",donuts_needed, "donuts")

        # Calculate the number of boxes needed.
        if (donuts_needed % 12) == 0:
            boxes = donuts_needed // 12
            print('Minimum boxes of donuts needed:', boxes)
        elif (donuts_needed % 12) != 0:
            boxes = int(donuts_needed // 12) + 1
            print('Minimum boxes of donuts needed:', boxes)

        # Calculate the donuts leftover:
        leftover = boxes * 12 - donuts_needed
        print('Donuts leftover:', leftover)

        # calculate the cost:
        if (boxes > 0) and (boxes <= 5):
            donut_cost = boxes * 8.00
            print("Donuts cost: $" + format(donut_cost,".2f"))
        elif (boxes > 5) and (boxes <= 20):
            donut_cost = boxes * 7.50
            print("Donuts cost: $" + format(donut_cost,".2f"))
        elif (boxes > 20):
            donut_cost = boxes * 6.00
            print("Donuts cost: $" + format(donut_cost,".2f"))
    else:
        print("Number of donuts needs to be numeric.")
else:
    print("Number of guests can only be numeric.")
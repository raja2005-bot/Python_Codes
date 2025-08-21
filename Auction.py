# name = input()
# bid = int(input())
# dict_item = {}
# for item in dict_item:
#     value = dict_item[name:dict_item[item]]
#     print(dict_item)





def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    max(bidding_dictionary)

    for key in bidding_dictionary:
        bid_amount = bidding_dictionary[key]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = key

    print(f"The winner is {winner} with a bid amound $ {highest_bid}")



dict_item = {}
continue_bidding = True
while continue_bidding:
    name = input()
    price = int(input("$ "))
    dict_item[name] = price
    should_continue = input("any Bidders 'Yes' or 'No'\n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(dict_item)
    elif should_continue == "yes":
        print("\n" * 20)










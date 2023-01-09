logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

flag = True
bidders = {}
while flag:
    name =  input("what's your name : ")
    bid = int(input("what's your bit : "))
    bidders[name] = bid
    print("Is there another bidder ? (y/n) (Y/N)")
    if input() in ["y","Y"] :
        flag = True
    else:
        flag = False

bidder_name = max(bidders, key=bidders.get)
max_bid ="$"+str( bidders[bidder_name])
print("The winner is ",bidder_name ,"with a bid of ",max_bid)

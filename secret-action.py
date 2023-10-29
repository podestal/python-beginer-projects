

print('Welcome to the secret auction')

auction_dict = {}
auction = True
count = 0

def get_winner(auction_dict):
    max_bid = 0
    name_max = ''
    for name in auction_dict:
        if max_bid < auction_dict[name]:
            max_bid = auction_dict[name]
            name_max = name
    return name_max

def get_info(auction_dict):
    winner_name = get_winner(auction_dict)
    winner_bid = auction_dict[winner_name]
    print('The winner is ' + winner_name + ' with a bid of $' + str(winner_bid))

while auction:
    
    user_name = input('What is your name: ')
    user_amount = int(input('What is your amount: '))
    auction_dict.update({user_name : user_amount})
    count += 1

    if count >= 2:
        quit = input('Do you want to keep the auction y/n: ')
        if quit == 'n':
            auction = False

get_info(auction_dict)
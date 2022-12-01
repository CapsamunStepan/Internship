def winner(user1, user2):
    if (user1 == 'rock' and user2 == 'scissors') \
            or (user1 == 'scissors' and user2 == 'paper') \
            or (user1 == 'paper' and user2 == 'rock'):
        return True
    else:
        return False


condition = 'yes'
while condition == 'yes':
    player1 = input("Player1, enter 'rock', 'paper' or 'scissors': ")
    player2 = input("Player2, enter 'rock', 'paper' or 'scissors': ")
    if player1 == player2:
        print('Draw!')
    elif winner(player1, player2):
        print("Congratulations to the Player1!")
    elif winner(player2, player1):
        print("Congratulations to the Player2!")
    else:
        print("Incorrect input!!!")
    condition = input("Wanna start a new game? [yes/not] ")

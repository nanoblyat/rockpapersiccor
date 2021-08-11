import random, sys

print('ROCK , PAPER, SCISSORS')

wins = 0
ties = 0
losses = 0

# choose what to display

while True:
    print(f'{wins} wins, {losses} losses, {ties} ties')

    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        elif playerMove == 'q':
            sys.exit()

        else:
            print('Write either "r" for rock "p" for paper" or "s" for scissors- like... are u dumb')

    # players input

    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # computers input
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    # what's gonna happen aka grand finale aka wagwgowngwognsnsj

    if playerMove == computerMove:
        print('Tie')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose')
        losses = losses + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win')
        wins = wins + 1

    else:
        print('Write either "r" for rock "p" for paper" or "s" for scissors')


import random

# Get user input
stake  = int(input("stake="))
goal   = int(input("goal="))
trials = int(input("trials="))

# Run trialCount experiments that start with stake and terminate on
# 0 or goal.
bets = 0
wins = 0
for t in range(trials):
    # Run one experiment.
    cash = stake
    while cash > 0 and cash < goal:
        # Simulate one bet.
        bets += 1
        if random.random() < 0.50:
            cash += 1
        else:
            cash -= 1
    if cash == goal:
        wins += 1

print("-------- Results ---------")
print('Win ratio:'+str(wins/trials))
print('Avg # bets per trial: ' + str(bets//trials))

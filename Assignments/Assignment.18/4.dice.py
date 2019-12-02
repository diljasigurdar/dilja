import random
# The implementation of Dice goes here

class Dice():
    def __init__(self, max_value):
        self.__max = max_value
        self.__value = 0
    
    def __str__(self):
        return "{}".format(self.__value)

    def roll(self):
        self.__value = random.randint(1, self.__max)
    
    def __add__(self, dice2):
        result = Dice(self.__max + self.__value)
        result.__value = self.__value + dice2.__value
        return result

def run_dice_experiment():
    dice1 = Dice(6)
    dice2 = Dice(6)
    for _ in range(0,10):
        dice1.roll()
        dice2.roll()
        sum_dice = dice1 + dice2
        print("dice1: {}, dice2: {}, sum dice: {}".format(str(dice1), str(dice2), str(sum_dice)))
        sum_dice.roll()
        print("sum dice: {}".format(str(sum_dice)))

# Main program starts here
seed_number = int(input("Enter a seed: "))
random.seed(seed_number)
run_dice_experiment()
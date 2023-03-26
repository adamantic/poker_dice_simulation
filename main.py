from random import randint
from random import seed

seed(0)

def play():
    mapping = {0: 'Ace', 1: 'King', 2: 'Queen', 3: 'Jack', 4: '10', 5: '9'}
    reverse_mapping = {'Ace': 0, 'King': 1, 'Queen': 2, 'Jack': 3, '10': 4, '9': 5}

    def roll_dice_ints(n):
        return sorted([randint(0, 5) for _ in range(n)])

    def print_dice(dice):
        dice_string = ' '.join(mapping[die] for die in dice)
        return dice_string

    def evaluate_hand(dice):
        counts = [dice.count(die) for die in set(dice)]

        if 5 in counts:
            return "Five of a kind"
        if 4 in counts:
            return "Four of a kind"
        if 3 in counts and 2 in counts:
            return "Full house"
        if 3 in counts:
            return "Three of a kind"
        if counts.count(2) == 2:
            return "Two pair"
        if counts.count(2) == 1 and 3 not in counts and 4 not in counts and 5 not in counts:
            return "One pair"
        else:
            return 'It is a Bust'

    rolls_left = 3
    dice_numbers = roll_dice_ints(5)
    dice_string = print_dice(dice_numbers)
    print("The roll is:", dice_string)
    print("It is a", evaluate_hand(dice_numbers))

    # SECOND ROLL
    while rolls_left > 1:
        kept_dice_str = input("Which dice do you want to keep for the second roll? ")

        if kept_dice_str.lower() == "all":
            print("Ok, done.")
            break
        # check if the input has all the components in dice_string, if so print "Ok, done.
        if sorted(kept_dice_str.split()) == sorted(dice_string.split()):
            print("Ok, done.")
            break
        else:
            # check if kept_dice_str is correct
            input_check_str = kept_dice_str.split()
            original_dice_string = dice_string.split()

            is_valid_input = all(item in original_dice_string for item in input_check_str)

            if not is_valid_input:
                print("That is not possible, try again!")
            else:
                kept_dice_ints = [reverse_mapping[die] for die in kept_dice_str.split()]
                number_of_new_dice = 5 - len(kept_dice_ints)
                new_dice = roll_dice_ints(number_of_new_dice)
                combined_dice = sorted(kept_dice_ints + new_dice)
                dice_string = print_dice(combined_dice)
                print("The roll is:", dice_string)
                print("It is a", evaluate_hand(combined_dice))
                rolls_left -= 1

        #THIRD ROLL
        if rolls_left == 2:
            kept_dice_str = input("Which dice do you want to keep for the third roll? ")

            if kept_dice_str.lower() == "all":
                print("Ok, done.")
                break
            # check if the input has all the components in dice_string, if so print "Ok, done.
            if sorted(kept_dice_str.split()) == sorted(dice_string.split()):
                print("Ok, done.")
                break
            else:
                # check if kept_dice_str is correct
                input_check_str = kept_dice_str.split()
                original_dice_string = dice_string.split()

                is_valid_input = all(item in original_dice_string for item in input_check_str)

                if not is_valid_input:
                    print("That is not possible, try again!")
                else:
                    kept_dice_ints = [reverse_mapping[die] for die in kept_dice_str.split()]
                    number_of_new_dice = 5 - len(kept_dice_ints)
                    new_dice = roll_dice_ints(number_of_new_dice)
                    combined_dice = sorted(kept_dice_ints + new_dice)
                    dice_string = print_dice(combined_dice)
                    print("The roll is:", dice_string)
                    print("It is a", evaluate_hand(combined_dice))
            rolls_left = 1

def simulate(n):
    n_copy = n
    mapping = {0: 'Ace', 1: 'King', 2: 'Queen', 3: 'Jack', 4: '10', 5: '9'}
    reverse_mapping = {'Ace': 0, 'King': 1, 'Queen': 2, 'Jack': 3, '10': 4, '9': 5}

    def roll_dice_ints(n):
        return sorted([randint(0, 5) for _ in range(n)])

    def print_dice(dice):
        dice_string = ' '.join(mapping[die] for die in dice)
        return dice_string

    def evaluate_hand(dice):
        counts = [dice.count(die) for die in set(dice)]

        # Check for a straight
        if sorted(dice) == [0, 1, 2, 3, 4] or sorted(dice) == [1, 2, 3, 4, 5]:
            return "Straight"

        if 5 in counts:
            return "Five of a kind"
        if 4 in counts:
            return "Four of a kind"
        if 3 in counts and 2 in counts:
            return "Full house"
        if 3 in counts:
            return "Three of a kind"
        if counts.count(2) == 2:
            return "Two pair"
        if counts.count(2) == 1 and 3 not in counts and 4 not in counts and 5 not in counts:
            return "One pair"
        else:
            return 'It is a Bust'

    five_of_a_kind = 0
    four_of_a_kind = 0
    full_house = 0
    straight = 0
    three_of_a_kind = 0
    two_pair = 0
    one_pair = 0
    busts = 0

    while n > 0:
        hand_str = roll_dice_ints(5)
        print_dice(hand_str)
        evaluate_hand(hand_str)
        if evaluate_hand(hand_str) == "Five of a kind":
            five_of_a_kind += 1
        if evaluate_hand(hand_str) == "Four of a kind":
            four_of_a_kind += 1
        if evaluate_hand(hand_str) == "Full house":
            full_house += 1
        if evaluate_hand(hand_str) == "Straight":
            straight += 1
        if evaluate_hand(hand_str) == "Three of a kind":
            three_of_a_kind += 1
        if evaluate_hand(hand_str) == "Two pair":
            two_pair += 1
        if evaluate_hand(hand_str) == "One pair":
            one_pair += 1
        if evaluate_hand(hand_str) == "It is a Bust":
            busts += 1

        n -= 1

    five_of_a_kind_p = five_of_a_kind / n_copy * 100
    four_of_a_kind_p = four_of_a_kind / n_copy * 100
    full_house_p = full_house / n_copy * 100
    straight_p = straight / n_copy * 100
    three_of_a_kind_p = three_of_a_kind / n_copy * 100
    two_pair_p = two_pair / n_copy * 100
    one_pair_p = one_pair / n_copy * 100

    # Output the results
    print(f"Five of a kind: {five_of_a_kind_p:.2f}%")
    print(f"Four of a kind: {four_of_a_kind_p:.2f}%")
    print(f"Full house: {full_house_p:.2f}%")
    print(f"Straight: {straight_p:.2f}%")
    print(f"Three of a kind: {three_of_a_kind_p:.2f}%")
    print(f"Two pair: {two_pair_p:.2f}%")
    print(f"One pair: {one_pair_p:.2f}%")


simulate(1000)




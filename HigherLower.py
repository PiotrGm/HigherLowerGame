from data import data
import asciiart
import random
import os
import time


def main():
    score = 0

    def random_dictionary(data):
        num = random.randint(0, len(data) - 1)
        value = int(data[num]['follower_count'])
        compare = (f"{data[num]['name']}, a {data[num]['description']}, from {data[num]['country']}")
        return compare, value
    
    compare_last = random_dictionary(data)
    while True:
        compare_A = compare_last
        compare_B = random_dictionary(data)
        os.system('cls' if os.name == "nt" else 'clear')
        print(asciiart.logo)
        print(f'Your score: {score}\n')
        print(compare_A[0])
        print(asciiart.vs)
        print(compare_B[0])
        try:
            choice = input('\nWhich one has more followers? Type "A" or "B"\n').lower()
            if choice == "a":
                compare_last = compare_A
                second_choice = compare_B
            elif choice == 'b':
                compare_last = compare_B
                second_choice = compare_A

            if compare_last[1] > second_choice[1]:
                score += 1
            elif compare_last[1] < second_choice[1]:
                print(f"Sorry, the correct answer is {compare_B[0]}")
                break
            else:
                score += 1
        except:
            print("Invalid input.")
            time.sleep(3)

main()

while True:
    choice = input("Do you want to try again? Type 'y' or 'n'").lower()
    if choice == "y":
        main()
    elif choice == "n":
        print("Ok, bye bye.")
        break
    else:
        print("Invalid input. Try again.")

# The easy empty fill-in-the-blank and its corresponding answers.
easy_ques = ["Two balls and two", "___1___", "on him. Here's the pitch on the "
            "way. A swing and a belt! Left field...way back...BLUE JAYS WIN "
            "IT! The Blue Jays are", "___2___", "Series Champions, as Joe",
            "___3___", "hits a three-run home run in the ninth", "___4___",
            "and the Blue Jays have repeated as World Series Champions!",
            "___5___", "'em all, Joe! You'll never hit a bigger home run in "
            "your life!"]
easy_ans = ["strikes", "World", "Carter", "inning", "Touch"]

# The medium empty fill-in-the-blank and its corresponding answers.
med_ques = ["1 and 1 on Jose. All eyes on the mound and the bearded Sam",
              "___1___", ". Now he comes set. Kicks, the 1-1 pitch. FLY BALL, "
              "DEEP", "___2___", "FIELD! YES SIR!", "___3___", "!", "___4___",
              "!", "___5___", "! Blue Jays 6,", "___6___", "3. Jose",
              "___7___", "is unbelievable!"]
med_ans = ["Dyson", "LEFT", "THERE", "SHE", "GOES", "Rangers",
                  "Bautista"]

# The hard empty fill-in-the-blank and its corresponding answers.
hard_ques = ["Deux balles deux prises a Russell", "___1___", "et voila le "
            "signal de", "___2___", ". La balle est frappee avec force au "
            "champ gauche et...ELLE EST", "___3___", "!", "___4___", "!",
            "___5___", "!", "___6___", "!", "___7___", "! Le Quebec danse! Le",
            "___8___", "danse! Et RUSSELLLLL quel chef d'orchestre. Bonsoir, "
            "elle est partie."]
hard_ans = ["Martin", "McCann", "PARTIE", "RUSSELL", "RUSSELL", "RUSSELL",
                "RUSSELL", "Canada"]
def ask_for_level():
    """Ask the user to choose the difficulty level."""
    level = input("\nPlease select the difficulty")
    if level.lower() == "easy":
        return easy_ques, easy_ans, "easy"
    elif level.lower() == "medium":
        return med_ques, med_ans, "medium"
    elif level.lower() == "hard":
        return hard_ques, hard_ans, "hard"
    else:
        print ("Please select a valid difficulty level")
        return ask_for_level()

def set_punc(fib_string):
    """Remove spaces before punctuation marks"""
    fib_string = fib_string.replace(" .", ".")
    fib_string = fib_string.replace(" !", "!")
    return fib_string

def links(level):
    if level == "easy":
        return "https://www.youtube.com/watch?v=-F5HwiGm7lg"
    if level == "medium":
        return "https://www.youtube.com/watch?v=Oc-LYFojWcw"
    if level == "hard":
        return ("http://bit.ly/russell-martins-hr-was-the-biggest-since-1993 "
                "(starts at 4:40)")

def check(blank_number, fib, answers, answer):
    """Asks the user for a guess. If correct, moves to the next blank.

    Prompts the user to fill in the first blank. Displays the updated
    fill-in-the-blank when the user inputs the correct answer and prompts them
    to fill in the next blank. Prompts the user to try again when their guess
    is incorrect."""
    blank = "___" + str(blank_number) + "___"
    guess = input("Please fill in blank #" + str(blank_number) +
                      " (case-sensitive): ")
    if guess == answer:
        fib[fib.index(blank)] = answer
        print (set_punc(" ".join(fib)) + "\n")
        blank_number += 1
        return blank_number
    else:
        print ("Incorrect. Please try again.\n")
        return check(blank_number, fib, answers, answer)

def main():
    """Start the game"""
    fib, answers, level = ask_for_level()
    print ("\nHere is the fill-in-the-blank for the " + level + " difficulty "
           "level:")
    print (set_punc(" ".join(fib)) + "\n")

    blank_number = 1
    for answer in answers:
        blank_number = check(blank_number, fib, answers, answer)

    print ("Congratulations, you have filled in all of the blanks! Here is the"
           " link to the call:")
    print (links(level) + "\n")

main()

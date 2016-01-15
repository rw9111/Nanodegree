# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/
easy_quiz = "The structure of an ___1___ statement is: the keyword, ___1___, followed by a comparison, we'll call that the ___2___ expression, followed by a ___3___.  And then, inside the ___1___, we have the ___4___, and the ___4___ is the code that will run when the ___2___ expression is True. If the ___2___ expression doesn't evaluate to True, then the ___3___ doesn't execute."
easy_answers = ['if', 'test', 'colon', 'block'] 


medium_quiz = "The way to introduce a ___1___ is using an assignment statement. And an assignment statement looks like this. We have a ___2___, followed by an ___3___ symbol, followed by an ___4___. After the assignment statement, the name that was on the left side refers to the value that the expression has. The name can be any sequence of ___5___ and ___6___, as well as ___7___, as long as it starts with a letter or an underscore."
medium_answers = ['variable', 'name', 'equal', 'expression', 'letters', 'numbers', 'underscores'] 


hard_quiz = "The structure of a ___1___ loop is the keyword ___2___ followed by a name, which is a ___3___ that can be used for later, then the keyword ___4___ followed by a ___5___, and this can be any expression which evaluates to a ___5___ followed by a colon.  This is similar to the structure of a ___6___ loop and an ___7___ statement with a block inside the ___2___.  A ___1___ means for each element in the ___5___ the program is going to assign that element to the name and evaluate the ___8___.  It goes through each element in the ___5___ in order."
hard_answers = ['for', 'for', 'variable', 'in', 'list', 'while', 'if', 'block', '', '']


def output(qname, current_quiz, answer_replace, attempts_left, max_trys):
    """Prompts the user for answers and if they are correct or not and how many guesses left if the user guesses wrong."""
    prompt = '\nBelow is the %s quiz:\n\n%s' % (qname, current_quiz)
    prompt += '\n\nWhat is you answer for %s? ' % answer_replace
    if attempts_left == max_trys:
        return prompt
    new_prompt = "\n\nThat isn't the correct answer!  "
    if attempts_left > 1:
        new_prompt += "Let's try again; you have %s trys left!\n\n" % attempts_left
    else:
        new_prompt += 'You only have %s try left!  Make it count!\n\n' % attempts_left
    return new_prompt + prompt




def ask_question(qname, quiz, blank_num, answer, max_trys):
    """Takes the current quiz, and answer.  Returns the partially answered quiz 
    and the number of the next answer blank."""
    attempts_left = max_trys
    answer_replace = '__' + str(blank_num) + '__'
    """Displays quiz with all blanks.  Returns prompt Asking for answer for the first blank number."""
    prompt = output(qname, quiz, answer_replace, attempts_left, max_trys)
    user_guess = raw_input(prompt)
    """If user guess is wrong outputs the quiz and try again and displays number of tries left.  Decreases number or tries by 1"""
    while user_guess != answer and attempts_left > 1:
        attempts_left = attempts_left - 1
        prompt = output(qname, quiz, answer_replace, attempts_left, max_trys)
        user_guess = raw_input(prompt)
    """if user guess is correct lets user know its correct and displays quiz with correct answer filled in and goes on to the next blank number."""   
    if user_guess == answer and attempts_left > 0:
        print '\nCorrect!\n'
        return (quiz.replace(answer_replace, answer), blank_num + 1)
    else:
        return (None, blank_num + 1)




def get_quiz_and_answers(difficulty):
    """Takes a difficulty (1, 2, 3) and Returns the quiz name, quiz string and answers list"""
    if difficulty == '1':
        return ("easy", easy_quiz, easy_answers)
    if difficulty == '2':
        return ("medium", medium_quiz, medium_answers)
    if difficulty == '3':
        return ("hard", hard_quiz, hard_answers)
    else:
        return ("Error", "Try Again")
      
    

def select_game_difficulty():
    """Choose a game difficulty.  Stays in loop until a valid input is selected.  Either 1, 2, or 3"""
    print "Enter a quiz difficulty. Choose (1, 2, or 3): "
    while True:
        """User selects quiz dificulty.  Only allows to choose 1,2 or 3 """
        user_input = raw_input("(1) Easy, (2) Medium, (3) Hard: ")
        if user_input in ['1','2','3']:
            break
    print "\nYou get 3 trys to get each answer correct.\n"
    return user_input



def play_game():
    """Starts the quiz game.  Selects the difficulty and then shows the quiz
    associated with the diffeculty selected."""
    difficulty = select_game_difficulty()
    """Returns the quiz name, the quiz with blanks and the quiz answers"""
    qname, quiz, answers = get_quiz_and_answers(difficulty)
    max_guesses = 3
    answer_number = 1
    while answer_number <= len(answers):
        """Returns the quiz with correct answers filled in"""
        quiz, answer_number = ask_question(qname, quiz, answer_number, answers[answer_number - 1], max_guesses)
        if quiz is None:
            print "Game over!  You took many guesses!"
            return False
    print quiz + '\n\nGreat!  You got them all correct!\n'
    return True

play_game()  

print('Hello and Welcome my Quiz!')
play = input('Would you like to take part in my quiz? (yes/no): ')
if play.lower() != 'yes':
    print('Okay, maybe next time.')
    quit()
else:
    print('Okay let\'s play!')
    score = 0

# formatting for the output design of the question
def question_format(question):
    print('='*53)
    print(f'|{question:^51s}|')
    print('='*53)

# formatting for the output design of the answers
def answer_format():
    answers = ['A: 4', 'B: 3', 'C: 2', 'D: 1']
    print(f'|{answers[0]:^12s}|{answers[1]:^12s}|{answers[2]:^12s}|{answers[3]:^12s}|')
    print('-'*53)
  
# QUESTION_1    
question_format('What is 1 + 1 = ?')
answer_format()
answer_input = input('Type A, B, C, or D: ') # thinking of how to make this a function to lower the duplication
if answer_input.upper() != 'C':
    print('That is incorrect :(, next question!')
else:
    print('That is correct :), next question!')
    score += 1

# QUESTION_2        
question_format('What is 100 / 50 = ?')
answer_format()
answer_input = input('Type A, B, C, or D: ') # thinking of how to make this a function to lower the duplication
if answer_input.upper() != 'C':
    print('That is incorrect :(, next question!')
else:
    print('That is correct :), next question!')
    score += 1

# QUESTION_3        
question_format('Binary is a base system of?')
answer_format()
answer_input = input('Type A, B, C, or D: ') # thinking of how to make this a function to lower the duplication
if answer_input.upper() != 'C':
    print('That is incorrect :(, next question!')
else:
    print('That is correct :), next question!')
    score += 1

# QUESTION_4        
question_format('A motorbike has how many wheels?')
answer_format()
answer_input = input('Type A, B, C, or D: ') # thinking of how to make this a function to lower the duplication
if answer_input.upper() != 'C':
    print('That is incorrect :(, next question!')
else:
    print('That is correct :), next question!')
    score += 1

# QUESTION_5
question_format('What does \'zwei\' mean?')
answer_format()
answer_input = input('Type A, B, C, or D: ') # thinking of how to make this a function to lower the duplication
if answer_input.upper() != 'C':
    print('You have completed the quiz!')
else:
    print('You have completed the quiz!')
    score += 1

# RESULT
score_in_percentage = (score/5)*100 # converting score into a percentage
last_message = 'You scored ' + str(score_in_percentage) + '% well done!'
question_format(last_message)

# after adding some functions i managed to reduce the number of lines
# previously 96 now only 76
# but i still have a few duplications but still figuring out how to make it a function


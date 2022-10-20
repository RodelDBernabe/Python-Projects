print('Hello and Welcome my Quiz!')
play = input('Would you like to take part in my quiz? (yes/no): ')
if play.lower() != 'yes':
    print('Okay come back when you\'re ready.')
    quit()

print('Okay let\'s play!')
score = 0

# QUESTION_1
question = 'What is 1 + 1 = ?'
q_heading = f'|{question:^51s}|'
print('='*53)
print(q_heading)
print('='*53)
answers = ['A: 4', 'B: 3', 'C: 2', 'D: 1']
print(f'|{answers[0]:^12s}|{answers[1]:^12s}|{answers[2]:^12s}|{answers[3]:^12s}|')
print('-'*53)
answer_input = input('Type A, B, C, or D: ')
if answer_input.upper() != 'C':
    print('That is incorrect :(, next question!')
else:
    print('That is correct :), next question!')
    score += 1

# QUESTION_2
question = 'What is 100 / 50 = ?'
q_heading = f'|{question:^51s}|'
print('='*53)
print(q_heading)
print('='*53)
answers = ['A: 4', 'B: 3', 'C: 2', 'D: 1']
print(f'|{answers[0]:^12s}|{answers[1]:^12s}|{answers[2]:^12s}|{answers[3]:^12s}|')
print('-'*53)
answer_input = input('Type A, B, C, or D: ')
if answer_input.upper() != 'C':
    print('That is incorrect :(, next question!')
else:
    print('That is correct :), next question!')
    score += 1

# QUESTION_3
question = 'Binary is a base system of?'
q_heading = f'|{question:^51s}|'
print('='*53)
print(q_heading)
print('='*53)
answers = ['A: 4', 'B: 3', 'C: 2', 'D: 1']
print(f'|{answers[0]:^12s}|{answers[1]:^12s}|{answers[2]:^12s}|{answers[3]:^12s}|')
print('-'*53)
answer_input = input('Type A, B, C, or D: ')
if answer_input.upper() != 'C':
    print('That is incorrect :(, next question!')
else:
    print('That is correct :), next question!')
    score += 1

# QUESTION_4
question = 'A motorbike has how many wheels?'
q_heading = f'|{question:^51s}|'
print('='*53)
print(q_heading)
print('='*53)
answers = ['A: 4', 'B: 3', 'C: 2', 'D: 1']
print(f'|{answers[0]:^12s}|{answers[1]:^12s}|{answers[2]:^12s}|{answers[3]:^12s}|')
print('-'*53)
answer_input = input('Type A, B, C, or D: ')
if answer_input.upper() != 'C':
    print('That is incorrect :(, next question!')
else:
    print('That is correct :), next question!')
    score += 1

# QUESTION_5   
question = 'What does \'zwei\' mean?'
q_heading = f'|{question:^51s}|'
print('='*53)
print(q_heading)
print('='*53)
answers = ['A: 4', 'B: 3', 'C: 2', 'D: 1']
print(f'|{answers[0]:^12s}|{answers[1]:^12s}|{answers[2]:^12s}|{answers[3]:^12s}|')
print('-'*53)
answer_input = input('Type A, B, C, or D: ')
if answer_input.upper() != 'C':
    print('You have completed the quiz!')
else:
    print('You have completed the quiz!')
    score += 1

# RESULT
score_in_percentage = (score/5)*100
last_message = 'You scored ' + str(score_in_percentage) + '% well done!'
print('='*53)
print(f'|{last_message:^51}|')
print('='*53)

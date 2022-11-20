import json
import random
import sys

f = open('asd.json')
data = json.load(f)

file = open('filename.txt', 'w')

sys.stdout = file # Change the standard output to the file we created.

for i in data['results']:
    if i['type'] == 'multiple':
        question = i['question']
        answer = i['correct_answer']
        posible_answers = i['incorrect_answers']
        posible_answers.append(answer)
        random.shuffle(posible_answers)
        original_stdout = sys.stdout # Save a reference to the original standard output
        pos = 0

        for j in range(len(posible_answers)):
            if posible_answers[j] == answer:
                pos = j

        print('qalternatives = ["{}","{}","{}","{}"]'.format(posible_answers[0],posible_answers[1],posible_answers[2],posible_answers[3]))
        print('m2.alt_questions.append(Question(question="{}",'.format(question))
        print('                                      answer={},'.format(pos))
        print('                                      alternatives=qalternatives))')
        print()
            
sys.stdout = original_stdout # Reset the standard output to its original value
file.close()  
f.close()
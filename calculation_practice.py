import time
from random import randint

ones = [6,7,8,9]

def form_digit(n):
    '''returns an n digit number'''
    ans = 0
    for i in range(n):
        if i == 0:
            ans+=ones[randint(0,3)]
            continue
        ans += randint(1,9)*pow(10,i)
    return ans

def form_ques(s):
    '''return a List of digits to multiply'''
    ans = []
    for i in s:
        ans.append(form_digit(int(i)))
    return ans
    

def main():
    t = int(input('Provide How many ques you want: '))
    s = input('What digit numbers type 3,3 for 3 digit into 3 digit: ')
    s = s.split(',')
    ques = []

    for i in range(t):
        ques.append(form_ques(s))
    
    answers = []
    index = 0

    start = time.time()
    for i in ques:
        index+=1
        print(f'{index}. {i[0]} X {i[1]}')
        answers.append(i[0]*i[1])

    input('Press Enter to show the answers')
    end = time.time()

    for i in range(len(answers)):
        print(f'{i+1}. {answers[i]}')

    print(f'Time Taken is {round(end-start,2)} seconds')

if __name__=='__main__':
    main()

    

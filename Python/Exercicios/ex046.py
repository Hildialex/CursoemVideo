from time import sleep
import emoji
print('\033[4;31mCONTAGEM REGRESSIVA\033[m')
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print('{} \033[33mESTOUROU\033[m {}'.format(emoji.emojize(':boom:'),emoji.emojize(':boom:')))
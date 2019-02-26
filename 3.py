## import modules here 
from math import log, exp
################# Question 1 #################
def multinomial_nb(training_data, sms):# do not change the heading of the function
    #  **replace** this line with your code
    if len(training_data)==0:
        return
    def _count(subsms,hamorspam):
        L=[]
        count=0
        for i in training_data:
            if i[1]==hamorspam:
                L.append(i[0])
        for i in L:
            if subsms in i:
                count+=i[subsms]
        return count

    ham_num = 0
    spam_num = 0
    for i in training_data:
        if i[-1] == 'ham':
            for j in i[0]:
                ham_num += i[0][j]
        else:
            for j in i[0]:
                spam_num += i[0][j]
    #print(ham_num)
    #print(spam_num)
    num_tol = len(set([v for msss in training_data for v in msss[0].keys()]))
    #print('num_tol', num_tol)
    voc = set([v for msss in training_data for v in msss[0].keys()])
    #print(voc)

    Lham = 0
    Lspam = 0

    for i in sms:
        if i not in voc:
            continue
        word_ham = _count(i,'ham')
        #word_total = 0
        #word_ham = 0
        #word_spam = 0
        # print(i)
        #for j in training_data:
            #if i in j[0]:
                #word_total += j[0][i]
                #if j[-1] == 'ham':
                  #  word_ham += 1
                #else:
                    #word_spam += 1
        #print(word_total, word_spam, word_ham)
        pham = (word_ham + 1) / (ham_num + num_tol)
        Lham+=log(pham)
        word_spam = _count(i,'spam')

        pspam = (word_spam + 1) / (spam_num + num_tol)
        Lspam+=log(pspam)
        #print(p_token_in_ham)
        #print(p_token_in_spam)
        #Lham.append(p_token_in_ham)
        #Lspam.append(p_token_in_spam)
    #print(Lspam, Lham)
    #print(pham)
    #print(pspam)
    numham = 0
    numspam = 0
    for i in training_data:
        #print(i[-1])
        if i[1] == 'spam':
            numspam += 1
    #print(numspam, numham)
    pnumspam = numspam / len(training_data)
    #print(pnumspam)
    #pnumham = numham / len(training_data)
    #print(pnumham)
    # print(training_data)
    # print (len(training_data))
    # print(training_data[0][0])
    s = exp((log(pnumspam)+Lspam)-(log(1-pnumspam)+Lham))
    return s
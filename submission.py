import helper
import math
import numpy as np
import string
def fool_classifier(test_data): ## Please do not change the function defination...
    ## Read the test data file, i.e., 'test_data.txt' from Present Working Directory...
    ## You are supposed to use pre-defined class: 'strategy()' in the file `helper.py` for model training (if any),
    #  and modifications limit checking
    strategy_instance=helper.strategy() 

    parameters = {}

    parameters['gamma'] = 'auto'
    parameters['C'] = 1.0
    parameters['kernel'] = 'linear'
    parameters['degree'] = 3
    parameters['coef0'] = 0.0

    def _counter(data):
        tokens = {}
        for token in data:
            for e in token:

                if e not in tokens:
                    tokens[e] = 1
                else:
                    tokens[e] += 1
        return tokens

    def _counteridf (data,sss):
        tokens = {}
        for token in data:
            for i in sss :
                if token in i :
                    if token not in tokens:
                        tokens[token] =1
                    else:
                        tokens[token] +=1
        #print(tokens)
        return tokens
    def _tf(word,voc,lenlenvoc):
        sumwordinsample = 0
        for i in voc:
            for j in i:
                if j == word:
                    sumwordinsample +=1
        #print(sumwordinsample)
        tf = sumwordinsample / lenlenvoc
        return tf

    #def idf ():
    def _idf (word ,voc):
        sumwordinsample = 0
        for i in voc:
            if word in i:
                sumwordinsample+=1
        #print(sumwordinsample)
        idf = math.log(len(sss)/(1+sumwordinsample))
        return idf

    def transfer_np (idf_vector):
        idf_ = np.zeros((len(idf_vector),len(idf_vector)))
        np.fill_diagonal(idf_,idf_vector)
        return  idf_


    sss = strategy_instance.class0+strategy_instance.class1
    sss0 = strategy_instance.class0
    #print(len(sss0))
    sss1 = strategy_instance.class1
    #print(len(sss1))
    #print(sss)
    sss0_dict = _counter(sss0)
    sss0idf_dict = _counteridf(sss0_dict,sss0)
    #print(sss0idf_dict)
    #print(sss0_dict)
    lenlenvoc0 = 0
    for i in sss0:
        for j in i :
            lenlenvoc0+=1
    #print(lenlenvoc0)

    sss1_dict = _counter(sss1)
    sss1idf_dict = _counteridf(sss1_dict,sss1)
    #print(sss1idf_dict)
    #print(sss1_dict)
    lenlenvoc1 = 0
    for i in sss1:
        for j in i :
            lenlenvoc1+=1
    #print(lenlenvoc1)
    L0 = {}
    LL0 =[]
    for i in sss0_dict:
        tf0 = sss0_dict[i]/lenlenvoc0
        idf0 = math.log((len(sss0))/(sss0idf_dict[i]+1))
        tf_idf0 =  tf0*idf0
        #LL0.append((i,tf_idf0))
        L0[i]=tf_idf0
    #print(L0)
    #print(LL0)
    #LL0_sort = sorted(LL0, key=lambda s: (s[1]), reverse=True)
    #print(LL0_sort)
    #print (';;;;;;;')
    L1 = {}
    LL1= []
    for i in sss1_dict:
        tf1 = sss1_dict[i]/lenlenvoc1
        idf1 = math.log((len(sss1))/(sss1idf_dict[i]+1))
        tf_idf1 =  tf1*idf1
        #LL1.append((i,tf_idf1))
        L1[i]=tf_idf1
    #print(L1)
    #print(LL1)
    #LL1_sort = sorted(LL1, key=lambda s: (s[1]), reverse=True)
    #print(LL1_sort)


    x_train = []
    x_train_lie= []
    for i in sss:
        for j in i :
            x_train_lie.append(j)
    #print(x_train_lie)
    #print(len(set(x_train_lie)))
    x_train.append(list(set(x_train_lie)))
    #print(x_train)
    #print(x_train[0].index('artillery'))
    for i in sss:
        x_train.append([0 for x in range (len(set(x_train_lie)))])
    for sample in range(len(sss)):
        if sample<=len(sss0):
            for word in sss[sample]:
                if word not in L0:
                    pass
                else:
                    x_train[sample+1][x_train[0].index(word)] = L0[word]
        else:
            for word in sss[sample]:
                if word not in L1:
                    pass
                else:
                    x_train[sample+1][x_train[0].index(word)] = L1[word]



    #def normalizer(vec):
     #   denom = np.sum([el ** 2 for el in vec])
      #  return [(el / math.sqrt(denom)) for el in vec]

    nom = []

    #print (x_train)
    L_head = x_train.pop(0)

    #for vec in x_train:
     #   nom.append(normalizer(vec))

    a = np.matrix(x_train)
    #print(type(a))

    y_train = ["class 0" for _ in range(len(sss0))] + ["class 1" for _ in range(len(sss1))]
    model = strategy_instance.train_svm(parameters, a, y_train)
    #print (len(model.coef_))
    coef = model.coef_[0]
    #coef111= model.coef0
    #print(model.coef0)

    more1=[]
    more0=[]
    for i in range(len(L_head)):
        if coef[i]==0:
            continue
        if coef[i]>0:
            more1.append((L_head[i],coef[i]))
        else:
            more0.append((L_head[i], coef[i]))
    #print(more0)
    #print(more1)
    LL0_sort = sorted(more0, key=lambda s: (s[1]), reverse=True)
    LL1_sort = sorted(more1, key=lambda s: (s[1]), reverse=True)
    #print(LL0_sort)
    #print(LL1_sort)
    LL0_feature =[]
    for i in LL0_sort:
        LL0_feature.append(i[0])
    LL1_feature =[]
    for i in LL1_sort:
        LL1_feature.append(i[0])
    #print(LL0_feature)
    #print(LL1_feature)
     #L_more_0 = [i for i in ]
    with open (test_data,'r') as file:
        testContent = [line.strip().split(' ') for line in file]

    biaodian = string.punctuation

    data = ''
    for i in range(len(testContent)):

        testContent_set =set(testContent[i])
        test_set_inter = testContent_set.intersection(set(LL1_feature))
        #print(test_set_inter)
        #print()
        test_set_inter1_sort = sorted(test_set_inter,key=lambda s:LL1_feature.index(s))
        #print(len(test_set_inter1_sort))
        #test_set_inter0 = set(LL0_feature).intersection(testContent_set)
        waiting = set(LL0_feature)-testContent_set
        waiting_sort = sorted(waiting,key=lambda s:LL0_feature.index(s))
        #print(waiting_sort)
        #print(waiting_sort)
        change_count = 0
        for k in test_set_inter1_sort:
            testContent_set.remove(k)
            change_count+=1
            if change_count==20:
                break
        while change_count<20:
            addword = waiting_sort.pop()
            testContent_set.add(addword)
            change_count+=1

        data += ' '.join(testContent_set)+'\n'

    #print(data)

    with open('modified_data.txt', 'w') as file:
        file.write(data)

    modified_data='./modified_data.txt'
    assert strategy_instance.check_data(test_data, modified_data)
    return strategy_instance

if __name__ == "__main__":
    fool_classifier('test_data.txt')

'''''    
    with open (test_data,'r') as file:
        testContent = [line.strip().split(' ') for line in file]

if __name__ == "__main__":
    fool_classifier('test_data.txt')
    
    for i in range(len(testContent)):
        tokens=[]
        for j in range(len(testContent[i])):
            if testContent[i][j] in class1_voc and testContent[i][j] in class0_voc:
                tokens.append((class0_voc[testContent[i][j]]/length_0,class1_voc[testContent[i][j]]/length_1,testContent[i][j]))
            elif testContent[i][j] in class0_voc:
                tokens.append((class0_voc[testContent[i][j]]/length_0,0,testContent[i][j]))
            elif testContent[i][j] in class1_voc:
                tokens.append((0,class1_voc[testContent[i][j]]/length_1,testContent[i][j]))
            else:
                tokens.append((0,0,testContent[i][j]))
                
        tokens = sorted(tokens,key =lambda s:(s[1]-s[0]),reverse = True)
        slots=[e[2] for e in tokens]
        waitingWords=[e for e in wait_words]
        original = [e for e in testContent[i]]
        for token in slots:
            for j in range(len(testContent[i])):
                if token == testContent[i][j] and len((set(original)-set(testContent[i])) | (set(testContent[i])-set(original)))<20:
                    while True:
                        word = waitingWords.pop()
                        if word not in testContent[i]:
                            for k in range(len(testContent[i])):
                                if testContent[i][k] == token:
                                    testContent[i][k] = word
                            break
                    break
                
    output_txt = 'modified_data.txt'
    with open(output_txt,'w') as file:
        for i in testContent:
            file.write(" ".join(i)+"")
    
    ## Write out the modified file, i.e., 'modified_data.txt' in Present Working Directory...
    ## You can check that the modified text is within the modification limits.
    modified_data='./modified_data.txt'
    assert strategy_instance.check_data(test_data, modified_data)
    return strategy_instance ## NOTE: You are required to return the instance of this class.



#'test_data.txt'
    
    #for i in sss:
     #   for j in i :
      #      idf =_idf(j,sss)
       #     tf = sss_dict[j] / lenlenvoc
        #    tf_idf = idf*tf
         #   L+=((j,tf_idf))
    #print(L)



    #len_sss = len(sss)#540
    #print(len(sss))
    #classss = _counter(sss)
    #print(classss)
    #length_0,length_1 = len(strategy_instance.class0),len(strategy_instance.class1)
    #class0_voc, class1_voc = _counter(strategy_instance.class0), _counter(strategy_instance.class1)
    #print(strategy_instance.class0)
    #tf  = _tf(classss,len_sss)
    #print(tf0)
    #L1=[]
    #L0=[]
    #print(list(tf0))
    #for i in list(tf0):
        #L0.append((i,tf0[i]))
    #print (L0)
    #print(sorted(L0,key =lambda s:(s[1]),reverse = True))
    #L0_sorted = sorted(L0,key =lambda s:(s[1]),reverse = True)
    #or i in list(tf1):
       #L1.append((i,tf1[i]))
    #print (L1)
    #L1_sorted = sorted(L1, key=lambda s: (s[1]), reverse=True)
    #print(tf1)
    #print(L0_sorted)
    #print(L1_sorted)
    #processed_words = sorted([(tf0[word] - tf1[word],word) if word in tf1 else (class0_voc[word]/length_0,word) for word in tf0])
    #print(processed_words)
    #wait_words = [i[1] for i in processed_words]
'''''
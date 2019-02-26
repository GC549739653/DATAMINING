## import modules here 
import pandas as pd
import numpy as np


################# Question 1 #################
def read_data(filename):
    df = pd.read_csv(filename, sep='\t')
    return (df)
# helper functions
def project_data(df, d):
    # Return only the d-th column of INPUT
    return df.iloc[:, d]

def select_data(df, d, val):
    # SELECT * FROM INPUT WHERE input.d = val
    col_name = df.columns[d]
    return df[df[col_name] == val]

def remove_first_dim(df):
    # Remove the first dim of the input
    return df.iloc[:, 1:]

def slice_data_dim0(df, v):
    # syntactic sugar to get R_{ALL} in a less verbose way
    df_temp = select_data(df, 0, v)
    return remove_first_dim(df_temp)


def single_dim(df):
    outputlist=[]
    LL = list(df.loc[0])
    outputlist.append([i for i in LL])
    #outputlist[0].pop()
    for i, num in enumerate(outputlist):
        sublist = [i for i in num]
        for j, sub_num in enumerate(sublist):
            if j == len(sublist)-1:
                break
            if sub_num == "ALL":
                pass
            else :
                subsublist = [i for i in sublist]
                subsublist[j] = 'ALL'
                if subsublist not in outputlist:
                    outputlist.append(subsublist)
    #print(outputlist)
    #for i in outputlist:
     #   i.append(LL[-1])
    head = list(df)
    #print(head)
    result = pd.DataFrame(outputlist, columns=head)
    return result

def pre_buc_rec_optimized(df, sublist, subresult):

    dims = df.shape[1]

    if dims!=1:
        L= list(project_data(df, 0))
        cutlistdim0= set(L)
        #print(dim0_vals)

        copy_of_sublist=[]
        for i in sublist:
            copy_of_sublist.append(i)

        for dim0 in cutlistdim0:
            subsublist=[]
            for i  in copy_of_sublist:
                subsublist.append(i)
            #print(pre_num)
            subsublist.append(dim0)
            #print(pre_num)
            pre_buc_rec_optimized(slice_data_dim0(df, dim0), subsublist, subresult)
        subsubsublist=[]
        for i in range(0,len(copy_of_sublist)):
            subsubsublist.append(copy_of_sublist[i])
        subsubsublist.append("ALL")
        pre_buc_rec_optimized(remove_first_dim(df), subsubsublist, subresult)

    else:
        sumvalue = sum(project_data(df, 0))
        sublist.append(sumvalue)
        subresult.loc[len(subresult)] = sublist
    #head= list(df)
    #result = pd.DataFrame(columns=head)


def buc_rec_optimized(df):  # do not change the heading of the function
    dims = df.shape[0]
    if dims != 1:
        L=list(df)
        head = []
        for i in L:
            head.append(i)
        subresult = pd.DataFrame(columns=head)
        sublist=[]
        pre_buc_rec_optimized(df, sublist, subresult)
    else:
        subresult = single_dim(df)
    return subresult

    #L=list(input.iloc[0])
    #outputlist=[]
    #outputlist.append(L)
    #LL=[i for i in L]
    #print(LL)

'''''
        a=0
        while a<len(L)-1:
            LL[i]='ALL'
            outputlist.append([i for i in LL])
            i+=1
            if i ==len(L)-1:
                break
            a+=1
        LL = [i for i in L ]
    for i in range(0,len(L)-1):
        LL[i]='ALL'
    outputlist.append(LL)
    print(outputlist)
    return L

#L = list(range(10))
#I = [i for i in L]
'''''
################# Question 2 #################

#def v_opt_dp(x, num_bins):# do not change the heading of the function
    # **replace** this line with your code
#-----------------------------------------------
def creatlist(x,numofbins):
    L=[]
    for i in range(numofbins):
        L.append([])
    for i in L:
        for j in range(len(x)):
            i.append(-1)
    return L
def appendbins(bins,x,start,end):
    L=[]
    for i in range (start,end):
        L.append(x[i])
    bins.append(L)
    return bins


def proc_index_matrix(x,index_matrix):
    #print(index_matrix)
    first = index_matrix[-1][0]
    #print(start)
    prefirst = first
    #print(prefirst)
    bins = []
    bins =appendbins(bins, x, 0, index_matrix[-1][0])

    for i in range(len(index_matrix) - 2, 0, -1):
        first = index_matrix[i][first]
        #print(start)
        bins = appendbins(bins, x,prefirst, first)
        prefirst = first
        #print(prefirst)
    bins = appendbins(bins, x, prefirst, len(x))
    return bins

def savematrix(matrix):
    matrixcopy = []
    for i in matrix:
        matrixcopy.append(i)
    return matrixcopy

def v_opt_dp(x, numofbins):  # do not change the heading of the function

    matrix=creatlist(x,numofbins)
    index_matrix=creatlist(x,numofbins)
    pre_v_opt_dp(0, numofbins - 1,x,numofbins,matrix,index_matrix)

    bins = proc_index_matrix(x, index_matrix)

    return matrix, bins

def pre_v_opt_dp(index_of_x, otherbins,x,numofbins,matrix,index_matrix):


    judge1 = numofbins-index_of_x-otherbins
    judge2 = len(x)-index_of_x

    if judge2 <= otherbins :
        pass
    else:
        if judge1 < 2:
            pre_v_opt_dp(index_of_x + 1, otherbins,x,numofbins,matrix,index_matrix)

            if (otherbins == 0):
                L=[]
                for i in range (index_of_x,len(x)):
                    L.append(x[i])
                value = np.var(L) * len(L)

                matrix[otherbins][index_of_x] = value
                return

            pre_v_opt_dp(index_of_x, otherbins - 1,x,numofbins,matrix,index_matrix)
            a=otherbins-1
            b=index_of_x+1
            min_list = [matrix[a][b]]

            for i in range(index_of_x + 2, len(x)):
                LL=[]
                for j in range (index_of_x,i):
                    LL.append(x[j])
                d=i-index_of_x
                c = matrix[a][i] + d * np.var(LL)
                min_list.append(c)
            minimum = min(min_list)
            matrix[otherbins][index_of_x] = minimum
            minindex = min_list.index(minimum)
            index = minindex + index_of_x+ 1
            index_matrix[otherbins][index_of_x] = index
from turtle import done
from numpy import indices
import re

def custom_find(list,target):
    for i in range(0,len(list)):
        if list[i] == target:
            return i 

    return -1    

masked_word="vinuthna"
length=len(masked_word)
tries=length
done=[]
answer=[]
for i in range(0,length):
    answer.append("__ ")
for i in range(0,2*length):

    take = input()
    print("word")
    
    done.append(take)
    
    indices = [i.start() for i in re.finditer(take,masked_word)]
    if len(indices)!=0:
        for j in range(0,length):
            if custom_find(indices,j)!=-1:
                answer[j]=masked_word[j]
                
    
            

    else:
        print('wrong input')
        tries=tries-1
    
    for i in range (0,len(answer)):
        print(answer[i],end=' ')
    print("")    
    if(custom_find(answer,"__ ")==-1):
        print("Congratulations")
        break
    print("next_try")   
    if tries==0:
        print("failed")
        print("Word is ",end=' ')
        print(masked_word)
        break  





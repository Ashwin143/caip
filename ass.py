#1
import math  
# x1=int(input())  
# x2=int(input())
# y1=int(input())
# y2=int(input())
# dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
# print(dist)

#2

# def fruitful(x1,x2,y1,y2):
#     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
#     return dist
# x1=int(input())  
# x2=int(input())
# y1=int(input())
# y2=int(input())
# print(fruitful(x1,x2,y1,y2))

#3
# Number = int(input(" Please Enter any Number: "))
# count = 0
# i = 2

# while(i <= Number//2):
#     if(Number % i == 0):
#         count = count + 1
#         break
#     i = i + 1

# if (count == 0 and Number != 1):
#     print(" %d is a Prime Number" %Number)
# else:
#     print(" %d is not a Prime Number" %Number)

#4
# count=0
# x=input().split(" ")
# for words in x:

#     if words.lower()==words.lower()[::-1]:
#         count+=1
    
# print(count)

#5 


# s=input()
# line = s.strip().lower() 
  

# d = dict()  
 
# words = line.split(" ") 
  
   
# for word in words: 
        
#     if word in d: 
           
#         d[word] = d[word] + 1
#     else: 
          
#         d[word] = 1
  

# for key in list(d.keys()): 
#     print(key, ":", d[key]) 
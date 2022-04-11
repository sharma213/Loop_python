# # count=1
# # num=int(input("enter your number"))
# # while count<=10:
# #     if(num%2==0):
# #         print("even",num)
# #     else:
# #         print("odd",num)
# #     count=count+1


# # list=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# # i=0
# # while i<len(list):
# #     j=0
# #     while j<len(list[i]):
# #         c=list[i][j]
# #         print(c,end="")
# #         j+=1
# #     i+=1

a=['1','2','3']
new=[]
# i=0
# while i<len(a):
#     c=a[i].split()
#     d=list(c)
#     i+=1
#     new.append(d)
# print(new)


# list=['1','2','3']
# new=[]
# i=0
# while i<len(list):
#     c=list[i].split()
#     d=list(c)
#     i=i+1
#     new.append(d)
# print(new)


a=[['red'],['green'],['blue']]
new=[]
i=0
while i<len(a):
    j=0
    b=''
    while j<len(a[i]):
        b=b+a[i][j]
        c=list(b)
        new.append(c)
        j+=1
    i+=1
print(new)


# # a=[10,2,3,4]
# # i=0
# # multipy=1
# # while i<len(a):
# #     multipy=multipy*a[i]
# #     i=i+1
# # print(multipy)


# a=[10,2,3,4]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+a[i]
#     i=i+1
# print(sum)


# # i=1
# # while i<=100:
# #     if (i%2==0):
# #         print(-i)
# #     else:
# #         print(i)
# #     i=i+1


# i=int(input("enter your number"))
# rev=0
# sum=0
# while i>0:
#     rev=(rev*10)+i%10
#     i=i//10
# print("reverse",rev)

# num=int(input("enter your number"))
# i=0
# counter =0
# while i<=num:
#     if num%1==0:
#         counter=counter+1
#     if counter==2:
#         print("prime")
#     else:
#         print("not a prime")
#     i=i+1

# i=2
# num=int(input("enter your number"))
# while (i<num):
#     if (num/i==0):
#         print(num,"is a not a prime number")
#         i=i+1
    # else:
        # print(num,"is a prime number")

# n=5
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         if i%2!=0:
# #             print("#", end=" " )
#         else:
#             print(j*j,end="")
#         j=j+1
#     i=i+1
#     print()
# b=4
# k=b
# while k>=1:
#     j=k
#     while j>=1:
#         if k%2!=0:
#           print("#",end="")
#         else:
#             print(j*j,end="")
#         j-=1
#     k-=1
#     print()


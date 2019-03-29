# DATA STRUCTURES
# 79. l=[10,20,30,[40,50,60],70,[80,90,20]]. Convert this list as single dimensional list
# 83. l=[1,2,3,[4,5,6],7,[8,9,10]] for single dimensional list

def unpack_2dlist(l):
    res = []
    for i in l:
        if isinstance(i, list):
            for j in i:
                res.append(j)
        else:
            res.append(i)
    return res


# 80. input: "Google" print count of each character


# string = "Google"
# for i in string:
#     print(f"count of {i}: {string.count(i)} ")

# 81. Convert n dimensional list to single dimensional list.DOUBT

# def flatten(l):
#     for el in l:
#         if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
#             yield from flatten(el)
#         else:
#             yield el


# 82. l=[1,2,3] just make it as a string.

# ll = [1, 2, 3]
# j = ""
# for i in ll:
#     j += str(i)
# print(j)


# 84. l=['a','A','b','B','d','D','c','C'] WAP to find out case

# l=['a','A','b','B','d','D','c','C']
# for i in l:
#     if i.isupper():
#         print(f"{i} is in uppercase")
#     else:
#         print(f"{i} is in lower case.")

# insensitive count and 85. case insensitive search for an element.

# l=['a','A','b','B','d','D','c','C']
# hs = set()
# lista = []
# for i in l:
#     lista += [i.lower()]
# for i in lista:
#     if i not in hs:
#         hs.add(i)
#         print(f"count of {i} is {lista.count(i)}")

# 86. l=['a','A','b','B','d','D','c','C']  sort the list properly

# l=['a','A','b','B','d','D','c','C']
# l.sort()
# print(l)

# 87. find the start position of the largest block of repeated characters in a given string, DOUBT

# string = input("Enter a string: ")
# c = 1
# temp = 0
# element = ""
# for i in range(1, len(string)):
#     if string[i - 1] == string[i]:
#         c += 1
#         print("c = ",c)
#     else:
#         if temp < c:
#             temp = c
#             c = 1
#             print("temp is ", temp)
#             element = string[i - 1]
#             print(element)
#         else:
#             c = 1
#
#
#
#
#
# print(string.index(element))


# 88. WAP to find union and intersection of lists.
#
# l1 = [1,2,3,4,5,6]
# l2 = [1,2,3,7,8,9,121,234]
# l = l1 + l2
# hs = set()
# intersection = []
# for i in l:
#     if i not in hs:
#         hs.add(i)
#     else:
#         intersection.append(i)
# union = list(hs)
# print("The union is: ", hs)
# print("The intersection is: ", intersection)

# 89. input: fun(5) output: [1,2,3,4,3,2,1]

# def fun(n):
#     res = []
#     temp = 0
#     for i in range(1, 2*n-2):
#         if i < n:
#             res.append(i)
#             temp = res[i-1]
#         else:
#             temp -= 1
#             res.append(temp)
#     return print(res)

# 90. input fun('abc') output: [[],][a],[b],[c],[a,b],[b,c],[c,a],[a,b,c]]

# def fun(string):
#     res = [[]]
#     for i in range(2**len(string)):
#         if i < len(string):
#             x = list(string[i-1])
#             res.append(x)
#         else:
#
#
#     return print(res)
#
#
# fun('abc')


# practice
# ll = [1,2,4,6,7,8,97,55,66]
# lll = ["Even" if i%2==0 else "ODd" for i in ll if isinstance(i, int)]
# l = ("Even" if i%2==0 else "ODd" for i in ll if isinstance(i, int))
# print(lll)
#
# lista = zip(ll,lll)
# print(lista)
# for i,j in lista:
#     print(i,j)

#
# get max profit
# stock_prices = [9, 7, 4, 1]
#
#
# def max_profit(stock_prices):
#     maxp = -200
#     buy = 0
#     sell = 0
#     for i in range(len(stock_prices)-1, 0, -1):
#         print("stockprice[i]: ",stock_prices[i])
#
#         for j in range(len(stock_prices)-1):
#             print("stock_prices[j]: ",stock_prices[j])
#             profit = stock_prices[i] - stock_prices[j]
#             print("profit: ", profit)
#             if maxp < profit:
#                 buy = stock_prices[j]
#                 sell = stock_prices[i]
#                 maxp = profit
#                 print("max_profit: ",maxp)
#     return print(sell-buy)
#
# max_profit(stock_prices)

# 91. Remove duplicates from the list: a=[1,2,3,2,3,4,1,,3,4]

# a=[1,2,3,2,3,4,1,3,4]
# hs = set()
# for i in a:
#     if i not in hs:
#         hs.add(i)
# result = list(hs)
# print(result)

# 92. l=['1','2','3'] get the sum of the list
#
# l=['1','2','3']
# sum = 0
# for i in l:
#     sum += int(i)
# print(sum)


# 93. l1=[1,2,3,4] l2=[5,6,7,8] sum of two lists

# l1=[1,2,3,4]
# l2=[5,6,7,8]
# l = l1 + l2
# sum = 0
# for i in l:
#     sum += i
# print(sum)


# 94. Find third max value of element in a list with soring and without sorting a list.

# l = [1,23,34,56,77,896,535,6676,345]
# # l.sort()
# # print(l[-3])
#
# for i in l:



# 95. Input = ["1/1","1/2","1/3","1/4","2/5","2/6","2/8"] Output = [['1/1-4'], ['2/5-6'], ['2/8']]
# 96. l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]
# output = [[1, 2, 3], [5], [7, 8, 9, 10, 11, 12, 13], [20], [22, 23, 24, 25, 26, 27], [20, 21, 22], [4]]



# 97. input = 1,2,3,4,5,6,8,10 output = odd,even,odd,even,odd,even,even,even
# 98. input n=3  DOUBT
#     		output:     111
#         		101
#         		111



# 99. input: Google
#     output: {'g':2,'o':2,'l':1,'e':1} use dictionary comprehension

# string = "Google"
# string1 = string.lower()
# dic = {}
# for i in string1:
#     if i not in dic:
#         dic.update({i:1})
#     else:
#         dic[i] += 1
# print(dic)

# 100. keys=['k1','k2'], values = ['v1','v2'] form a dictionary.

# keys = ['k1', 'k2']
# values = ['v1', 'v2']
# res = {}
# for i,j in zip(keys,values):
#     res.update({i:j})
# print(res)

# def test():
#     x=46
#     print("x = ",x)
#
# test()
#print("x = ",x) #local variable of function test()


# ###################################
# a = 1
#
#
# # Uses global because there is no local 'a'
# def f():
#     print('Inside f() : ', a) #a=1
#
#
# # Variable 'a' is redefined as a local
# def g():
#     a = 2
#     print('Inside g() : ', a) #a=2
#
#
# # Uses global keyword to modify global 'a'
# def h():
#     global a
#     a = 3
# #     print('Inside h() : ', a) #a value changed to 3
# #
# #
# # # Global scope
# # print('global : ', a) #1
# # f() #1
# # print('global : ', a) #1
# # g()#2
# # print('global : ', a) #1
# # h()#3
# # print('global : ', a) #3
#
# def myFun(**kwargs):
#
#     # for key, value in kwargs.items():
#     #     # print("%s == %s" % (key, value))
#     #     print(key,value)
#     print(kwargs)
#
# myFun(first='Geeks')
# kwargs1 = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"}
# myFun(kwargs1)



# def fact_recursive(n):
#     if n==0:
#         return  1
#     else:
#         return n*fact_recursive(n-1)
#
# print(fact_recursive(0))




def fibbo_recursive(n):
    if n<=1:
        return  n
    else:
        return fibbo_recursive(n-1)+fibbo_recursive(n-2)

for i in range (5):

    print(fibbo_recursive(i))


'''
def tail_recursive_fact(n,a=1):
    if n==0:
        return  a
    else:
        return tail_recursive_fact(n-1,n*a)
print(tail_recursive_fact(7))
'''
'''
k=[ lambda i:i*10 for i in range(1,11)]
for item in k:
    print(item)
'''


name_list = ['Grace Hopper', 'Ada Lovelace', 'Emmy Noether', 'Marie Curie']
var='Grace Hopper'.split()
var2=var[1]
func=[lambda x: x.split()[1],'Grace Hopper']
sorted_by_surname = sorted(name_list, key = lambda x: x.split()[1])

print(sorted_by_surname)
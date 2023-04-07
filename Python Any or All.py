n = int(input())
list1 = list(map(int,input().split()))
if all(ele > 0 for ele in list1) and any(ele < 10 for ele in list1):
    print(True)
else:
    print(False) 

orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



even_list=list(filter(lambda orig_list:orig_list%2==0,orig_list))
odd_list=list(filter(lambda orig_list:orig_list%2!=0 ,orig_list))

print(f"orig list {orig_list}")
print(f"odd list{odd_list}")
print(f"even list{even_list}")
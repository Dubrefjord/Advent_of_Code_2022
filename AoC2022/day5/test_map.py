list_a = [['1.1','1.2','1.3'],['2.1','2.2','2.3'],['3.1','3.2','3.3']]
list_b = ['1','2','3']
list_c = list(zip(*list_a,list_b))
print(list_c)
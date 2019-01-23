
data = [1, 3, 5, 7, 9] # 清單中裝著一些整數
#data = str(data)
# 請開始寫"寫入檔案"的程式碼

products = [['apple', '100'], ['car', '200']]

for p in data:
    print(p)

with open('test.txt','w') as f:
    for p in data:
        f.write(str(p) + '\n')

#with open('test.txt','w') as f:
#    for p in products:
#        f.write( p[0])


products = []
while True:
    name = input('請輸入商品名字')
    if name == 'q':
        break
    price = input('請輸入商品價格')
    '''完整寫法
    p = []
    p.append(name)
    p.append(price)
    '''
    #縮寫
    products.append([name, price])

print(products)

#for p in products:
#   print('商品',p[0],'價格是',p[1])

with open('products.csv','w') as f:
    for p in products:
        f.write( p[0] + ',' + p[1] + '\n')
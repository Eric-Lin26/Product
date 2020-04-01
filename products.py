products = []
money = 0

while True:
    name = input("請輸入商品名稱： ")
    if name == "q":
        break
    price = input("請輸入價格： ")
    products.append([name, price])
    money += int(price)

for p in products:
    print(p[0], "的價格是：", p[1], "元")

print("共花", money, "元")

with open ("products.csv" , "w" , encoding = "utf-8") as f:
    for d in products:
        f.write(d[0] + "," + str(d[1]) + "元" + "\n")
import os #operating system
products = []
if os.path.isfile("products.csv"): # os模組path功能中的isfile去尋找檔案
    print("找到檔案了！")
    # 讀取檔案
    with open("products.csv", "r", encoding = "utf-8") as f:
        for line in f:
            if "商品,價格" in line:
                continue
            name, price = line.strip().split(",") #.strip() 去除\n換行符號 #.split()切割
            products.append([name, price])
    print(products)
else:
    print("沒找到檔案！")

# 使用者輸入

while True:
    name = input("請輸入商品名稱： ")
    if name == "q":
        break
    price = input("請輸入價格： ")
    products.append([name, price])

for p in products:
    print(p[0], "的價格是：", p[1], "元")


# 寫入檔案
with open ("products.csv" , "w" , encoding = "utf-8") as f:
    f.write("商品,價格\n")
    for d in products:
        f.write(d[0] + "," + str(d[1]) + "\n")

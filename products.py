
import os #operating system

# 讀取檔案
def read_file(file):
    products = []
    # 讀取檔案
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if "商品,價格" in line:
                continue #跳過
            name, price = line.strip().split(",") #.strip() 去除\n換行符號 #.split()切割
            products.append([name, price])
    print(products)
    return products

# 使用者輸入
def user_input(products):
    while True:
        name = input("請輸入商品名稱： ")
        if name == "q":
            break
        price = input("請輸入價格： ")
        products.append([name, price])
    return products

# 印處所有購買紀錄
def print_buy_list(products):
    for p in products:
        print(p[0], "的價格是：", p[1], "元")

# 寫入檔案
def write(file, products):
    with open (file , "w" , encoding="utf-8") as f:
        f.write("商品,價格\n")
        for d in products:
            f.write(d[0] + "," + str(d[1]) + "\n")

# 主函式
def main():
    file = "products.csv"
    if os.path.isfile(file): # os模組path功能中的isfile去尋找檔案
        print("找到檔案了！")
        products = read_file(file)
    else:
        print("找不到檔案")
    products = user_input(products)
    print_buy_list(products)
    write("products.csv", products)

main()

# 此段程式碼不需特別了解, 該功能為將輸入的資料轉換為串列
# 只需知道 my_lst 為一串列, 即可對 my_lst 進行操作完成本題
my_lst = input().split(",")
my_lst.reverse()
first_item = my_lst.pop(0)
print(my_lst)
print(first_item)

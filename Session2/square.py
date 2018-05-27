# # print("hello", end="") # để đảm bảo 2 câu lệnh trên cùng 1 dòng
# # print("Hoa")

# for i in range (3):
#     #print in one line
#     for j in range (5):
#         print("* ", end = "")
#     #break
#     print()

for i in range(11): #tạo thành các dòng
    #print one line
    for j in range(11): # tạo thành từng dòng một, j: 0 - 10.
        if j <= 11 - i -1:
            print("  ", end = "")
        else:
            print("* ", end = "")
    #break
    print()
# name = input("Ten: ")
# age = input("Tuoi: ")
# print("Xin chao "+ name +" ban "+age+" tuoi")

# n =int(input("Nhap so can kiem tra:"))
# if n%2==0:
#    print("Chan")
# else:
#    print("Le")

# ###### Danh sách sinh viên cơ bản #############
# stu = []
# while True:
#   print("\n1. Thêm sinh viên")
#   print("2. Xóa sinh viên")
#    print("3. Hiển thị danh sách")
#    print("4. Thoát")
   
#    choice = input("Chọn chức năng: ")
   
#   if choice == "1":

#        name = input("Nhập tên sinh viên: ")
#        if name not in stu:
#           stu.append(name)
#       else:
#           print("Tên đã tồn tại!")
  
#    elif choice == "2":
#         name = input("Nhập tên sinh viên cần xóa: ")
#         if name not in stu:
#             print("Không tồn tại sinh viên này")
#         else :
#             stu.remove(name)
#             print(f"Đã xóa sinh viên {name} ra khỏi danh sách")
    
#     elif choice == "3":
#         print("Danh sách sinh viên:", stu)
    
#     elif choice == "4":
#         break

#     else:
#         print("Lựa chọn chưa hợp lệ!")


# #####################Tra Cứu số điện thoại ##############################
# phone_book = {}
# while True:
#     print("\n1. Thêm số điện thoại")
#     print("2. Tìm kiếm số điện thoại")
#     print("3. Hiển thị danh bạ")
#     print("4. Thoát")
    
#     choice = int(input("Chọn chức năng: "))
    
#     if choice == 1:
#         name = input("Nhập tên: ")
#         phone = input("Nhập số điện thoại: ")
#         if name not in phone_book:
#             phone_book[name]= phone
#             print(f"Số của {name} là: {phone}")
#         else:
#             print("Tên đã tồn tại")
    
#     elif choice == 2:
#         name = input("Nhập tên:")
#         if name in phone_book:
#             print(f"Số của {name}: {phone_book[name]}")
#         else :
#             print("Không tìm thấy!")
        
#     elif choice == 3:
#         for name, phone in phone_book.items():
#             print(name, ":", phone)
            
#     elif choice == 4:
#         break
    
#     else :
#         print("Lựa chọn không hợp lệ! Hãy nhập từ 1 đến 4")


# ############### Tính tiền điện ####################
# n = int(input("Nhập số kWh:"))

# if n <= 50:
#     ans = n * 1500
    
# elif n <= 100:
#     ans = 50 * 1500 + (n-50)*2000

# elif n <= 200:
#     ans = 50 * 3500 + (n-100)*2500

# else :
#     ans = 50 * 3500 + 100*2500 + (n -200 )*3000

# print("Số tiền cần trả", ans)

# ###########IF ELSE ##############
# age = int(input("Nhập tuổi: "))
# if age < 5 :
#     print("Miễn phí")
# elif age <=12 :
#     print("Vé trẻ em: 50,000 VNĐ")
# elif age <=18 :
#     print("Vé học sinh: 70,000 VNĐ")
# else :
#     print("Vé người lớn: 100,000 VNĐ")


# ########## For while #############
# n = int(input("NHap N= "))
# sum=0
# for i in range(1,n+1):
#     sum +=i
# print("n!= ", sum)


# n = int(input("Nhap n:"))
# print(f"Bảng cửu chương của {n} là:")
# for i in range(1,11):
#     ans = n*i
#     print(f"{n} x {i} = {ans}")

# n = int(input("Nhap N = "))
# is_prime = True
# if n <2 :
#     print("N không là số nguyên tố ")
# else :
#     for i in range (2,n):
#         if n%i==0:
#             is_prime = False
#             break
#     if is_prime == True:
#         print("N là số nguyên tố ")
#     else :
#         print("N không là số nguyên tố ")


# n = int(input("Nhập n: "))
# for i in range (1,n+1):
#     for j in range (1, i+1):
#         print(j, end=" ")
#     print()



# stus = []
# while True:
#     print("\n1. Thêm vào list.")
#     print("2. Xóa vào list.")
#     print("3. Hiển thị vào list.")
#     print("4. Thoát.")
#     choice = input("Chọn: ")
    
#     if choice == "1":
#         name =input( "Nhập tên sinh viên: ")
#         if name not in stus:
#             stus.append(name)
#         else:
#             print("Tên đã tồn tại")
#     elif choice == "2":
#         name =input("Nhập tên sinh viên cần xóa: ")
#         if name in stus:
#             stus.remove(name)
#         else :
#             print("Tên không tồn tại")
        
#     elif choice == "3":
#         print(stus)
            
#     elif choice == "4":
#         break
    
#     else:
#         print("Chỉ nhập 1-4")



# ####################Tính phương trình bậc 2#####################
# from math import sqrt

# print("Giải phương trình bậc 2: ax^2+bx+c=0")
# a= int(input("Nhập a = "))
# b= int(input("Nhập b = "))
# c= int(input("Nhập c = "))

# if a == 0:
#     if b == 0:
#         if c == 0:
#             print("Phương trình vô số nghiệm")
#         else :
#             print("Phương trình vô nghiệm")
#     else :
#         if c == 0:
#             print("Phương trình có nghiệm x=0")
#         else :
#             x = -b/c
#             print(f"Phương trình có nghiệm x={x}")

# else :
#     delta = b**2 - 4*a*c
#     if delta < 0:
#         print("Phương trình vô nghiệm")
#     elif delta == 0:
#         x = -b/(2*a)
#         print(f"Phương trình có nghiệm kép x={x}")
#     else :
#         x1 = float((-b + sqrt(delta))/(2*a))
#         x2 = float((-b - sqrt(delta))/(2*a))
#         print("Phương trình có hai nghiệm phân biệt")
#         print (f"x1={x1}")
#         print (f"x2={x2}")

# x = True
# y = False
# z = False
# if not x or y:
#     print(1)
# elif not x or not y and z:
#     print (2)
# elif not x or y or not y and x:
#     print(3)
# else:
#     print(4)
    

# a = [1, 3, 3, 4, 5]
# n = len(a)
# for i in range (0,n):
#     print(a[i])




# #################### Mảng ##########################
a =[]
while True:
    print("\n   MỤC LỤC")
    print("1. Nhập số liệu")
    print("2. Xóa số liệu")
    print("3. Tìm số liệu")
    print("4. Hiển thị số liệu số liệu")
    print("5. Thoát")
    choice = input("Nhập lựa chọn: ")
    
    if choice == "1":
        n = int(input("Nhập kích thước cần thêm vào : "))
        x = 1
        for i in range (0,n):
            tmp = input(f"Nhập giá trị thứ {x} = ")
            a.append(tmp)
            x += 1
        print ("Mảng thu được là",a)

    elif choice =="2":
        n = int(input("Xóa phần tử số : "))
        if n <len(a):
            print ("Mảng ban đầu là",a)
            a.pop(n)
            print ("Mảng sau xóa là",a)
        else :
            print("Stt nằm ngoài phạm vi của mảng")
    elif choice =="3":
        n = int(input("Nhập vị trí cần tìm : "))
        if n <len(a):
            tmp =a[n]
            print(f"Giá trị cần tìm là : {tmp}")
            print ("Trong ",a)
        else :
            print("Stt nằm ngoài phạm vi của mảng")
        
    elif choice =="4":
        print(a)
        
    elif choice =="5" :
        break
    
    else :
        print("Chỉ nhập 1-5")



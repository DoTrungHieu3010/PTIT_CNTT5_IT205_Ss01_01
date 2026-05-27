user_name = input("Nhap ten benh nhan: ")
gender = input("Nhpa gioi tinh: ")
date_birth = int(input("Nhap nam sinh: "))
phone_num = input("Nhap so dien thoai: ")
email = input("Nhap email: ")
symptoms = input("Nhap trieu chung: ")
cost = float(input("Nhap chi phi kham: "))

code = f"MV{date_birth}001"

print("----PHIEU KHAM BENH----")
infomation = f"Ma benh nhan: {code}\nTen benh nhan: {user_name}\nGioi tinh: {gender}\nNam sinh: {date_birth}  So dien thoai: {phone_num}\nEmail: {email}\nTrieu chung: {symptoms}\nChi phi kham: {cost} VND"
print(infomation)
# Dò luồng thực thi
# Người dùng nhập tên bệnh nhân qua input lưu vào biến name_patient
# Người dùng nhập cân nặng qua input lưu vào biến weight
# Chương trình in ra thông tin vừa nhập
# chương trình kiểm tra kiểu dữ liệu của biến weight bằng type(weight) và in ra cảnh báo

# Đặc điểm của hàm input trong Python là input sẽ mặc định trả về dữ liệu về dạng chuỗi

print("- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN -")
name_patient = input("Nhập tên bệnh nhân: ")
weight = float(input("Nhập cân nặng bệnh nhân: "))
print("- KIỂM TRA DỮ LIỆU LƯU TRỮ --")
print("Bệnh nhân : ", name_patient)
print("Cân nặng dã nhập : ",weight)
# Trường nhóm IT viết thêm dòng này để kiểm tra dữ liệu của cân nặng
print("CẢNH BÁO Kiểu dữ liệu dang lưu là : ",type (weight))
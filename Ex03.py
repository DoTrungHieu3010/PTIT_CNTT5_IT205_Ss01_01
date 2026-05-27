# Dữ liệu đầu vào:
# Tên bệnh nhân: String
# Mã bệnh nhân: String
# Tên khoa: String
# Dữ liệu đầu ra:
# Chuỗi theo định dạng của đề bài
# Bệnh nhân: [Họ tên] - Mã BA: [Mã bệnh án] - Chuyển tới: [Khoa/Phòng khám]

# Sử dụng hàm input để nhập dữ liệu từ bàn phím
# Lưu dữ liệu vào biến kiểu string
# Dùng print để hiển thị lại thông tin theo định dạng chuẩn
# Có thể dùng f-string để ghép chuỗi 


# Thiết kế thuật toán
# 1. Nhập họ và tên bệnh nhân từ bàn phím lưu vào biến ho_ten
# 2. Nhập mã bệnh án từ bàn phím lưu vào biến ma_ba
# 3. Nhập khoa/phòng khám chỉ định lưu vào biến khoa
# 4. Tạo chuỗi phiếu khám bệnh điện tử theo định dạng:
#    "Bệnh nhân: {ho_ten} - Mã BA: {ma_ba} - Chuyển tới: {khoa}"
# 5. In ra phiếu khám bệnh điện tử
# 6. In ra thông báo xác nhận: "Thông tin bệnh nhân đã được ghi nhận thành công!"

patient_name = input("Nhập tên bệnh nhân: ")
patient_id = input("Nhập mã bệnh nhân: ")
department = input("Nhập khoa chuyển tới: ")

print(f"Bệnh nhân: {patient_name} - Mã BN: {patient_id} - Chuyển tới: {department}")
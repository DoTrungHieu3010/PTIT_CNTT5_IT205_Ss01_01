# Input:
# Mã bệnh nhân: String
# Nhiệt độ cơ thể: String
# Nhịp tim: String
# Output:
# Mã bệnh nhân: String
# Nhiệt độ cơ thể: Float
# Nhịp tim: Integer

# Có 2 giải pháp ép kiểu dữ liệu:
# Ép kiểu trực tiếp
# Ép kiểu sau khi lưu chuỗi

# |Tiêu chí      | Ép kiểu trực tiếp      | Ép kiểu sau khi lưu chuỗi |
# |Số lượng biến | Ít (3 biến)            | Nhiều hơn (5 biến)        |
# |Độ ngắn gọn   | Ngắn gọn nhất          | Dài hơn một chút          |
# |Khả năng debug| Khó dò lỗi khi nhập sai| Dễ debug vì có biến gốc   |

# Trong môi trường bệnh viện thì giải pháp 2 hợp lý hơn vì nó giữ lại giữ lại dữ liệu gốc dạng chuỗi để kiểm tra từ đó sẽ dễ kiểm tra

patient_name = input("Nhập mã bệnh nhân: ")
temperature_body = float(input("Nhập nhiệt độ cơ thể: "))
heart_rate = int(input("Nhập nhịp tim: "))

information = f"""
--- KẾT QUẢ CHUẨN HÓA DỮ LIỆU ---
Mã bệnh nhân: {patient_name}
Nhiệt độ cơ thể: {temperature_body} độ C
=> Kiểu dữ liệu hệ thống ghi nhận: {type(temperature_body)}
Nhịp tim: {heart_rate} nhịp/phút
=> Kiểu dữ liệu hệ thống ghi nhận: {type(heart_rate)}
---------------------------------
Thông báo: Dữ liệu hợp lệ. Màn hình Monitor đã sẵn sàng kết nối!
"""

print(information)

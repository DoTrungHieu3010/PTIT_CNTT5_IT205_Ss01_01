# Luồng thực thi của chương trình:
# Input dữ liệu -> In thông tin lên terminal

# Chương trình không bị crash  nhưng dữ liệu bị in ra sai do vị trí biến trong print bị sai từ đó khiến cho dữ liệu in ra terminal bị sai

print(' HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ');
name_patient = input('Nhập tên bệnh nhân: ');
age = int(input('Mời bạn nhập tuổi: '));
symptom = input('Mời bạn nhập triệu chứng bênh: ');

print(' -- PHIẾU KHÁM BỆNH --');
print ('Tên bệnh nhân:', name_patient);
print('Tuổi:', age);
print ('Triệu chứng:', symptom);
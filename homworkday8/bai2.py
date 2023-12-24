import numpy as np
A = np.array([int(i) for i in input().split()])
B = np.array([int(i) for i in input().split()])
maximum = np.max(A)
minimum = np.min(A)
mean = np.mean(A)
std_dev = np.std(A)
median = np.median(A)

print("Maximum:", maximum)
print("Minimum:", minimum)
print("Mean:", mean)
print("Standard Deviation:", std_dev)
print("Median:", median)
# Tạo 1 ma trận numpy c (2-D) có kích thước nx2 từ a, b, in ra màn hình.
C = np.array((A, B))
print(C)
# Khởi tạo 1 ma trận (2-D) numpy d với kích thước nxn theo phân phối Gauss
mean = np.mean(B)
std_dev = np.std(B)

D = np.random.normal(mean, std_dev, size=(len(A),len(B)))
print(D)
#Tính tổng, hiệu, tích 2 ma trận, tích ma trận chuyển vị
e = np.expand_dims(C, axis=0)
print(e.shape)
print(e)
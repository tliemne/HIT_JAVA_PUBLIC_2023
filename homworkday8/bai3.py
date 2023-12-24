import numpy as np
scores = np.random.randint(0, 11, (3, 20))
print(scores)
print(f"max: {np.argmax(scores)}")
print(f"min: {np.argmin(scores)}")
# Làm phẳng mảng và xóa đi các vị trí có điểm là 0, in ra màn hình.
fscores = scores.flatten()
print(fscores)
# Sắp xếp giảm theo thuật toán quicksort, in ra màn hình.
sorted = np.sort(fscores)[::-1]
print(sorted)
# Nhập vào một số thực k từ bàn phím và cho biết vị trí chèn k vào mảng mà không phá vỡ tính sắp xếp của mảng và thêm vào vị trí đó.
k = float(input("Nhap vao so thuc k: "))  
index = np.searchsorted(sorted,k)
sorted =np.insert(sorted,index,k)
sorteds = np.sort(sorted)[::-1]
print(sorteds)
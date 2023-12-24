import numpy as np
#khoi tao mang numpy nguyen
n = 7
arr = np.random.randint(1, 15, size= n)
print("ndim: ", arr.ndim)
print("shape: ", arr.shape)
print("len: ", len(arr))
print("dtype: ", arr.dtype)
print("itemsize: ", arr.itemsize)
# khoi tao mang numpy vs 100 so chan dau tien
arr = np.arange(0, 200, 2)
print("ndim: ", arr.ndim)
print("shape: ", arr.shape)
print("len: ", len(arr))
print("dtype: ", arr.dtype)
print("itemsize: ", arr.itemsize)
#khoi tao 1 ma tran numpy co kich thuoc n*n với 100 phần tử 0, in ra màn hình
n = int(100 ** (1/2))
arr = np.zeros((n,n))
print("ndim: ", arr.ndim)
print("shape: ", arr.shape)
print("len: ", len(arr))
print("dtype: ", arr.dtype)
print("itemsize: ", arr.itemsize)
#Khởi tạo ma trận đơn vị có kích thước nxn.
n = 5
arr = np.eye(n)
print("ndim: ", arr.ndim)
print("shape: ", arr.shape)
print("len: ", len(arr))
print("dtype: ", arr.dtype)
print("itemsize: ", arr.itemsize)
#Khởi tạo ma trận đường chéo với các giá trị trên đường chéo là mảng a.
arr = np.arange(0, 10, 2)
e = np.diag(arr)
print("Array e:")
print(e)
print("ndim: ", e.ndim)
print("shape: ", e.shape)
print("len: ", len(e))
print("dtype: ", e.dtype)
print("itemsize: ", e.itemsize)
import numpy as np

vec = np.array([1, 2, 3, 4, 5])
print(vec)

mat = np.array([[10, 20, 30], [40, 50, 60]])
print(mat)

print(type(vec))
print(type(mat))

print(vec.ndim)
print(vec.shape)

print(mat.ndim)
print(mat.shape)

zero_mat = np.zeros((2, 3))
print(zero_mat)

one_mat = np.ones((2, 3))
print(one_mat)

same_value_mat = np.full((2, 2), 7)
print(same_value_mat)

eye_mat = np.eye(3)
print(eye_mat)

random_mat = np.random.random((2, 2))
print(random_mat)

range_vec = np.arange(10)
print(range_vec)

n = 2
range_n_step_vec = np.arange(1, 10, n)
print(range_n_step_vec)

reshape_mat = np.arange(30).reshape((5, 6))
print(reshape_mat)

mat = np.array([[1, 2, 3], [4, 5, 6]])
print(mat)

slicing_mat = mat[0, :]
print(slicing_mat)

slicing_mat = mat[:, 1]
print(slicing_mat)

mat = np.array([[1, 2,], [4, 5,], [7, 8]])
print(mat)
print(mat[1, 0])

indexing_mat = mat[[2, 1], [0, 1]]
print(indexing_mat)

# TODO: ???

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
result = x + y
print(result)

result = x - y
print(result)

result = x * y
print(result)

result = x / y
print(result)

mat1 = np.array([[1, 2,], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])

# 1 2  5 6
# 3 4  7 8
# 5 + 14 6 + 16 15 + 28 18 + 32
mat3 = np.dot(mat1, mat2)
print(mat3)

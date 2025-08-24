import numpy as np

print("NumPy Array Inspector\n")

OriginalArr = np.array([10, 20, 30, 40, 50])

print(f"Original Array : \n {OriginalArr}\n")

print(f"Indexing Example (3rd element): \n {OriginalArr[2]}\n")

print(f"Slicing Example(from index 1 to 3): \n {OriginalArr[1:4]}\n")

print(f"Data Type of Array: \n {OriginalArr.dtype}\n")

print("Copy vs View Demonstration:\n")

OriginalArr1 = OriginalArr.copy()
print(f"Copy Array: \n {OriginalArr1}\n")

OriginalArr2 = OriginalArr.view()
print(f"View Array: \n {OriginalArr2}\n")

print("After modifying the original array:\n")

copy = OriginalArr.copy()
OriginalArr[0] = 99

view = OriginalArr.view()
OriginalArr[0] = 99

print(f"Copy: \n {copy}\n")

print(f"View: \n {view}\n")

print(f"Original: \n {OriginalArr}\n")

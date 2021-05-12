import numpy as np
npy_file_name = input("npy file name: ")
npy = np.load(npy_file_name)


print("shape:",npy.shape)
print("content[:10]\n",npy[:10])
print("content[10:]\n",npy[10:])
print("content\n",npy)


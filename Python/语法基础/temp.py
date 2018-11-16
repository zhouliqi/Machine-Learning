import numpy as np

e = [1.0/10 for i in range(10)]
print(e)
e=np.array(e)
print(e)
e = e.reshape(-1,1)
print(e)


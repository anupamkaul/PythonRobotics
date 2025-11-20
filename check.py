import matplotlib

print(matplotlib.get_backend())

import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
plt.show()

matplotlib.use('TkAgg')

print(matplotlib.get_backend())

import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
plt.show()


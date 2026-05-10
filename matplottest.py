
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

ax.set_title('A simple plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

fig.savefig('test.png')
plt.show()


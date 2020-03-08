from matplotlib import pyplot as plt
x = range(2,26,2)
y = [15,13,14.5,17,20,25,26,26,27,22,18,15]
plt.figure(figsize=(20,8),dpi=80)
plt.plot(x,y)
plt.xticks(range(0,25)[::2])
# plt.savefig("./t1.png")
plt.show()

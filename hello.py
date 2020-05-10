import matplotlib as mlp
import matplotlib.pyplot as plt

print("hello khadija")
name = "abcde"
nbr = [1,2,3,4]

for i in range(0,4):
    print(name[i],nbr[i], sep="_", end="\n")

plt.xlabel("Zahlen")
plt.ylabel("Quadratzahen")

plt.plot([1,2,3,4], [1,4,9,16], 'b*')
plt.axis([0,5,0,20])
plt.grid(True)

#plt.show()
plt.savefig('myplot.png')

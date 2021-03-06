#---------------------------------------Hands On #1---------------------------------------#

import matplotlib.pyplot as plt



# cubed=[]
# inputVal=[1,2,3,4,5]
# for num in inputVal:
#     cubed.append(num**3) 
# plt.plot(inputVal,cubed)
# plt.title("Cubed Numbers")
# plt.ylabel("Values Cubed")
# plt.xlabel("Input Values")
# plt.grid()
# plt.show()

#---------------------------------------Hands On #2---------------------------------------#

#Plot 1 
# cubed=[]
# inputVal=[1,2,3,4,5]
# for num in inputVal:
#     cubed.append(num**3)     
# ax1 = plt.subplot(1,2,1)
# ax1.plot(inputVal,cubed)
# plt.ylabel("Values Cubed")
# plt.xlabel("Input Values")
# plt.title("Cubed Numbers")
# plt.grid()


# #Plot 2 
# list2=[]
# inputVal=[1,2,3,4,5]
# for num in inputVal:
#     list2.append(num**2) 
# ax2 = plt.subplot(1,2,2)
# ax2.plot(inputVal,list2)
# plt.ylabel("Second Power")
# plt.xlabel("Input Values")
# plt.title("Numbers Raised")
# plt.grid()

# plt.suptitle("Fun With Numbers")
# plt.show()

#---------------------------------------Hands On #3---------------------------------------#

# #Plot 1 
# cubed=[]
# inputVal=[1,2,3,4,5]
# for num in inputVal:
#     cubed.append(num**3)     
# ax1 = plt.subplot(1,2,1)
# ax1.plot(inputVal,cubed, marker='*', ls='--', c='orange', lw='2.0')
# plt.ylabel("Values Cubed")
# plt.xlabel("Input Values")
# plt.title("Cubed Numbers")
# plt.grid()


# #Plot 2 
# list2=[]
# inputVal=[1,2,3,4,5]
# for num in inputVal:
#     list2.append(num**2) 
# ax2 = plt.subplot(1,2,2)
# ax2.plot(inputVal,list2)
# plt.ylabel("Second Power")
# plt.xlabel("Input Values")
# plt.title("Numbers Raised")
# plt.grid()

# plt.suptitle("Fun With Numbers", c="blue", fontfamily="Comic Sans MS", fontsize="20")
# plt.subplots_adjust(top=.8,wspace=1)
# plt.show()

#---------------------------------------Hands On #4---------------------------------------#

#Plot 1 
cubed=[]
inputVal=[1,2,3,4,5]
for num in inputVal:
    cubed.append(num**3)     
ax1 = plt.subplot(1,2,1)
ax1.plot(inputVal,cubed, marker='*', ls='--', c='orange', lw='2.0')
plt.ylabel("Values Cubed")
plt.xlabel("Input Values")
plt.title("Cubed Numbers")
plt.grid()


#Plot 2 
list2=[]
inputVal=[1,2,3,4,5]
for num in inputVal:
    list2.append(num**2) 
ax2 = plt.subplot(1,2,2)
plt.style.use("seaborn-dark-palette")
ax2.plot(inputVal,list2)
plt.ylabel("Second Power")
plt.xlabel("Input Values")
plt.title("Numbers Raised", color="purple")
plt.grid(color="lemonchiffon")
plt.suptitle("Fun With Numbers", c="blue", fontfamily="Comic Sans MS", fontsize="20")
plt.subplots_adjust(top=.8,wspace=1)
plt.show()
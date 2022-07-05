
from turtle import color
from pylab import  *
from numpy import *
import scipy
from scipy.special import jn
N=101                           
k=9 
A0=1.05
B0=-0.105
data = np.loadtxt("fitting.dat")
t=data[:,0]
y=data[:,1:]
def G(t,A,B):
    return A*jn(2,t)+B*t
g=G(t,A0,B0)
figure(0)
plot(t,g)
plot(t,y)
grid(True)
sigma=logspace(-1,-3,k)
legend(sigma)
labels = append(sigma, "True Value")
for i in range(k):
    labels[i] = "$\sigma" + "_" + str(i + 1) + "$" + "=" + str(round(float(labels[i]), 4))
legend(labels)
xlabel("t"+"$\\rightarrow$")
ylabel("f(t)+n"+"$\\rightarrow$")
title("Data to be fitted to theory")
show()

figure(1)
plot(t,g,label='actual graph')
stdev = std(y[:, 0] - g)
grid(True)
errorbar(t[::5],y[::5,0],stdev,fmt='ro',label='errorbar')
legend()
title("data points for"+"$\sigma$"+"=0.01 along with the exact function")
xlabel("t"+"$\\rightarrow$")
show()


coulmn1=jn(2,t)
column2=t
M=c_[coulmn1,column2]
p=array([A0,B0])
print(allclose(g,dot(M,p)))

figure(2)
A = linspace(0, 2, 21)
B= linspace(-0.2, 0, 21)
Eij=zeros((len(A),len(B)))
fk = y[:, 0]
#calculate E for the ith column of data points
for i in range(len(A)):
    for j in range(len(B)):
        Eij[i, j] = ((fk-G(t,A[i],B[j]))**2).mean(axis=0)
t1, y1 = meshgrid(A, B)
levels = linspace(0.025, 0.5, 20)
contour_lines= contour(t1, y1, Eij,levels)
clabel(contour_lines, levels)
p=scipy.linalg.lstsq(M,g)
plot(p[0][0], p[0][1], color="red", marker="o")
title("contour plot of Eij")
xlabel("A"+"$\\rightarrow$")
ylabel("B"+"$\\rightarrow$")
show()


figure(3)
error_in_A=[]
error_in_B=[]

for i in range(9):
    temp=scipy.linalg.lstsq(M,y[:,i])[0]
    error_in_A.append(abs(temp[0]-A0))
    error_in_B.append(abs(temp[1]-B0))

plot(sigma, error_in_A, linestyle="--", marker="o", label="error in A")
plot(sigma, error_in_B, linestyle="--", marker="o", label="error in B")
grid(True)
title(" Variation of error with noise")
xlabel("Noise standard deviation"+"$\\rightarrow$",size=15)
ylabel("$MS Error\\rightarrow$",size=15)
legend()
show()

figure(4)
loglog(sigma, error_in_A,linestyle=" ", marker="o", label="error in A",markerfacecolor="blue")
loglog(sigma, error_in_B,linestyle=" ", marker="o", label="error in B",markerfacecolor="red")
stem(sigma, error_in_A, 'b',use_line_collection = True,markerfmt=" ")
stem(sigma, error_in_B, 'r', use_line_collection = True,markerfmt=" ")
grid(True)
title("Variation of error with noise")
xlabel("$\sigma_n\\rightarrow$")
ylabel("$MS Error\\rightarrow$")
legend()
show()
exit()
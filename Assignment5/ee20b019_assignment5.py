
from cProfile import label
from turtle import color
from black import err
from numpy import *
from pylab import * 
import mpl_toolkits.mplot3d.axes3d as p3
import sys

Nx=25
Ny=25
R=8
Niter=1500

try:
    Nx=int(sys.argv[1])
    Ny=int(sys.argv[2])
    R=int(sys.argv[3])
    Niter=int(sys.argv[4])
except:
    Nx=25
    Ny=25
    R=8
    Niter=1500
    


phi=zeros((Ny,Nx))
x=linspace(-0.5,0.5,Nx)
y=linspace(-0.5,0.5,Ny)
Rnorm= float(R/(Nx-1))+0.001
Y,X=meshgrid(y,x)
ij= where(X*X+Y*Y <= Rnorm**2)
levels=linspace(0,1,50)
phi[ij]=1.0

figure(1)
contourf(Y, X, phi,levels,cmap='terrain')
xcord=ij[0]/Nx-1/2
ycord=ij[1]/Ny-1/2
scatter(xcord,ycord,marker='o',label="V=1",s=5)
xlim((-1/2,1/2))
ylim((-1/2,1/2))
title("contour plot of initial phi")
xlabel("$x\\rightarrow$")
ylabel("$y\\rightarrow$")
legend()
show()
error_phi=zeros(Niter)
for k in range(Niter):
    oldphi=phi.copy()
    phi[1:-1,1:-1] = 0.25*(phi[1:-1,0:-2] + phi[1:-1,2:] + phi[0:-2,1:-1] + phi[2:,1:-1])
    phi[0,1:-1],phi[-1,1:-1],phi[:,-1] = phi[1,1:-1],phi[-2,1:-1],phi[:,-2]
    phi[ij] = 1.0
    error_phi[k]=((abs(phi-oldphi))).max();
t=array(range(Niter))
M=vstack([t,ones(len(t))]).T
B,log_A = linalg.lstsq(M,log(error_phi),rcond=None)[0]

error_fit=(exp(B*(t+0.5)+log_A))

figure(2)
semilogy(t,error_phi,label='errors')
scatter(t[::50],error_phi[::50],color='red',label='datapoints after every 50th point')
title("semilog plot of error")
xlabel("Iterations$\\rightarrow$")
ylabel("Absolute Err$\\rightarrow$")

legend()
show()

figure(3)
semilogy(t,error_phi,label='errors')
plot(t,error_fit,label='errors_fit',color='green',linewidth=1.5)
scatter(t[::50],error_phi[::50],color='red',label='datapoints after every 50th point')
plot(t[500:],error_fit[500:],label='fit after 500th iterations',color='red')
title("semilog plot of error")
xlabel("Iterations$\\rightarrow$")
ylabel("Absolute Err$\\rightarrow$")

legend()
show()

figure(4)
loglog(t,error_phi,label="errors")
scatter(t[::50],error_phi[::50],label='after 50th iterations',color='green')
title("loglog plot of error")
xlabel("iterations$\\rightarrow$")
ylabel("Absolute Err$\\rightarrow$")
legend()
show()

figure(4)
loglog(t,error_phi,label="errors")
scatter(t[::50],error_phi[::50],label='after 50th iterations',color='green')
semilogx(t,error_fit,label="error fit")
semilogx(t[500:],error_fit[500:],label="error fit after 500th iteration")
title("loglog plot of error")
xlabel("iterations$\\rightarrow$")
ylabel("Absolute Err$\\rightarrow$")
legend()
show()


fig=figure(5)
ax=p3.Axes3D(fig)
surf = ax.plot_surface(Y, X, phi.T, rstride=1, cstride=1, cmap=cm.jet)
xlabel("x-->")
ylabel("y-->")
title("The 3-D surface plot of the potential")
fig.set_size_inches(8, 8)
colorbar(surf,shrink=0.75)
show()

fig6=figure(6)
a=contourf(X,Y,phi,levels,cmap='terrain')
xcord=ij[0]/Nx-1/2
ycord=ij[1]/Ny-1/2
scatter(xcord,ycord,marker='o',label="V=1",s=5)
xlim((-1/2,1/2))
ylim((-1/2,1/2))
fig6.colorbar(a)
title("contour plot of phi")
xlabel("$x\\rightarrow$")
ylabel("$y\\rightarrow$")
legend()
show()


Jy = 0.5*(phi[1:-1,0:-2]-phi[1:-1,2:])
Jx= 0.5*(-phi[2:, 1:-1]+phi[0:-2,1:-1])
figure(7)
quiver(X[1:-1, 1:-1], Y[1:-1, 1:-1], Jx, Jy, scale=4, label="j")
scatter(xcord,ycord,marker='o',label="V=1",s=5)
xlim((-1/2,1/2))
ylim((-1/2,1/2))
title("Vector plot off current density")
xlabel("$x\\rightarrow$")
ylabel("$y\\rightarrow$")
legend()
show()

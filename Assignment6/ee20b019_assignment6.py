from numpy import *
from pylab import * 
import scipy.signal as sp
alpha=0.5
W=1.5
def solve(alpha,W):
    F=sp.lti([1,alpha],[1,2*alpha,W**2+alpha**2])
    X=sp.lti([1],[1,0,W**2])
    numerator= polymul(F.num , X.num)
    denominator= polymul(F.den , X.den)
    print(denominator)
    sol=sp.TransferFunction(numerator,denominator)
    print(F)
    print(X)
    print(sol)
    return sol
sol=solve(0.5,1.5)
t,x=sp.impulse(sol,None,linspace(0,50,20001))
plot(t,x)
xlabel("$t\\rightarrow$")
ylabel("$X\\rightarrow$")
show()

sol=solve(0.05,1.5)
t,k=sp.impulse(sol,None,linspace(0,50,2001))
plot(t,k)
xlabel("$t\\rightarrow$")
ylabel("$X\\rightarrow$")
show()
alpha=0.05
H=sp.TransferFunction([1],[1,0,W**2])
t=linspace(0,50,2001)
def f(W,alpha):
    func=cos(W*t)*exp(-alpha*t)
    return func


t=linspace(0,100,2001)
W=1.4
while W<=1.6 :
    t,p,svec=sp.lsim(H,f(W,alpha),t)
    plot(t,p,label="W= "+ str(W))
    legend()
    show()
    W=W+0.05

x_spring=sp.lti([1,0,2,0],[1,0,3,0,0])
y_spring=sp.lti([2,0],[1,0,3,0,0])
time,plt_x=sp.impulse(x_spring,None,linspace(0,20,2001))

plot(time,plt_x)
xlabel("$t\\rightarrow$")
ylabel("$X\\rightarrow$")
show()

time,plt_y=sp.impulse(y_spring,None,linspace(0,20,2001))
plot(time,plt_y)
xlabel("$t\\rightarrow$")
ylabel("$Y\\rightarrow$")
show()
R=100.0
L=1e-6
C=1e-6
H_circuit=sp.lti([1],[L*C,R*C,1])
w,S,phi=H_circuit.bode()
subplot(2,1,1)
semilogx(w,S)
xlabel("$t\\rightarrow$")
ylabel("$|H(S)|\\rightarrow$")
subplot(2,1,2)
semilogx(w,phi)
xlabel("$t\\rightarrow$")
ylabel("$\u03C6\\rightarrow$")
show()

w1=1e3
w2=1e6
t1=linspace(0,30*1e-6,2001)

Vi=cos(w1*t1)-cos(w2*t1)

t1,j,svec=sp.lsim(H_circuit,Vi,t1)
plot(t1,j)
xlabel("$t\\rightarrow$")
ylabel("$Vo\\rightarrow$")
show()

t2=linspace(0,10*1e-3,2001)
Vi=cos(w1*t2)-cos(w2*t2)
t2,j,svec=sp.lsim(H_circuit,Vi,t2)
plot(t2,j)
xlabel("$t\\rightarrow$")
ylabel("$Vo\\rightarrow$")
show()
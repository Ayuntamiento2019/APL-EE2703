from cProfile import label
from os import remove
from turtle import color

from pylab import  *
from numpy import *
from scipy import integrate
def exponent(x):
    return exp(x)
def v(f,x,k):
    return f*sin(k*x)
def u(f,x,k):
    return f*cos(k*x)
def cosine(x):
    return cos(x)

x=linspace(-2*pi,4*pi,1001)

def fourier_exp():
    g= lambda k:exp(k)
    a0=float(integrate.quad(g,0,2*pi)[0]/(2*pi))
   
    coeff_exp_a=array([a0])
    coeff_exp_b=array([0])
    ans_exp=array([a0])
    for i in range(25):
        s=i+1
        a=lambda t,s:u(exp(t),t,s)
        ai=float(integrate.quad(a,0,2*pi,args=(i+1))[0]/(pi))
        coeff_exp_a=append(coeff_exp_a,ai)
        ans_exp=append(ans_exp,ai)
        b=lambda p,s:v(exp(p),p,s)
        bi=float(integrate.quad(b,0,2*pi,args=(s))[0]/(pi))
        coeff_exp_b=append(coeff_exp_b,bi)
        ans_exp=append(ans_exp,bi)
        
    return coeff_exp_a,coeff_exp_b,ans_exp
def fourier_coscos():
    g= lambda k:cos(cos(k))
    a0=float(integrate.quad(g,0,2*pi)[0])/(2*pi)
    coeff_cos_a=array([a0])
    coeff_cos_b=array([0])
    ans_cos=array([a0])
    for i in range(25):
        s=i+1
        a=lambda t,s:u(cos(cos(t)),t,s)
        ai=float(integrate.quad(a,0,2*pi,args=(s))[0])/(pi)
        coeff_cos_a=append(coeff_cos_a,ai)
        ans_cos=append(ans_cos,ai)
        b=lambda p,s:v(cos(cos(p)),p,s)
        bi=float(integrate.quad(b,0,2*pi,args=(s))[0])/(pi)
        coeff_cos_b=append(coeff_cos_b,bi)
        ans_cos=append(ans_cos,bi)
        
        
    return coeff_cos_a,coeff_cos_b,ans_cos

figure(1)
semilogy(x,exp(x),label='actual graph')
semilogy(x,exp(x%(2*pi)),label="expected fouriers series")
grid(True)
title("Q1. exp(x) vs. x & the expected fourier series (semilogy)")
xlabel("$x\\rightarrow$")
ylabel("$log(exp(x))\\rightarrow$")
legend()
show()

figure(2)
plot(x,cosine(cosine(x)),label='actual graph')
plot(x,cosine(cosine(x%(2*pi))),label="expected fouriers series")
title("Q2. cos(cos(x)) vs. x & the expected fourier series")
xlabel("$x\\rightarrow$")
ylabel("$cos(cos(x))\\rightarrow$")
grid(True)
legend()
show()
coeff_exp_a,coeff_exp_b,ans_exp=fourier_exp()
n=linspace(0,25,26)
figure(3)
semilogy(n,abs(coeff_exp_a),linestyle='None',marker='o',color='red')
semilogy(n,abs(coeff_exp_b),linestyle='None',marker='o',color='red')
title("Q3. Magnitude of fourier coefficients of exp(x) (semilog)")
xlabel("$n\\rightarrow$")
ylabel("Magnitude of fourier coefficients$\\rightarrow$")
grid(True)
show()
figure(4)
loglog(n,abs(coeff_exp_a),linestyle='None',marker='o',color='red')
loglog(n,abs(coeff_exp_b),linestyle='None',marker='o',color='red')
title("Q4. Magnitude of fourier coefficients of exp(x) (loglog)")
xlabel("$n\\rightarrow$")
ylabel("Magnitude of fourier coefficients$\\rightarrow$")
grid(True)
show()
coeff_cos_a,coeff_cos_b,ans_cos=fourier_coscos()

figure(5)
semilogy(n,abs(coeff_cos_a),linestyle='None',marker='o',color='red')
semilogy(n,abs(coeff_cos_b),linestyle='None',marker='o',color='red')
title("Q5. Magnitude of fourier coefficients of cos(cos(x)) (semilogy)")
xlabel("$n\\rightarrow$")
ylabel("Magnitude of fourier coefficients$\\rightarrow$")
grid(True)
show()

figure(6)
loglog(n,abs(coeff_cos_a),linestyle='None',marker='o',color='red')
loglog(n,abs(coeff_cos_b),linestyle='None',marker='o',color='red')
title("Q6. Magnitude of fourier coefficients of cos(cos(x)) (loglog)")
xlabel("$n\\rightarrow$")
ylabel("Magnitude of fourier coefficients$\\rightarrow$")
grid(True)
show()

coeff_exp_b=delete(coeff_exp_b,0)
coeff_cos_b=delete(coeff_cos_b,0)

t=linspace(0,2*pi,401)
t=t[:-1]
b=exponent(t) 
A=zeros((400,51)) 
A[:,0]=1 
for k in range(1,26):
    A[:,2*k-1]=cos(k*t) 
    A[:,2*k]=sin(k*t) 

c1=lstsq(A,b,rcond=None)[0]
s=linspace(0,50,51)
figure(7)
semilogy(s,abs(ans_exp),linestyle='None',marker='o',color='red',label="coeff._by_integration")
semilogy(s,abs(c1),linestyle='None',marker='o',color='green',markersize=3,label='lstq_coeff.')
title("Q7. Magnitude of fourier coefficients of exp(x) found by lstsq method (semilogy)")
xlabel("$n\\rightarrow$")
ylabel("Magnitude of fourier coefficients$\\rightarrow$")
grid(True)
show()

figure(8)
loglog(s,abs(ans_exp),linestyle='None',marker='o',color='red',label="coeff._by_integration")
loglog(s,abs(c1),linestyle='None',marker='o',color='green',markersize=3,label='lstq_coeff.')
title("Q8. Magnitude of fourier coefficients of exp(x) found by lstsq method (loglog)")
xlabel("$n\\rightarrow$")
ylabel("Magnitude of fourier coefficients$\\rightarrow$")
grid(True)
show()
b2=cos(cos(t)) 
A2=zeros((400,51)) 
A2[:,0]=1 
for k in range(1,26):
    A2[:,2*k-1]=cos(k*t) 
    A2[:,2*k]=sin(k*t) 

c2=lstsq(A2,b2,rcond=None)[0]
figure(9)
semilogy(s,abs(ans_cos),linestyle='None',marker='o',color='red',label='coeff. by integration')
semilogy(s,abs(c2),linestyle='None',marker='o',color='green',markersize=3,label='coeff. by listsq ')
title("Q9. Magnitude of fourier coefficients of cos(cos(x)) found by lstsq method (semilogy)")
xlabel("$n\\rightarrow$")
ylabel("Magnitude of fourier coefficients$\\rightarrow$")
grid(True)
legend()
show()
figure(10)
loglog(s,abs(ans_cos),linestyle='None',marker='o',color='red',label='coeff. by integration')
loglog(s,abs(c2),linestyle='None',marker='o',color='green',markersize=3,label='coeff. by listsq ')
title("Q10. Magnitude of fourier coefficients of cos(cos(x)) found by lstsq method (loglog)")
xlabel("$n\\rightarrow$")
ylabel("Magnitude of fourier coefficients$\\rightarrow$")
grid(True)
legend()
show()

dev_exp=c1-ans_exp
figure(11)
stem(s,abs(dev_exp))
title("Q11. Deviation in coefficients calculated using least squares and direct integration for exp(x) " )
xlabel("$n\\rightarrow$")
ylabel("Deviation in coefficients$\\rightarrow$")
grid(True)
show()

dev_cos=c2-ans_cos
figure(12)
stem(s,abs(dev_cos))
title("Q12. Deviation in coefficients calculated using least squares and direct integration for cos(cos(x)) " )
xlabel("$n\\rightarrow$")
ylabel("Deviation in coefficients$\\rightarrow$")
grid(True)
show()


b=exponent(x) 
A=zeros((1001,51)) 
A[:,0]=1 
for k in range(1,26):
    A[:,2*k-1]=cos(k*x) 
    A[:,2*k]=sin(k*x) 
fourier_Series_exp=dot(A,ans_exp)
figure(1)
semilogy(x,exp(x),label='actual graph')
semilogy(x,exp(x%(2*pi)),label="expected fouriers series")
grid(True)
semilogy(x,fourier_Series_exp,linestyle='None',marker='o',color='green',label='actual fourier series')
title("Q13. exp(x) vs x, the expected and real fourier series")
xlabel("$x\\rightarrow$")
ylabel("$exp(x)\\rightarrow$")
legend()
show()

b2=cos(cos(x))
A2=zeros((1001,51)) 
A2[:,0]=1 
for k in range(1,26):
    A2[:,2*k-1]=cos(k*x) 
    A2[:,2*k]=sin(k*x) 
fourier_Series_cos=dot(A2,ans_cos)
figure(2)
plot(x,cosine(cosine(x)),label='actual graph')
plot(x,cosine(cosine(x%(2*pi))),label="expected fouriers series")
plot(x,fourier_Series_cos,linestyle='None',marker='o',color='green',label='actual fourier series')
title("Q13. cos(cos(x)) vs x, the expected and real fourier series")
xlabel("$x\\rightarrow$")
ylabel("$cos(cos(x))\\rightarrow$")
grid(True)
legend()
show()
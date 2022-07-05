import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as ft
x=np.linspace(0,2*np.pi,129);x=x[:-1]
y=np.sin(5*x)
Y=ft.fftshift(ft.fft(y))/128.0
w=np.linspace(-64,63,128)
plt.figure()
plt.subplot(2,1,1)
plt.plot(w,abs(Y),lw=2)
plt.xlim([-10,10])
plt.ylabel(r"$|Y|$",size=16)
plt.title(r"Spectrum of $\sin(5t)$")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(w,np.angle(Y),'ro',lw=2)
ii=np.where(abs(Y)>1e-3)
plt.plot(w[ii],np.angle(Y[ii]),'go',lw=2)
plt.xlim([-10,10])
plt.ylabel(r"Phase of $Y$",size=16)
plt.xlabel(r"$k$",size=16)
plt.grid(True)
# plt.show()

t=np.linspace(-4*np.pi,4*np.pi,513);t=t[:-1]
y=(1+0.1*np.cos(t))*np.cos(10*t)
Y=ft.fftshift(ft.fft(y))/512.0
w=np.linspace(-64,64,513);w=w[:-1]
plt.figure()
plt.subplot(2,1,1)
plt.plot(w,abs(Y),lw=2)
plt.xlim([-15,15])
plt.ylabel(r"$|Y|$",size=16)
plt.title(r"Spectrum of $\left(1+0.1\cos\left(t\right)\right)\cos\left(10t\right)$")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(w,np.angle(Y),'ro',lw=2)
plt.xlim([-15,15])
ii=np.where(abs(Y)>1e-3)
plt.plot(w[ii],np.angle(Y[ii]),'go',lw=2)
plt.xlim([-15,15])
plt.ylabel(r"Phase of $Y$",size=16)
plt.xlabel(r"$\omega$",size=16)
plt.grid(True)
# plt.show()

t=np.linspace(-4*np.pi,4*np.pi,513);t=t[:-1]
y=np.sin(t)**3
Y= ft.fftshift(ft.fft(y))/512.0
w=np.linspace(-64,64,513);w=w[:-1]
plt.figure()
plt.subplot(2,1,1)
plt.plot(w,abs(Y),lw=2)
plt.xlim([-15,15])
plt.ylabel(r"$|Y|$",size=16)
plt.title(r"Spectrum of $\sin(t)**3$")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(w,np.angle(Y),'ro',lw=1,markersize=3)
plt.xlim([-15,15])
ii=np.where(abs(Y)>1e-3)
plt.plot(w[ii],np.angle(Y[ii]),'go',lw=1,markersize=3)
plt.xlim([-15,15])
plt.ylabel(r"Phase of $Y$",size=16)
plt.xlabel(r"$\omega$",size=16)
plt.grid(True)
# plt.show()

t=np.linspace(-4*np.pi,4*np.pi,513);t=t[:-1]
y=np.cos(t)**3
Y= ft.fftshift(ft.fft(y))/512.0
w=np.linspace(-64,64,513);w=w[:-1]
plt.figure()
plt.subplot(2,1,1)
plt.plot(w,abs(Y),lw=2)
plt.xlim([-15,15])
plt.ylabel(r"$|Y|$",size=16)
plt.title(r"Spectrum of $\cos(t)**3$")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(w,np.angle(Y),'ro',lw=1,markersize=3)
plt.xlim([-15,15])
ii=np.where(abs(Y)>1e-3)
plt.plot(w[ii],np.angle(Y[ii]),'go',lw=1,markersize=3)
plt.xlim([-15,15])
plt.ylabel(r"Phase of $Y$",size=16)
plt.xlabel(r"$\omega$",size=16)
plt.grid(True)
# plt.show()

t=np.linspace(-4*np.pi,4*np.pi,513);t=t[:-1]
y=np.cos(20*t+5*np.cos(t))
Y= ft.fftshift(ft.fft(y))/512.0
w=np.linspace(-64,64,513);w=w[:-1]
plt.figure()
plt.subplot(2,1,1)
plt.plot(w,abs(Y),lw=2)
plt.xlim([-40,40])
plt.ylabel(r"$|Y|$",size=16)
plt.title(r"Spectrum of $\cos(20*t+cos(t))$")
plt.grid(True)
plt.subplot(2,1,2)
# y_req = Y[abs(Y) > 0.001]
# w_req = w[abs( Y) > 0.001]
# plt.plot(w_req,np.angle(y_req),'ro',lw=1,markersize=1)
ii=np.where(abs(Y)>1e-3)
plt.plot(w[ii],np.angle(Y[ii]),'go',lw=1,markersize=3)
plt.xlim([-40,40])
plt.ylabel(r"Phase of $Y$",size=16)
plt.xlabel(r"$\omega$",size=16)
plt.grid(True)
# plt.show()

t=np.linspace(-2*np.pi,2*np.pi,513);t=t[:-1]
y=np.exp(-(t*t)/2)
Y= ft.fftshift(ft.fft(y))/512.0
w=np.linspace(-64,64,513);w=w[:-1]
plt.figure()
plt.subplot(2,1,1)
plt.plot(w,abs(Y),lw=2)
plt.xlim([-15,15])
plt.ylabel(r"$|Y|$",size=16)
plt.title(r"Spectrum of $\exp(-t**2/2)$")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(w,np.angle(Y),'ro',lw=1,markersize=3)
plt.xlim([-15,15])
ii=np.where(abs(Y)>1e-3)
plt.plot(w[ii],np.angle(Y[ii]),'go',lw=1,markersize=3)
plt.xlim([-15,15])
plt.ylabel(r"Phase of $Y$",size=16)
plt.xlabel(r"$\omega$",size=16)
plt.grid(True)
# plt.show()

t=np.linspace(-12*np.pi,12*np.pi,1025);t=t[:-1]
y=np.exp(-(t**2)/2)
Y= ft.fftshift(ft.fft(y))/1024.0
w=np.linspace(-64,64,1025);w=w[:-1]
plt.figure()
plt.subplot(2,1,1)
plt.plot(w,abs(Y),lw=2)
plt.xlim([-15,15])
plt.ylabel(r"$|Y|$",size=16)
plt.title(r"Spectrum of $\exp(-t**2/2)$")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(w,np.angle(Y),'ro',lw=1,markersize=3)
plt.xlim([-15,15])
ii=np.where(abs(Y)>1e-3)
plt.plot(w[ii],np.angle(Y[ii]),'go',lw=1,markersize=3)
plt.xlim([-15,15])
plt.ylabel(r"Phase of $Y$",size=16)
plt.xlabel(r"$\omega$",size=16)
plt.grid(True)
plt.show()
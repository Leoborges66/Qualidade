import numpy as np
import math

V = 11200
F = 60
h5 = 4.7
h7 = 6.7
Q = 40
VcapUn = 2400
QcapUn = 50000
Un_serie = 3

#---------------Carga-------------------
Scarga1 = 7968000
fp1 = 0.882
Z_c1 = (V**2)/Scarga1
R_c1 = Z_c1*fp1
X_c1 = Z_c1*np.sin(np.arccos(fp1))
L_c1 = X_c1/(2* np.pi * F) * 1000
print('\n-----Carga-----')
print('R =',"{:.4f}".format(R_c1),'ohm')
print('L =',"{:.4f}".format(L_c1),'mH')

#---------------Transformador-------------------
Straf = 8000000
X_c2 = 0.1*(V**2)/Straf
L_c2 = X_c2/(2* np.pi * F) * 1000
print('\n-----Impedancia Transformador------')
print('L =',"{:.4f}".format(L_c2),'mH')




#---------------Filtro de 5° ordem único-------------------
Pcap = Scarga1 * fp1
QfiH = Pcap*(np.tan(np.arccos(fp1)) - np.tan(np.arccos(0.94)))
Xfilt = (V**2)/QfiH
Xcap = (h5*2)*Xfilt/((h5*2)-1)
Qcap = (V**2)/Xcap

#Banco de capacitores-------------
Vcapn = np.sqrt(3)*Un_serie*VcapUn
Porcent = (Vcapn/V)*100 - 100
NUC = QfiH/(Un_serie*QcapUn)
NUCY = math.ceil(NUC/6)
Qcapn = 6*Un_serie*NUCY*QcapUn
Xcapn = (Vcapn**2)/Qcapn
#---------------------------------

Cn = 1/(Xcapn*2* np.pi * F)*1000000
print('\n------------Filtro de 5º único---------------')
print('Xcap =',"{:.4f}".format(Xcap),'ohn')
print('Qcap =',"{:.4f}".format(Qcap),'VAr')
print('Xcapn =',"{:.4f}".format(Xcapn),'ohn')
print('Cn =',"{:.4f}".format(Cn),'uF')

#----------Reator do Filtro-----------
Xl = Xcapn/(h5**2)
L = Xl/(2* np.pi * F) * 1000
print('\n-----Reator do Filtro------')
print('Xl =',"{:.4f}".format(Xl),'ohn')
print('L =',"{:.4f}".format(L),'mH')

#----------Resistência do Filtro-----------
R = Xl/Q
print('\n-----Resistencia------')
print('R =',"{:.4f}".format(R),'ohn')


#---------------Filtro de 5º ordem-------------------
Pcap = Scarga1 * fp1
QfiH = Pcap*(np.tan(np.arccos(fp1)) - np.tan(np.arccos(0.94)))/2
Xfilt = (V**2)/QfiH
Xcap = (h5*2)*Xfilt/((h5*2)-1)
Qcap = (V**2)/Xcap
#Banco de capacitores-------------
Vcapn = np.sqrt(3)*Un_serie*VcapUn
Porcent = (Vcapn/V)*100 - 100
NUC = QfiH/(Un_serie*QcapUn)
NUCY = math.ceil(NUC/6)
Qcapn = 6*Un_serie*NUCY*QcapUn
Xcapn = (Vcapn**2)/Qcapn
#---------------------------------
Cn = 1/(Xcapn*2* np.pi * F)*1000000
print('\n-------------Filtro 5º ordem---------------')
print('Xcap =',"{:.4f}".format(Xcap),'ohn')
print('Qcap =',"{:.4f}".format(Qcap),'VAr')
print('Xcapn =',"{:.4f}".format(Xcapn),'ohn')
print('Cn =',"{:.4f}".format(Cn),'uF')

#----------Reator do Filtro-----------
Xl5 = Xcapn/(h5**2)
L5 = Xl5/(2* np.pi * F) * 1000
print('\n-----Reator do Filtro------')
print('Xl =',"{:.4f}".format(Xl5),'ohn')
print('L =',"{:.4f}".format(L5),'mH')

#----------Resistência do Filtro-----------
R5 = Xl5/Q
print('\n-----Resistencia------')
print('R =',"{:.4f}".format(R5),'ohn')

#---------------Filtro de 7º ordem-------------------
Pcap = Scarga1 * fp1
QfiH = Pcap*(np.tan(np.arccos(fp1)) - np.tan(np.arccos(0.94)))/2
Xfilt = (V**2)/QfiH
Xcap = (h7*2)*Xfilt/((h7*2)-1)
Qcap = (V**2)/Xcap
#Banco de capacitores-------------
Vcapn = np.sqrt(3)*Un_serie*VcapUn
Porcent = (Vcapn/V)*100 - 100
NUC = QfiH/(Un_serie*QcapUn)
NUCY = math.ceil(NUC/6)
Qcapn = 6*Un_serie*NUCY*QcapUn
Xcapn = (Vcapn**2)/Qcapn
#---------------------------------
Cn = 1/(Xcapn*2* np.pi * F)*1000000
print('\n-----Filtro de 7º ordem------')
print('Xcap =',"{:.4f}".format(Xcap),'ohn')
print('Qcap =',"{:.4f}".format(Qcap),'VAr')
print('Xcapn =',"{:.4f}".format(Xcapn),'ohn')
print('Cn =',"{:.4f}".format(Cn),'uF')

#----------Reator do Filtro-----------
Xl7 = Xcapn/(h7**2)
L7 = Xl7/(2* np.pi * F) * 1000
print('\n-----Reator do Filtro------')
print('Xl =',"{:.4f}".format(Xl7),'ohn')
print('L =',"{:.4f}".format(L7),'mH')

#----------Resistência do Filtro-----------
R7 = Xl7/Q
print('\n-----Resistencia------')
print('R =',"{:.4f}".format(R7),'ohn')

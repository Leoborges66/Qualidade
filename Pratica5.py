import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import cmath
import math

V = 11200
F = 60

#---------------Carga-------------------
Scarga1 = 7968000
fp1 = 0.882
Z_c1 = (V**2)/Scarga1
R_c1 = Z_c1*fp1
X_c1 = Z_c1*np.sin(np.arccos(fp1))
L_c1 = X_c1/(2* np.pi * F) * 1000
print('\n-----Carga Pratica5-----')
print('R =',"{:.4f}".format(R_c1),'ohm')
print('L =',"{:.4f}".format(L_c1),'mH')

#---------------Transformador-------------------
Straf = 8000000
X_tr = 0.1*(V**2)/Straf
L_tr = X_tr/(2* np.pi * F) * 1000
print('\n-----Impedancia Transformador------')
print('L =',"{:.4f}".format(L_tr),'mH')

#---------------Capacitor-------------------
Pcap = Scarga1 * fp1
Q = Pcap*(np.tan(np.arccos(fp1)) - np.tan(np.arccos(0.94)))
X_cap = ((V)**2)/Q
C = 1/(X_cap*2* np.pi * F)*1000000
print('\n-----Capacitor ideal------')
print('C =',"{:.4f}".format(C),'uF')

#----------Banco de Capacitores-------------
VcapUn = 2400
QcapUn = 50000
Un_serie = 3
Vcapn = np.sqrt(3)*Un_serie*VcapUn
Porcent = (Vcapn/V)*100 - 100
print('\n-----Banco------')
print('Vcap =',"{:.4f}".format(Vcapn),'V')
print('Porcentagem acima da nominal =',"{:.2f}".format(Porcent),'%')

NUC = Q/(Un_serie*QcapUn)
print('NUC =',"{:.4f}".format(NUC))

NUCY = math.ceil(NUC/6)
print('NUCY =', NUCY)

Qcapn = 6*Un_serie*NUCY*QcapUn
print('Qcap-n =',"{:.4f}".format(Qcapn))

Xcapn = (Vcapn**2)/Qcapn
Ccap = 1/(Xcapn*2*np.pi*F)*1000000
print('Ccap =',"{:.4f}".format(Ccap),'uF')

TotalCaps = NUCY*Un_serie
print('-----Resumo------')
print('Total de capacitores =',TotalCaps)
print('Especificação =',VcapUn,'V e Potência Reativa de =',QcapUn/1000,'kVAr')

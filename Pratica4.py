import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import cmath
import math

V = 13800
F = 60
Scc1 = 10000000
Scc2 = 20000000
Scc3 = 50000000
Scc4 = 100000000

#---Cálculo do cabo de MT entre SE de entrada e SEs remotas----
R_lt = 1.47
X_lt = 0.24
D_lt = 0.7
r_lt = R_lt * D_lt
x_lt = X_lt * D_lt
L_lt = x_lt/(2* np.pi * F) * 1000
print('_________________________')
print('Dados para Simulação ATP ')
print('_________________________')
print('----------Cabo-----------')
print('R =',"{:.4f}".format(r_lt),'ohm')
print('L =',"{:.4f}".format(L_lt),'mH')

#---------------Cálculo da carga de 750[kVA]-------------------
Scarga1 = 750000
fp1 = 0.8
Z_c1 = (V**2)/Scarga1
R_c1 = Z_c1*fp1
X_c1 = Z_c1*np.sin(np.arccos(fp1))
L_c1 = X_c1/(2* np.pi * F) * 1000
print('\n-----Carga Trifásica-----')
print('R =',"{:.4f}".format(R_c1),'ohm')
print('L =',"{:.4f}".format(L_c1),'mH')

#---------------Cálculo da carga de 500[kVA]-------------------
Scarga2 = 500000
fp2 = 0.7
Z_c2 = (V**2)/Scarga2
R_c2 = Z_c2*fp2
X_c2 = Z_c2*np.sin(np.arccos(fp2))
L_c2 = X_c2/(2* np.pi * F) * 1000
print('\n-----Carga Bifásica------')
print('R =',"{:.4f}".format(R_c2),'ohm')
print('L =',"{:.4f}".format(L_c2),'mH')

#--------------Cálculo das impedâncias de Scc------------------
Zcc1 = (V**2)/Scc1
Zcc2 = (V**2)/Scc2
Zcc3 = (V**2)/Scc3
Zcc4 = (V**2)/Scc4
#Fazendo Zcc = Xcc, para R = 0, tem-se:
Lcc1 = Zcc1/(2* np.pi * F) * 1000
Lcc2 = Zcc2/(2* np.pi * F) * 1000
Lcc3 = Zcc3/(2* np.pi * F) * 1000
Lcc4 = Zcc4/(2* np.pi * F) * 1000
print('\n---Impedância de curto---')
print('Lcc1 =',"{:.4f}".format(Lcc1),'mH')
print('Lcc2 =',"{:.4f}".format(Lcc2),'mH')
print('Lcc3 =',"{:.4f}".format(Lcc3),'mH')
print('Lcc4 =',"{:.4f}".format(Lcc4),'mH')
print('_________________________')

#--------------Cálculo do Fator de Desequilíbrio----------------
def FD(Van, Oa, Vbn, Ob, Vcn, Oc):
    
    Van_rect = cmath.rect(Van, math.radians(Oa))
    Vbn_rect = cmath.rect(Vbn, math.radians(Ob))
    Vcn_rect = cmath.rect(Vcn, math.radians(Oc))
    
    a = np.exp(1j * 2 * np.pi / 3)

    V_pos = (Van_rect + a * Vbn_rect + a**2 * Vcn_rect) / 3
    V_neg = (Van_rect + a**2 * Vbn_rect + a * Vcn_rect) / 3

    V1 = cmath.polar(V_pos)
    V2 = cmath.polar(V_neg)

    FD = (V2[0] / V1[0])*100
    return FD

print('-----Scc de 10 MVA-------')

Van = 10728.58
Oa = -3.1712
Vbn = 10405.5
Ob =-127.316
Vcn = 9902.376
Oc = 116.408
FD_10 = FD(Van, Oa, Vbn, Ob, Vcn, Oc)

print("FD = {:.4f}%".format(FD_10))

print('_________________________')
print('-----Scc de 20 MVA-------')

Van = 10976.52
Oa = -1.5685
Vbn = 10793.05
Ob =-123.76
Vcn = 10522.98
Oc = 118.20
FD_20 = FD(Van, Oa, Vbn, Ob, Vcn, Oc)

print("FD = {:.4f}%".format(FD_20))

print('_________________________')
print('-----Scc de 50 MVA-------')

Van = 11126.47
Oa = -0.5713
Vbn = 11023.33
Ob = -121.46
Vcn = 10925.04
Oc = 119.45
FD_50 = FD(Van, Oa, Vbn, Ob, Vcn, Oc)

print("FD = {:.4f}%".format(FD_50))

print('_________________________')
print('-----Scc de 100 MVA-------')

Van = 11176.59
Oa = -0.2329
Vbn = 11099.13
Ob = -120.67
Vcn = 11064
Oc = 119.8956
FD_100 = FD(Van, Oa, Vbn, Ob, Vcn, Oc)

print("FD = {:.4f}%".format(FD_100))

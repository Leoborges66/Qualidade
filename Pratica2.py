import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Aula2_QEE.txt', delimiter='\t')
colunaAN = df['Voltagem AN'][:1008]
colunaBN = df['Voltagem BN'][:1008]
colunaCN = df['Voltagem CN'][:1008]

colunaAN = colunaAN.replace(',', '.', regex=True).astype(float)
colunaBN = colunaBN.replace(',', '.', regex=True).astype(float)
colunaCN = colunaCN.replace(',', '.', regex=True).astype(float)

AdequadoAN = colunaAN.loc[(colunaAN > 117) & (colunaAN < 133)].count()
PrecarioAN = colunaAN.loc[((colunaAN > 110) & (colunaAN < 117))+(colunaAN > 133) & (colunaAN < 135)].count()
CríticoAN = colunaAN.loc[(colunaAN < 110)+(colunaAN > 135)].count()

AdequadoBN = colunaBN.loc[(colunaBN > 117) & (colunaBN < 133)].count()
PrecarioBN = colunaBN.loc[((colunaBN > 110) & (colunaBN < 117))+(colunaBN > 133) & (colunaBN < 135)].count()
CríticoBN = colunaBN.loc[(colunaBN < 110)+(colunaBN > 135)].count()

AdequadoCN = colunaCN.loc[(colunaCN > 117) & (colunaCN < 133)].count()
PrecarioCN = colunaCN.loc[((colunaCN > 110) & (colunaCN < 117))+(colunaCN > 133) & (colunaCN < 135)].count()
CríticoCN = colunaCN.loc[(colunaCN < 110)+(colunaCN > 135)].count()

print('AN')
print('Adequado:',AdequadoAN,'Precário:', PrecarioAN,'Crítico:', CríticoAN)
print('BN')
print('Adequado:',AdequadoBN,'Precário:', PrecarioBN,'Crítico:', CríticoBN)
print('CN')
print('Adequado:',AdequadoCN,'Precário:', PrecarioCN,'Crítico:', CríticoCN)

DRP = (max(PrecarioAN, PrecarioBN, PrecarioCN)/1008)*100
DRC = (max(CríticoAN, CríticoBN, CríticoCN)/1008)*100

print('DRP:',"{:.2f}".format(DRP)+'%','  Limite: 3%')
print('DRC:', "{:.2f}".format(DRC)+'%','  Limite: 0,5%')

x = range(1008)
y1 = colunaAN
y2 = colunaBN
y3 = colunaCN

reta1 = np.full_like(x, 110)  
reta2 = np.full_like(x, 117) 
reta3 = np.full_like(x, 133)  
reta4 = np.full_like(x, 135) 

plt.plot(x, y1, label='AN')
plt.plot(x, y2, label='BN')
plt.plot(x, y3, label='CN')

plt.xlabel('Pontos de medição')
plt.ylabel('Tensão(V)')

plt.xlim(0, 1008)  # Define o limite do eixo X
plt.ylim(60, 160)  # Define o limite do eixo Y

plt.fill_between(x, reta1, reta2, color='yellow', alpha=0.3)
plt.fill_between(x, reta3, reta4, color='yellow', alpha=0.3, label='Região Precária')
plt.fill_between(x, reta2, reta3, color='green', alpha=0.3, label='Região Adequada')
plt.axhspan(0, 110, facecolor='red', alpha=0.3)
plt.axhspan(135, 160, facecolor='red', alpha=0.3, label='Região Crítica')

plt.title('Qualidade da Tensão')
plt.legend()

plt.show()

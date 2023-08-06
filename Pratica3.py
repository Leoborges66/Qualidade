import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk

# Função para atualizar o gráfico e exibir os resultados com base na medição selecionada
def atualizar_grafico_e_resultados():
    medição_selecionada = variavel_medição.get()
    caminho_arquivo = f'Medição {medição_selecionada}.txt'
    df = carregar_dados_medição(caminho_arquivo)
    exibir_resultados(df)

# Função para carregar os dados da medição e realizar o pré-processamento necessário
def carregar_dados_medição(caminho_arquivo):
    df = pd.read_csv(caminho_arquivo, delimiter='\t')
    primeira_data = df['Date'].iloc[0]
    count = df['Date'].value_counts()[primeira_data]

    if count != 144:
        indices_para_remover = df[df['Date'] == primeira_data].index
        df.drop(indices_para_remover, inplace=True)
    df = df.head(1008)
    df = df.reset_index(drop=True)
    return df

# Função para calcular os resultados e exibi-los
def exibir_resultados(df):
    colunaAN = df['Voltage L1 Avg'][:1008]
    colunaBN = df['Voltage L2 Avg'][:1008]
    colunaCN = df['Voltage L3 Avg'][:1008]

    AdequadoAN = colunaAN.loc[(colunaAN > 117) & (colunaAN < 133)].count()
    PrecárioAN = colunaAN.loc[((colunaAN > 110) & (colunaAN < 117))+(colunaAN > 133) & (colunaAN < 135)].count()
    CríticoAN = colunaAN.loc[(colunaAN < 110)+(colunaAN > 135)].count()

    AdequadoBN = colunaBN.loc[(colunaBN > 117) & (colunaBN < 133)].count()
    PrecárioBN = colunaBN.loc[((colunaBN > 110) & (colunaBN < 117))+(colunaBN > 133) & (colunaBN < 135)].count()
    CríticoBN = colunaBN.loc[(colunaBN < 110)+(colunaBN > 135)].count()

    AdequadoCN = colunaCN.loc[(colunaCN > 117) & (colunaCN < 133)].count()
    PrecárioCN = colunaCN.loc[((colunaCN > 110) & (colunaCN < 117))+(colunaCN > 133) & (colunaCN < 135)].count()
    CríticoCN = colunaCN.loc[(colunaCN < 110)+(colunaCN > 135)].count()

    DCR = (max(PrecárioAN, PrecárioBN, PrecárioCN) / 1008) * 100
    DRP = (max(CríticoAN, CríticoBN, CríticoCN) / 1008) * 100

    # Calcular DTT95% para as diferentes faixas
    HarmL1 = ['Volts Harmonics{} L1'.format(i) for i in range(2, 50 + 1)] 
    HarmL2 = ['Volts Harmonics{} L2'.format(i) for i in range(2, 50 + 1)] 
    HarmL3 = ['Volts Harmonics{} L3'.format(i) for i in range(2, 50 + 1)] 

    DTTpercent1 = np.sqrt(np.square(df[HarmL1]).sum(axis=1))
    DTTpercent2 = np.sqrt(np.square(df[HarmL2]).sum(axis=1))
    DTTpercent3 = np.sqrt(np.square(df[HarmL3]).sum(axis=1))

    df['DTT95_plot'] = np.maximum.reduce([DTTpercent1, DTTpercent2, DTTpercent3])

    DTT95_1 = np.percentile(DTTpercent1, 95)
    DTT95_2 = np.percentile(DTTpercent2, 95)
    DTT95_3 = np.percentile(DTTpercent3, 95)

    DTT95 = max(DTT95_1, DTT95_2, DTT95_3)

    # Calcular DTTp95% para as diferentes faixas
    
    HarmL1p = ['Volts Harmonics{} L1'.format(i) for i in range(2, 50 + 1) if i % 2 == 0 and i % 3 !=0] 
    HarmL2p = ['Volts Harmonics{} L2'.format(i) for i in range(2, 50 + 1) if i % 2 == 0 and i % 3 !=0] 
    HarmL3p = ['Volts Harmonics{} L3'.format(i) for i in range(2, 50 + 1) if i % 2 == 0 and i % 3 !=0] 

    DTTpercent1 = np.sqrt(np.square(df[HarmL1p]).sum(axis=1))
    DTTpercent2 = np.sqrt(np.square(df[HarmL2p]).sum(axis=1))
    DTTpercent3 = np.sqrt(np.square(df[HarmL3p]).sum(axis=1))
    
    df['DTTp95_plot'] = np.maximum.reduce([DTTpercent1, DTTpercent2, DTTpercent3])
    DTTp95_1 = np.percentile(DTTpercent1, 95)
    DTTp95_2 = np.percentile(DTTpercent2, 95)
    DTTp95_3 = np.percentile(DTTpercent3, 95)

    DTTp95 = max(DTTp95_1, DTTp95_2, DTTp95_3)

    # Calcular DTTi95% para as diferentes faixas
    HarmL1i = ['Volts Harmonics{} L1'.format(i) for i in range(2, 50 + 1) if i % 2 != 0 and i % 3 !=0] 
    HarmL2i = ['Volts Harmonics{} L2'.format(i) for i in range(2, 50 + 1) if i % 2 != 0 and i % 3 !=0] 
    HarmL3i = ['Volts Harmonics{} L3'.format(i) for i in range(2, 50 + 1) if i % 2 != 0 and i % 3 !=0] 

    DTTpercent1i = np.sqrt(np.square(df[HarmL1i]).sum(axis=1))
    DTTpercent2i = np.sqrt(np.square(df[HarmL2i]).sum(axis=1))
    DTTpercent3i = np.sqrt(np.square(df[HarmL3i]).sum(axis=1))

    df['DTTi95_plot'] = np.maximum.reduce([DTTpercent1i, DTTpercent2i, DTTpercent3i])

    DTTi95_1 = np.percentile(DTTpercent1i, 95)
    DTTi95_2 = np.percentile(DTTpercent2i, 95)
    DTTi95_3 = np.percentile(DTTpercent3i, 95)

    DTTi95 = max(DTTi95_1, DTTi95_2, DTTi95_3)

    # Calcular DTT3_95% para as diferentes faixas
    HarmL1_3 = ['Volts Harmonics{} L1'.format(i) for i in range(2, 50 + 1) if i % 3 == 0] 
    HarmL2_3 = ['Volts Harmonics{} L2'.format(i) for i in range(2, 50 + 1) if i % 3 == 0] 
    HarmL3_3 = ['Volts Harmonics{} L3'.format(i) for i in range(2, 50 + 1) if i % 3 == 0] 

    DTTpercent1_3 = np.sqrt(np.square(df[HarmL1_3]).sum(axis=1))
    DTTpercent2_3 = np.sqrt(np.square(df[HarmL2_3]).sum(axis=1))
    DTTpercent3_3 = np.sqrt(np.square(df[HarmL3_3]).sum(axis=1))

    df['DTT3_95_plot'] = np.maximum.reduce([DTTpercent1i, DTTpercent2i, DTTpercent3i])

    DTT3_95_1 = np.percentile(DTTpercent1_3, 95)
    DTT3_95_2 = np.percentile(DTTpercent2_3, 95)
    DTT3_95_3 = np.percentile(DTTpercent3_3, 95)

    DTT3_95 = max(DTT3_95_1, DTT3_95_2, DTT3_95_3)

    # ------------------------FD95%----------------------
    FD = df['Unbalance Avg'][:1008]
    df['FD'] = FD
    FD_COMP_SIMETRICA_95 = np.percentile(FD, 95)

    # ------------------Pst95%-------------------------------
    PstAN = df['Pst  L1'][:1008]
    media1 = PstAN.mean()
    PstAN.fillna(media1, inplace=True)

    PstBN = df['Pst  L2'][:1008]
    media2 = PstBN.mean()
    PstBN.fillna(media2, inplace=True)

    PstCN = df['Pst  L3'][:1008]
    media3 = PstCN.mean()
    PstCN.fillna(media3, inplace=True)

    df['Pst_plot'] = np.maximum.reduce([PstAN, PstBN, PstCN])
    PstAN95 = np.percentile(PstAN, 95)
    PstBN95 = np.percentile(PstBN, 95)
    PstCN95 = np.percentile(PstCN, 95)

    Pst95 = max(PstAN95, PstBN95, PstCN95)

    # Limpar resultados anteriores
    result_text.delete('1.0', tk.END)

    # Exibir os resultados
    result_text.insert(tk.END, '---------------Qualímetro do Leozao---------------\n')
    result_text.insert(tk.END, 'Fase AN\n')
    result_text.insert(tk.END, f'Adequado: {AdequadoAN}, Precário: {PrecárioAN}, Crítico: {CríticoAN}\n')
    result_text.insert(tk.END, 'Fase BN\n')
    result_text.insert(tk.END, f'Adequado: {AdequadoBN}, Precário: {PrecárioBN}, Crítico: {CríticoBN}\n')
    result_text.insert(tk.END, 'Fase CN\n')
    result_text.insert(tk.END, f'Adequado: {AdequadoCN}, Precário: {PrecárioCN}, Crítico: {CríticoCN}\n')
    result_text.insert(tk.END, '\nDCR:\t\t' + "{:.2f}".format(DCR) + '%\t\tLimite: 3%\n')
    result_text.insert(tk.END, 'DRP:\t\t' + "{:.2f}".format(DRP) + '%\t\tLimite: 0.5%\n')
    result_text.insert(tk.END, 'DTT95%:\t\t' + "{:.2f}".format(DTT95)+'%' + '\t\tLimite: 10%\n')
    result_text.insert(tk.END, 'DTTp95%:\t\t' + "{:.2f}".format(DTTp95)+'%' + '\t\tLimite: 2.5%\n')
    result_text.insert(tk.END, 'DTTi95%:\t\t' + "{:.2f}".format(DTTi95)+'%' + '\t\tLimite: 7.5%\n')
    result_text.insert(tk.END, 'DTT3_95%:\t\t' + "{:.2f}".format(DTT3_95)+'%' + '\t\tLimite: 6.5%\n')
    result_text.insert(tk.END, 'FD95%:\t\t' + "{:.2f}".format(FD_COMP_SIMETRICA_95)+'%' + '\t\tLimite: 3%\n')
    result_text.insert(tk.END, 'Pst95%:\t\t' + "{:.2f}".format(Pst95)+'%' + '\t\tLimite: 1pu\n')

    # ----------------------Plot Vrms e faixas-----------------------------
    x = range(1008)
    y1 = colunaAN
    y2 = colunaBN
    y3 = colunaCN

    reta1 = np.full_like(x, 110)
    reta2 = np.full_like(x, 117)
    reta3 = np.full_like(x, 133)
    reta4 = np.full_like(x, 135)

    plt.figure(figsize=(10, 6))

    plt.plot(x, y1, label='AN', color='blue')
    plt.plot(x, y2, label='BN', color='green')
    plt.plot(x, y3, label='CN', color='red')

    plt.xlabel('Pontos de medição')
    plt.ylabel('Tensão (V)')
    plt.xlim(0, 1008)  # Define o limite do eixo X
    plt.ylim(60, 160)  # Define o limite do eixo Y

    plt.fill_between(x, reta1, reta2, color='yellow', alpha=0.3)
    plt.fill_between(x, reta3, reta4, color='yellow',
                     alpha=0.3, label='Região Precária')
    plt.fill_between(x, reta2, reta3, color='green',
                     alpha=0.3, label='Região Adequada')
    plt.axhspan(0, 110, facecolor='red', alpha=0.3)
    plt.axhspan(135, 160, facecolor='red', alpha=0.3, label='Região Crítica')

    plt.title('Qualidade da Tensão')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

    # ------------------Plot DTT, DTTp, DTTi, DTT3, FD e Pst---------------------

    def plot_daily_percentile(ax, df, column_name, ylabel, color):
        df_grouped = df.groupby('Date')[column_name].apply(
            lambda x: np.percentile(x, 95)).reset_index()

        ax.bar(range(len(df_grouped)), df_grouped[column_name], color=color)

        ax.set_xlabel('Dia')
        ax.set_ylabel(ylabel)
        ax.set_title(f'{ylabel} diário')
        ax.set_xticks(range(len(df_grouped)))
        ax.set_xticklabels(df_grouped['Date'], rotation=0)
        ax.grid(True)

    fig, axs = plt.subplots(3, 2, figsize=(12, 12))
    fig.tight_layout(pad=4.0)

    plot_daily_percentile(axs[0, 0], df, 'DTT95_plot', 'DTT95%', 'blue')
    plot_daily_percentile(axs[0, 1], df, 'DTTp95_plot', 'DTTp95%', 'green')
    plot_daily_percentile(axs[1, 0], df, 'DTTi95_plot', 'DTTi95%', 'red')
    plot_daily_percentile(axs[1, 1], df, 'DTT3_95_plot', 'DTT395%', 'orange')
    plot_daily_percentile(axs[2, 0], df, 'FD', 'FD95%', 'purple')
    plot_daily_percentile(axs[2, 1], df, 'Pst_plot', 'Pst95% em pu', 'brown')

    plt.show()

# Criar a janela principal
window = tk.Tk()
window.title("Painel de Controle de Medição")

# Criar um menu suspenso para selecionar a medição
variavel_medição = tk.StringVar()
label_medição = ttk.Label(window, text="Selecione a Medição:")
label_medição.pack()
dropdown_medição = ttk.Combobox(window, textvariable=variavel_medição)
dropdown_medição['values'] = [str(i) for i in range(1, 28)]
dropdown_medição.pack()

# Criar um botão para atualizar o gráfico e exibir os resultados
botão_atualizar = ttk.Button(window, text="Atualizar Gráfico e Resultados", command=atualizar_grafico_e_resultados)
botão_atualizar.pack()

# Criar um widget de texto para exibir os resultados
result_text = tk.Text(window, height=20, width=50)
result_text.pack()

def update_additional_plot_and_results():
    medição_selecionada2 = additional_measurement_var.get()
    caminho_arquivo = f'Medições VTCD/Medição {medição_selecionada2}.txt'
    df_VTCD = load_additional_measurement_data(caminho_arquivo)
    display_additional_results(df_VTCD)

# Criar uma função para carregar os dados da medição adicional e realizar o pré-processamento necessário
def load_additional_measurement_data(caminho):
    df_VTCD = pd.read_csv(caminho, delimiter='\t', index_col=False, encoding='latin-1')
    return df_VTCD

# Criar uma função para exibir os resultados da medição adicional
def display_additional_results(df_VTCD):
    # ---------------------------FI-------------------------------------------
    nivel_pu = df_VTCD['Nível [pu]'].str.replace(',', '.').astype(float)
    df_VTCD['Nível [V]'] = df_VTCD['Nível [V]'].str.replace('---', '0')
    nivel_V = df_VTCD['Nível [V]'].str.replace(',', '.').astype(float)
    duracao = df_VTCD['Duração [s]'].str.replace(',', '.').astype(float)
    regiao = []

    for npu, dur in zip(nivel_pu, duracao):
        if 0.85 <= npu <= 0.9 and 0.01667 <= dur <= 180:
            regiao.append('A')
        elif 0.8 <= npu <= 0.85 and 0.01667 <= dur <= 0.6:
            regiao.append('A')
        elif 0.6 <= npu <= 0.8 and 0.01667 <= dur <= 0.1:
            regiao.append('B')
        elif 0.4 <= npu <= 0.6 and 0.01667 <= dur <= 0.1:
            regiao.append('C')
        elif 0.4 <= npu <= 0.8 and 0.1 <= dur <= 0.6:
            regiao.append('D')
        elif npu < 0.4 and 0.01667 <= dur <= 0.6:
            regiao.append('E')
        elif npu < 0.7 and 0.6 <= dur <= 180:
            regiao.append('F')
        elif 0.7 <= npu <= 0.85 and 0.6 <= dur <= 180:
            regiao.append('G')
        elif npu > 1.1 and 0.01667 <= dur <= 0.6:
            regiao.append('H')
        elif npu > 1.1 and 0.6 <= dur <= 180:
            regiao.append('I')
        else:
            regiao.append('Outra')
    df_VTCD['regiao'] = regiao

    fpond = {
        'A': 0.00,
        'B': 0.04,
        'C': 0.07,
        'D': 0.15,
        'E': 0.25,
        'F': 0.36,
        'G': 0.07,
        'H': 0.02,
        'I': 0.04,
        'Outra': 0.00
    }

    quantidades = df_VTCD['regiao'].value_counts().sort_index()
    somatorio = (quantidades * pd.Series(fpond)).sum()
    nivel_V = nivel_V.mean()

    if 2300 <= nivel_V <= 69000:
        FIbase = 2.13
    elif 69000 <= nivel_V <= 230000:
        FIbase = 1.42

    FI = somatorio/FIbase

    # Limpar resultados anteriores
    additional_result_text.delete('1.0', tk.END)
    
    # Exibir os resultados
    additional_result_text.insert(tk.END, 'FI:\t\t' + "{:.2f}".format(FI)+'pu' + '\t\tLimite: 1pu\n')

    # --------------------------------Plot VTCD---------------------------------------
    df_VTCD['Duração [s]'] = df_VTCD['Duração [s]'].str.replace(
        ',', '.').astype(float)
    df_VTCD['Nível [pu]'] = df_VTCD['Nível [pu]'].str.replace(
        ',', '.').astype(float)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df_VTCD['Duração [s]'], df_VTCD['Nível [pu]'],
            marker='o', linestyle='', color='blue', markersize=5)
    for i, txt in enumerate(df_VTCD.index):
        ax.annotate(txt, (df_VTCD['Duração [s]'][i], df_VTCD['Nível [pu]']
                    [i]), textcoords="offset points", xytext=(0, 5), ha='center')
    ax.set_xscale('log')
    ax.set_xlabel('Duração [s]')
    ax.set_ylabel('Nível [pu]')
    ax.set_title('Gráfico VTCD')
    ax.grid(True)
    y = ax.get_ylim()[1]
    ax.fill_between([0.016, 180], 0.85, 0.9, alpha=0.3,
                    color='gray', label='Regiões A')
    ax.fill_between([0.016, 0.6], 0.8, 0.85, alpha=0.3,
                    color='gray')
    ax.fill_between([0.016, 0.1], 0.6, 0.8, alpha=0.3,
                    color='orange', label='Regiões B')
    ax.fill_between([0.016, 0.1], 0.4, 0.6, alpha=0.3,
                    color='blue', label='Regiões C')
    ax.fill_between([0.1, 0.6], 0.4, 0.8, alpha=0.3,
                    color='green', label='Regiões D')
    ax.fill_between([0.016, 0.6], 0.1, 0.4, alpha=0.3,
                    color='violet', label='Regiões E')
    ax.fill_between([0.6, 180], 0.1, 0.7, alpha=0.3,
                    color='Purple', label='Regiões F')
    ax.fill_between([0.6, 180], 0.7, 0.85, alpha=0.3,
                    color='yellow', label='Regiões G')
    ax.fill_between([0.016, 0.6], 1.1, y, alpha=0.3,
                    color='brown', label='Regiões H')
    ax.fill_between([0.6, 180], 1.1, y, alpha=0.3,
                    color='pink', label='Regiões I')
    plt.margins(0.05)
    ax.legend(loc='upper right')

    plt.tight_layout()
    plt.show()
    
# Criar uma nova janela para selecionar as medições adicionais
additional_window = tk.Toplevel(window)
additional_window.title("VTCD")

# Criar uma dropdown para selecionar a medição adicional
additional_measurement_var = tk.StringVar()
additional_measurement_label = ttk.Label(additional_window, text="Selecione a Medição:")
additional_measurement_label.pack()
additional_measurement_dropdown = ttk.Combobox(additional_window, textvariable=additional_measurement_var)
additional_measurement_dropdown['values'] = [str(i) for i in range(1, 9)]
additional_measurement_dropdown.pack()

# Criar um botão para atualizar o gráfico e exibir os resultados para a medição adicional
additional_update_button = ttk.Button(additional_window, text="Atualizar Gráfico e Resultados", command=update_additional_plot_and_results)
additional_update_button.pack()

# Criar uma área de texto para exibir os resultados da medição adicional
additional_result_text = tk.Text(additional_window, height=10, width=50)
additional_result_text.pack()

# Executar o loop de eventos da interface gráfica
window.mainloop()

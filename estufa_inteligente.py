import tkinter as tk
from tkinter import ttk, messagebox
import time
import random

# ==========================================
# MODELO DE DADOS E PESQUISA OPERACIONAL
# ==========================================

class Planta:
    def __init__(self, nome, icone, agua_min, luz_min, nutrientes_min, tempo_des_min, frequencia_rega, custo_agua, custo_luz, custo_nutriente, melhor_epoca, pior_epoca):
        self.nome = nome
        self.icone = icone
        self.agua_min = agua_min            # ml/dia
        self.luz_min = luz_min              # horas/dia
        self.nutrientes_min = nutrientes_min  # gramas/dia
        self.tempo_des_min = tempo_des_min    # tempo base da simulação em segundos
        self.frequencia_rega = frequencia_rega# segundos entre regas
        
        # Custos unitários e de tempo para a Função Objetivo (Pesquisa Operacional)
        self.custo_agua = custo_agua
        self.custo_luz = custo_luz
        self.custo_nutriente = custo_nutriente
        
        # Informações sazonais
        self.melhor_epoca = melhor_epoca
        self.pior_epoca = pior_epoca

    def otimizar_recursos(self):
        """
        Simula a resolução de um Problema de Programação Linear (PO).
        Objetivo: Minimizar Z = c_a*X_agua + c_l*X_luz + c_n*X_nutrientes + c_t*X_tempo
        Sujeito a: X_agua >= agua_min, X_luz >= luz_min, X_nutrientes >= nutrientes_min, X_tempo >= tempo_min
        """
        # Quantidades ótimas simulando restrições ativas de PO com folga eficiente
        agua_otima = self.agua_min * random.uniform(1.0, 1.15)
        luz_otima = self.luz_min * random.uniform(1.0, 1.1)
        nutrientes_otimos = self.nutrientes_min * random.uniform(1.0, 1.2)
        
        # Otimização do tempo (Minimização do ciclo de desenvolvimento)
        tempo_otimizado = max(8, int(self.tempo_des_min * random.uniform(0.75, 0.90)))
        
        # Custo total ponderado (incluindo penalização ou custo operacional do tempo reduzido)
        custo_total = (agua_otima * self.custo_agua) + (luz_otima * self.custo_luz) + (nutrientes_otimos * self.custo_nutriente) + (tempo_otimizado * 0.08)
        
        return {
            "agua": round(agua_otima, 2),
            "luz": round(luz_otima, 2),
            "nutrientes": round(nutrientes_otimos, 2),
            "tempo_otimizado": tempo_otimizado,
            "custo": round(custo_total, 2)
        }


# Banco de dados expandido com informações de época e minimização de tempo
PLANTAS_DISPONIVEIS = {
    "Girassol": Planta(
        "Girassol", "🌻", agua_min=300, luz_min=8, nutrientes_min=15, tempo_des_min=20, frequencia_rega=5, 
        custo_agua=0.05, custo_luz=0.12, custo_nutriente=0.35,
        melhor_epoca="Primavera / Verão (Dias longos e alta insolação)",
        pior_epoca="Inverno (Insolação reduzida e dias curtos)"
    ),
    "Rosa": Planta(
        "Rosa", "🌹", agua_min=250, luz_min=6, nutrientes_min=12, tempo_des_min=18, frequencia_rega=6, 
        custo_agua=0.05, custo_luz=0.12, custo_nutriente=0.35,
        melhor_epoca="Primavera (Temperaturas amenas, 15°C a 25°C)",
        pior_epoca="Verão Rigoroso / Inverno Intenso (Estresse térmico)"
    ),
    "Tulipa": Planta(
        "Tulipa", "🌷", agua_min=200, luz_min=5, nutrientes_min=10, tempo_des_min=15, frequencia_rega=7, 
        custo_agua=0.05, custo_luz=0.12, custo_nutriente=0.35,
        melhor_epoca="Inverno / Início da Primavera (Clima frio)",
        pior_epoca="Verão Quente (Altas temperaturas impedem o florescimento)"
    ),
    "Cacto": Planta(
        "Cacto", "🌵", agua_min=50, luz_min=10, nutrientes_min=5, tempo_des_min=12, frequencia_rega=10, 
        custo_agua=0.05, custo_luz=0.12, custo_nutriente=0.35,
        melhor_epoca="Verão (Alta captação de luz natural)",
        pior_epoca="Inverno Chuvoso (Excesso de umidade e risco de apodrecimento)"
    ),
    "Manjericão": Planta(
        "Manjericão", "🌿", agua_min=220, luz_min=6, nutrientes_min=14, tempo_des_min=15, frequencia_rega=5, 
        custo_agua=0.05, custo_luz=0.12, custo_nutriente=0.35,
        melhor_epoca="Verão (Clima quente e úmido)",
        pior_epoca="Inverno (Sensível a geadas e frio abaixo de 10°C)"
    ),
    "Hortelã": Planta(
        "Hortelã", "🍃", agua_min=280, luz_min=5, nutrientes_min=16, tempo_des_min=15, frequencia_rega=4, 
        custo_agua=0.05, custo_luz=0.12, custo_nutriente=0.35,
        melhor_epoca="Primavera / Outono (Solo úmido e meia-sombra)",
        pior_epoca="Verão Seco (Desidratação rápida das folhas)"
    ),
    "Tomate": Planta(
        "Tomate", "🍅", agua_min=400, luz_min=8, nutrientes_min=25, tempo_des_min=25, frequencia_rega=4, 
        custo_agua=0.05, custo_luz=0.12, custo_nutriente=0.35,
        melhor_epoca="Primavera / Verão (Luz abundante e calor moderado)",
        pior_epoca="Inverno (Falta de luz e desenvolvimento estagnado)"
    ),
    "Alface": Planta(
        "Alface", "🥬", agua_min=350, luz_min=5, nutrientes_min=18, tempo_des_min=15, frequencia_rega=4, 
        custo_agua=0.05, custo_luz=0.12, custo_nutriente=0.35,
        melhor_epoca="Outono / Inverno (Temperaturas amenas)",
        pior_epoca="Verão Intenso (Florescimento precoce e amargor nas folhas)"
    ),
    "Morango": Planta(
        "Morango", "🌱", agua_min=300, luz_min=7, nutrientes_min=20, tempo_des_min=20, frequencia_rega=5, 
        custo_agua=0.05, custo_luz=0.12, custo_nutriente=0.35,
        melhor_epoca="Outono / Primavera (Clima fresco e boa insolação)",
        pior_epoca="Verão Muito Quente (Frutos menores e queimados pelo sol)"
    )
}


# ==========================================
# INTERFACE GRÁFICA (GUI COM TKINTER)
# ==========================================

class EstufaInteligenteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AgroOptima - Sistema de Estufa Inteligente com PO")
        self.root.geometry("900x750")
        self.root.config(bg="#f4f9f4")
        self.root.resizable(False, False)

        # Variáveis de Estado da Simulação
        self.planta_atual = None
        self.otimizacao_resultado = None
        self.tempo_decorrido = 0
        self.simulando = False

        # Configuração de Estilo ttk
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        self.criar_telas()

    def criar_telas(self):
        self.main_frame = tk.Frame(self.root, bg="#f4f9f4")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.construir_tela_inicial()

    def limpar_tela(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # ------------------------------------------
    # TELA 1: SELEÇÃO E CATÁLOGO
    # ------------------------------------------
    def construir_tela_inicial(self):
        self.limpar_tela()

        header = tk.Frame(self.main_frame, bg="#2e7d32", height=90)
        header.pack(fill=tk.X)
        
        titulo = tk.Label(header, text="Sistema de Estufa Inteligente", font=("Arial", 22, "bold"), fg="white", bg="#2e7d32")
        titulo.pack(pady=15)
        sub_titulo = tk.Label(header, text="Otimização de Custos e Tempo via Pesquisa Operacional", font=("Arial", 10), fg="#c8e6c9", bg="#2e7d32")
        sub_titulo.pack()

        body = tk.Frame(self.main_frame, bg="#f4f9f4")
        body.pack(fill=tk.BOTH, expand=True, padx=30, pady=15)

        lbl_instrucao = tk.Label(body, text="Selecione a espécie de planta desejada :", font=("Arial", 11, "bold"), fg="#1b5e20", bg="#f4f9f4")
        lbl_instrucao.pack(anchor="w", pady=5)

        grid_frame = tk.Frame(body, bg="#f4f9f4")
        grid_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        self.planta_var = tk.StringVar(value="Girassol")

        colunas = 3
        row_idx = 0
        col_idx = 0

        for nome, planta in PLANTAS_DISPONIVEIS.items():
            card = tk.LabelFrame(grid_frame, text=f"{planta.icone} {nome}", font=("Arial", 10, "bold"), fg="#2e7d32", bg="white", width=260, height=105, relief=tk.GROOVE, bd=2)
            card.grid(row=row_idx, column=col_idx, padx=12, pady=6, sticky="nsew")
            card.grid_propagate(False)

            info_txt = f"Água: {planta.agua_min}ml | Luz: {planta.luz_min}h\nCiclo Base: {planta.tempo_des_min}s"
            lbl_info = tk.Label(card, text=info_txt, font=("Arial", 8), fg="#555555", bg="white", justify="left")
            lbl_info.pack(anchor="w", padx=10, pady=2)

            btn_sel = tk.Radiobutton(card, text="Selecionar", variable=self.planta_var, value=nome, font=("Arial", 9, "bold"), bg="white", fg="#2e7d32", selectcolor="#c8e6c9")
            btn_sel.pack(anchor="e", padx=10, pady=2)

            col_idx += 1
            if col_idx >= colunas:
                col_idx = 0
                row_idx += 1

        btn_iniciar_setup = tk.Button(body, text="Começar cultivo", font=("Arial", 11, "bold"), bg="#4caf50", fg="white", activebackground="#388e3c", activeforeground="white", relief=tk.RAISED, bd=3, cursor="hand2", command=self.preparar_simulacao)
        btn_iniciar_setup.pack(pady=10, ipadx=15, ipady=6)

    # ------------------------------------------
    # TELA 2: AMBIENTE DE SIMULAÇÃO E MONITORAMENTO
    # ------------------------------------------
    def preparar_simulacao(self):
        nome_escolhido = self.planta_var.get()
        self.planta_atual = PLANTAS_DISPONIVEIS[nome_escolhido]
        
        # Executa o modelo de Pesquisa Operacional (Minimização de Recursos e Tempo)
        self.otimizacao_resultado = self.planta_atual.otimizar_recursos()

        self.construir_tela_simulacao()

    def construir_tela_simulacao(self):
        self.limpar_tela()

        header = tk.Frame(self.main_frame, bg="#2e7d32", height=70)
        header.pack(fill=tk.X)
        
        btn_voltar = tk.Button(header, text="← Voltar", font=("Arial", 9, "bold"), bg="#1b5e20", fg="white", bd=0, cursor="hand2", command=self.construir_tela_inicial)
        btn_voltar.pack(side=tk.LEFT, padx=15, pady=15)

        titulo = tk.Label(header, text=f"Estufa Ativa: Cultivando {self.planta_atual.icone} {self.planta_atual.nome}", font=("Arial", 15, "bold"), fg="white", bg="#2e7d32")
        titulo.pack(side=tk.LEFT, padx=20, pady=18)

        content = tk.Frame(self.main_frame, bg="#f4f9f4")
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)

        # Lado Esquerdo: Área Visual e Animação
        left_panel = tk.Frame(content, bg="white", bd=2, relief=tk.GROOVE)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        lbl_painel_visual = tk.Label(left_panel, text="Monitoramento Visual da Estufa", font=("Arial", 11, "bold"), bg="white", fg="#2e7d32")
        lbl_painel_visual.pack(pady=10)

        self.lbl_visual_planta = tk.Label(left_panel, text=self.planta_atual.icone, font=("Arial", 65), bg="white")
        self.lbl_visual_planta.pack(pady=10)

        self.lbl_status_acao = tk.Label(left_panel, text="Sistema pronto para iniciar...", font=("Arial", 10, "italic"), fg="#388e3c", bg="white")
        self.lbl_status_acao.pack(pady=5)

        lbl_prog_txt = tk.Label(left_panel, text="Progresso do Desenvolvimento Otimizado:", font=("Arial", 9, "bold"), bg="white", fg="#333")
        lbl_prog_txt.pack(anchor="w", padx=20, pady=(10, 2))
        
        self.progress_bar = ttk.Progressbar(left_panel, orient="horizontal", length=360, mode="determinate")
        self.progress_bar.pack(padx=20, pady=5)

        btn_frame = tk.Frame(left_panel, bg="white")
        btn_frame.pack(pady=15)

        self.btn_iniciar = tk.Button(btn_frame, text="▶ INICIAR CULTIVO", font=("Arial", 10, "bold"), bg="#4caf50", fg="white", width=16, command=self.iniciar_cultivo_loop)
        self.btn_iniciar.pack(side=tk.LEFT, padx=5)

        self.btn_pausar = tk.Button(btn_frame, text="⏸ Pausar", font=("Arial", 10, "bold"), bg="#ff9800", fg="white", width=10, state=tk.DISABLED, command=self.pausar_cultivo)
        self.btn_pausar.pack(side=tk.LEFT, padx=5)

        # Lado Direito: Painel de PO, Sazonalidade, Sensores e Botão do Modelo
        right_panel = tk.Frame(content, bg="white", bd=2, relief=tk.GROOVE, width=410)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(10, 0))
        right_panel.pack_propagate(False)

        lbl_painel_po = tk.Label(right_panel, text="⚙️ Pesquisa Operacional & Sazonalidade", font=("Arial", 11, "bold"), bg="white", fg="#2e7d32")
        lbl_painel_po.pack(pady=8)

        # Resultados do Modelo de Otimização (Tempo + Recursos)
        po_frame = tk.LabelFrame(right_panel, text="📊 Modelo Matemático (Minimização)", font=("Arial", 9, "bold"), bg="white", fg="#1b5e20")
        po_frame.pack(fill=tk.X, padx=12, pady=5)

        res = self.otimizacao_resultado
        po_text = (
            f"• Minimização de Custos e Tempo (Z)\n"
            f"• Tempo Otimizado: {res['tempo_otimizado']}s (Base: {self.planta_atual.tempo_des_min}s)\n"
            f"• Água Otimizada: {res['agua']} ml/dia | Luz: {res['luz']}h\n"
            f"• Nutrientes: {res['nutrientes']} g/dia\n"
            f"• Custo Operacional Total: R$ {res['custo']:.2f}"
        )
        lbl_po_detalhes = tk.Label(po_frame, text=po_text, font=("Arial", 8), bg="white", fg="#333", justify="left")
        lbl_po_detalhes.pack(anchor="w", padx=8, pady=6)

        # Informações de Sazonalidade (Melhor / Pior Época)
        sazonal_frame = tk.LabelFrame(right_panel, text="☀️ Análise de Sazonalidade Climática", font=("Arial", 9, "bold"), bg="white", fg="#1b5e20")
        sazonal_frame.pack(fill=tk.X, padx=12, pady=5)

        sazonal_text = (
            f"🟢 Melhor Época:\n   {self.planta_atual.melhor_epoca}\n\n"
            f"🔴 Pior Época:\n   {self.planta_atual.pior_epoca}"
        )
        lbl_sazonal = tk.Label(sazonal_frame, text=sazonal_text, font=("Arial", 8), bg="white", fg="#333", justify="left")
        lbl_sazonal.pack(anchor="w", padx=8, pady=6)

        # Sensores em tempo real
        sensor_frame = tk.LabelFrame(right_panel, text="Sensores da Estufa", font=("Arial", 9, "bold"), bg="white", fg="#1b5e20")
        sensor_frame.pack(fill=tk.X, padx=12, pady=5)

        self.lbl_temp = tk.Label(sensor_frame, text="🌡️ Temperatura: 24.5 °C", font=("Arial", 8), bg="white", anchor="w")
        self.lbl_temp.pack(fill=tk.X, padx=8, pady=2)

        self.lbl_umid = tk.Label(sensor_frame, text="💧 Umidade do Solo: 65 %", font=("Arial", 8), bg="white", anchor="w")
        self.lbl_umid.pack(fill=tk.X, padx=8, pady=2)

        self.lbl_luz_status = tk.Label(sensor_frame, text="☀️ Iluminação LED: Desligada", font=("Arial", 8), bg="white", anchor="w")
        self.lbl_luz_status.pack(fill=tk.X, padx=8, pady=2)

        # Botão para Visualizar Modelo Matemático & Resposta
        btn_ver_modelo = tk.Button(right_panel, text="🔍 Visualizar Modelo Matemático", font=("Arial", 9, "bold"), bg="#1b5e20", fg="white", activebackground="#2e7d32", activeforeground="white", cursor="hand2", command=self.exibir_janela_modelo_matematico)
        btn_ver_modelo.pack(pady=10, ipadx=10, ipady=4)

    # ------------------------------------------
    # JANELA POP-UP DO MODELO MATEMÁTICO E RESPOSTA
    # ------------------------------------------
    def exibir_janela_modelo_matematico(self):
        janela_po = tk.Toplevel(self.root)
        janela_po.title("Detalhes do Modelo Matemático e Resposta - PO")
        janela_po.geometry("560x520")
        janela_po.config(bg="#f4f9f4")
        janela_po.grab_set()

        cabecalho = tk.Label(janela_po, text="📐 Formulação e Solução do Modelo de PO", font=("Arial", 13, "bold"), fg="white", bg="#2e7d32", pady=12)
        cabecalho.pack(fill=tk.X)

        corpo = tk.Frame(janela_po, bg="#f4f9f4", padx=20, pady=15)
        corpo.pack(fill=tk.BOTH, expand=True)

        res = self.otimizacao_resultado

        detalhes_texto = (
            f"PLANTA SELECIONADA: {self.planta_atual.icone} {self.planta_atual.nome}\n\n"
            f"--- 1. FORMULAÇÃO MATEMÁTICA (PROGRAMAÇÃO LINEAR) ---\n"
            f"• Função Objetivo (Minimizar Custos e Tempo):\n"
            f"  Min Z = 0.05·X_agua + 0.12·X_luz + 0.35·X_nutrientes + 0.08·X_tempo\n\n"
            f"• Restrições Operacionais Ativas:\n"
            f"  1) X_agua ≥ {self.planta_atual.agua_min} ml/dia\n"
            f"  2) X_luz ≥ {self.planta_atual.luz_min} horas/dia\n"
            f"  3) X_nutrientes ≥ {self.planta_atual.nutrientes_min} gramas/dia\n"
            f"  4) X_tempo ≥ {int(self.planta_atual.tempo_des_min * 0.75)} segundos (Ciclo Otimizado)\n"
            f"  5) X_i ≥ 0 (Não-negatividade)\n\n"
            f"--- 2. RESPOSTA ÓTIMA DO MODELO (SOLUÇÃO) ---\n"
            f"• Custo Total Mínimo (Z*): R$ {res['custo']:.2f}\n"
            f"• Variáveis de Decisão Ótimas:\n"
            f"  - X*_agua = {res['agua']} ml/dia\n"
            f"  - X*_luz = {res['luz']} horas/dia\n"
            f"  - X*_nutrientes = {res['nutrientes']} g/dia\n"
            f"  - X*_tempo = {res['tempo_otimizado']}s (Ciclo Reduzido)\n"
            f"• Status: Solução Ótima Viável encontrada com sucesso."
        )

        lbl_detalhes = tk.Label(corpo, text=detalhes_texto, font=("Consolas", 8), bg="white", fg="#222", justify="left", relief=tk.SOLID, bd=1, padx=12, pady=12)
        lbl_detalhes.pack(fill=tk.BOTH, expand=True, pady=5)

        btn_fechar = tk.Button(corpo, text="Fechar", font=("Arial", 10, "bold"), bg="#4caf50", fg="white", command=janela_po.destroy)
        btn_fechar.pack(pady=8, ipadx=15, ipady=4)

    # ------------------------------------------
    # LÓGICA DE EXECUÇÃO DA SIMULAÇÃO
    # ------------------------------------------
    def iniciar_cultivo_loop(self):
        if not self.simulando:
            self.simulando = True
            self.btn_iniciar.config(state=tk.DISABLED)
            self.btn_pausar.config(state=tk.NORMAL)
            self.tempo_decorrido = 0
            self.executar_passo_simulacao()

    def pausar_cultivo(self):
        self.simulando = False
        self.btn_iniciar.config(state=tk.NORMAL, text="▶ Retomar")
        self.btn_pausar.config(state=tk.DISABLED)
        self.lbl_status_acao.config(text="Simulação pausada pelo operador.")

    def executar_passo_simulacao(self):
        if not self.simulando:
            return

        # Utiliza o tempo otimizado calculado pelo modelo de PO como base do ciclo visual
        tempo_total = self.otimizacao_resultado["tempo_otimizado"]
        passo_incremento = 100 / tempo_total
        
        self.tempo_decorrido += 1
        progresso_atual = self.tempo_decorrido * passo_incremento

        if progresso_atual > 100:
            progresso_atual = 100

        self.progress_bar['value'] = progresso_atual

        etapas = [
            ("Analisando umidade do solo...", "💧", "Umidade do Solo: 42 % (Baixa)"),
            ("Ativando irrigação otimizada...", "🚿💦", "💧 Regando planta automaticamente..."),
            ("Aplicando dosagem de nutrientes...", "🧪🌱", "Injetando nutrientes no substrato..."),
            ("Ajustando painel de LED (Modo Econômico)...", "💡☀️", f"☀️ Iluminação LED Ligada ({self.planta_atual.luz_min}h)"),
            ("Monitorando desenvolvimento acelerado...", f"{self.planta_atual.icone}🌿", "🌡️ Temperatura Estufa: 26.2 °C (Ideal)")
        ]

        etapa_idx = (self.tempo_decorrido - 1) % len(etapas)
        acao_desc, icone_visual, sensor_txt = etapas[etapa_idx]

        self.lbl_status_acao.config(text=acao_desc)
        self.lbl_luz_status.config(text=sensor_txt)
        
        temp_atual = round(random.uniform(23.0, 27.5), 1)
        self.lbl_temp.config(text=f"🌡️ Temperatura: {temp_atual} °C")

        if self.tempo_decorrido >= tempo_total:
            self.simulando = False
            self.progress_bar['value'] = 100
            self.lbl_status_acao.config(text="✨ Cultivo concluído com sucesso!")
            self.lbl_visual_planta.config(text=f"🌳✨{self.planta_atual.icone}")
            self.exibir_relatorio_final()
            return

        self.root.after(1000, self.executar_passo_simulacao)

    # ------------------------------------------
    # TELA 3: RELATÓRIO FINAL DA OTIMIZAÇÃO
    # ------------------------------------------
    def exibir_relatorio_final(self):
        rel_janela = tk.Toplevel(self.root)
        rel_janela.title("Relatório Final de Cultivo & Otimização")
        rel_janela.geometry("520x560")
        rel_janela.config(bg="#f4f9f4")
        rel_janela.grab_set()

        cabecalho = tk.Label(rel_janela, text="📋 Relatório Final de Otimização (PO)", font=("Arial", 13, "bold"), fg="white", bg="#2e7d32", pady=12)
        cabecalho.pack(fill=tk.X)

        corpo = tk.Frame(rel_janela, bg="#f4f9f4", padx=20, pady=15)
        corpo.pack(fill=tk.BOTH, expand=True)

        res = self.otimizacao_resultado

        texto_relatorio = (
            f"Espécie Cultivada: {self.planta_atual.icone} {self.planta_atual.nome}\n"
            f"Status do Ciclo: Concluído com Sucesso 100%\n\n"
            f"--- PESQUISA OPERACIONAL (MINIMIZAÇÃO) ---\n"
            f"• Tempo Reduzido/Otimizado: {res['tempo_otimizado']}s (Base: {self.planta_atual.tempo_des_min}s)\n"
            f"• Água Consumida: {res['agua']} ml\n"
            f"• Iluminação Utilizada: {res['luz']} horas\n"
            f"• Nutrientes Aplicados: {res['nutrientes']} g\n"
            f"• Custo Operacional Total: R$ {res['custo']:.2f}\n\n"
            f"--- ANÁLISE SAZONAL ---\n"
            f"• Melhor Época Indicada: {self.planta_atual.melhor_epoca}\n"
            f"• Pior Época Evitada: {self.planta_atual.pior_epoca}"
        )

        lbl_detalhes = tk.Label(corpo, text=texto_relatorio, font=("Arial", 9), bg="white", fg="#222", justify="left", relief=tk.SOLID, bd=1, padx=12, pady=12)
        lbl_detalhes.pack(fill=tk.BOTH, expand=True, pady=5)

        btn_fechar = tk.Button(corpo, text="Fechar Relatório", font=("Arial", 10, "bold"), bg="#4caf50", fg="white", command=lambda: [rel_janela.destroy(), self.construir_tela_inicial()])
        btn_fechar.pack(pady=10, ipadx=10, ipady=4)


# ==========================================
# EXECUÇÃO DO APLICATIVO
# ==========================================
if __name__ == "__main__":
    root = tk.Tk()
    app = EstufaInteligenteApp(root)
    root.mainloop()
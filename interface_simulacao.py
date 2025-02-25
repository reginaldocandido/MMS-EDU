import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import sys
import subprocess

# Variáveis globais
table_data = []
student_id = 1

# Salvar dados nos CSVs
def save_to_csv(data, relevancia):
    alunos_df = pd.DataFrame(data, columns=["ID", "Nome", "EE", "SB", "SO", "P1", "P2", "P3"])
    alunos_df[["ID", "Nome"]].to_csv("entradas/Alunos.csv", index=False)

    ee_df = pd.DataFrame(data, columns=["ID", "Nome", "EE", "SB", "SO", "P1", "P2", "P3"])
    ee_df[["ID", "EE", "P1"]].to_csv("entradas/EE.csv", index=False)

    sb_df = pd.DataFrame(data, columns=["ID", "Nome", "EE", "SB", "SO", "P1", "P2", "P3"])
    sb_df[["ID", "SB", "P2"]].to_csv("entradas/SB.csv", index=False)

    so_df = pd.DataFrame(data, columns=["ID", "Nome", "EE", "SB", "SO", "P1", "P2", "P3"])
    so_df[["ID", "SO", "P3"]].to_csv("entradas/SO.csv", index=False)

    relevancia_df = pd.DataFrame([relevancia], columns=["delta1", "delta2", "delta3"])
    relevancia_df.to_csv("entradas/Relevancia.csv", index=False)

# Executar a calculadora
def execute_calculator():
    try:
        subprocess.run([sys.executable, "calculadora_smi.py"], check=True)
        messagebox.showinfo("Sucesso", "Cálculo do SMI realizado com sucesso! Verifique a saída.")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao executar a calculadora: {e}")

# Adicionar dados na tabela
def add_to_table(nome, ee, sb, so, p1, p2, p3):
    global student_id, table_data

    if nome and ee and sb and so and p1 and p2 and p3:
        try:
            table_data.append([student_id, nome, int(ee), int(sb), int(so), float(p1), float(p2), float(p3)])
            table.insert("", "end", values=(student_id, nome, ee, sb, so, p1, p2, p3))
            student_id += 1
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")
    else:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios.")

# Limpar a tabela
def clear_table():
    global table_data, student_id
    table_data.clear()
    student_id = 1
    table.delete(*table.get_children())

# Interface Principal
def main():
    global table

    # Criação da janela principal
    root = tk.Tk()
    root.title("Dados para Simulação - Calculadora SMI")
    root.geometry("830x490")

    # Definir o ícone da aplicação
    root.iconbitmap("assets/icone_mms-edu.ico")

    # Tema ttk
    style = ttk.Style(root)
    style.theme_use("clam")

    # Frames
    data_frame = ttk.LabelFrame(root, text="Dados do Aluno")
    data_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    relevance_frame = ttk.LabelFrame(root, text="Fatores de Relevância")
    relevance_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    action_frame = ttk.LabelFrame(root, text="Ações")
    action_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    # Entradas para Dados
    ttk.Label(data_frame, text="Nome").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    nome_entry = ttk.Entry(data_frame)
    nome_entry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(data_frame, text="EE").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    ee_entry = ttk.Entry(data_frame)
    ee_entry.grid(row=1, column=1, padx=5, pady=5)

    ttk.Label(data_frame, text="SB").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    sb_entry = ttk.Entry(data_frame)
    sb_entry.grid(row=2, column=1, padx=5, pady=5)

    ttk.Label(data_frame, text="SO").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    so_entry = ttk.Entry(data_frame)
    so_entry.grid(row=3, column=1, padx=5, pady=5)

    ttk.Label(data_frame, text="P1").grid(row=4, column=0, padx=5, pady=5, sticky="e")
    p1_entry = ttk.Entry(data_frame)
    p1_entry.grid(row=4, column=1, padx=5, pady=5)

    ttk.Label(data_frame, text="P2").grid(row=5, column=0, padx=5, pady=5, sticky="e")
    p2_entry = ttk.Entry(data_frame)
    p2_entry.grid(row=5, column=1, padx=5, pady=5)

    ttk.Label(data_frame, text="P3").grid(row=6, column=0, padx=5, pady=5, sticky="e")
    p3_entry = ttk.Entry(data_frame)
    p3_entry.grid(row=6, column=1, padx=5, pady=5)

    # Entradas para Relevância
    ttk.Label(relevance_frame, text="δ1").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    delta1_entry = ttk.Entry(relevance_frame)
    delta1_entry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(relevance_frame, text="δ2").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    delta2_entry = ttk.Entry(relevance_frame)
    delta2_entry.grid(row=1, column=1, padx=5, pady=5)

    ttk.Label(relevance_frame, text="δ3").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    delta3_entry = ttk.Entry(relevance_frame)
    delta3_entry.grid(row=2, column=1, padx=5, pady=5)

    # Tabela
    table = ttk.Treeview(root, columns=("ID", "Nome", "EE", "SB", "SO", "P1", "P2", "P3"), show="headings")
    for col in table["columns"]:
        table.heading(col, text=col)
    table.grid(row=0, column=1, rowspan=3, padx=10, pady=10, sticky="ns")
    
    # Configuração dos cabeçalhos
    table.heading("ID", text="ID")
    table.heading("Nome", text="Nome")
    table.heading("EE", text="EE")
    table.heading("SB", text="SB")
    table.heading("SO", text="SO")
    table.heading("P1", text="P1")
    table.heading("P2", text="P2")
    table.heading("P3", text="P3")

    # Configuração das larguras das colunas
    table.column("ID", width=50, anchor="center")   # Máximo 5 caracteres
    table.column("Nome", width=120, anchor="w")    # Máximo 12 caracteres
    table.column("EE", width=50, anchor="center")  # Máximo 5 caracteres
    table.column("SB", width=50, anchor="center")  # Máximo 5 caracteres
    table.column("SO", width=50, anchor="center")  # Máximo 5 caracteres
    table.column("P1", width=50, anchor="center")  # Máximo 5 caracteres
    table.column("P2", width=50, anchor="center")  # Máximo 5 caracteres
    table.column("P3", width=50, anchor="center")  # Máximo 5 caracteres

    # Adicionando a tabela ao layout
    table.grid(row=0, column=1, rowspan=3, padx=10, pady=10, sticky="ns")

    # Botões
    ttk.Button(action_frame, text="Adicionar", command=lambda: add_to_table(
        nome_entry.get(), ee_entry.get(), sb_entry.get(), so_entry.get(),
        p1_entry.get(), p2_entry.get(), p3_entry.get())).grid(row=0, column=0, padx=5, pady=5)

    ttk.Button(action_frame, text="Salvar e Executar", command=lambda: [
        save_to_csv(table_data, [float(delta1_entry.get()), float(delta2_entry.get()), float(delta3_entry.get())]),
        execute_calculator()
    ]).grid(row=0, column=1, padx=5, pady=5)

    ttk.Button(action_frame, text="Limpar Tabela", command=clear_table).grid(row=0, column=2, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()

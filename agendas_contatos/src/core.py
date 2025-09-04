import csv
import os
from .utils import validar_email, validar_telefone
from tkinter import messagebox

ARQUIVO = os.path.join(os.path.dirname(__file__), 'contatos.csv')

def salvar_contato(nome, telefone, email, listbox):
    nome = nome.strip()
    telefone = telefone.strip()
    email = email.strip()

    if not nome or not telefone or not email:
        messagebox.showwarning("Campos vazios", "Preencha todos os campos!")
        return

    if not validar_telefone(telefone):
        messagebox.showerror("Telefone inválido", "Digite 10 ou 11 números.")
        return

    if not validar_email(email):
        messagebox.showerror("E-mail inválido", "Digite um e-mail válido.")
        return

    novo = [nome, telefone, email]
    novo_arquivo = not os.path.exists(ARQUIVO)

    with open(ARQUIVO, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if novo_arquivo:
            writer.writerow(['Nome', 'Telefone', 'E-mail'])
        writer.writerow(novo)

    messagebox.showinfo("Sucesso", f"Contato '{nome}' salvo!")
    listar_contatos(listbox)

def listar_contatos(listbox):
    listbox.delete(0, 'end')
    if not os.path.exists(ARQUIVO):
        return

    with open(ARQUIVO, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)
        for linha in reader:
            listbox.insert('end', f"{linha[0]} | {linha[1]} | {linha[2]}")

def remover_contato(nome_contato, listbox):
    with open(ARQUIVO, 'r', encoding='utf-8') as f:
        contatos = list(csv.reader(f))

    novos_contatos = [contatos[0]]
    for contato in contatos[1:]:
        if contato[0] != nome_contato:
            novos_contatos.append(contato)

    with open(ARQUIVO, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(novos_contatos)

    messagebox.showinfo("Removido", f"Contato '{nome_contato}' foi removido.")
    listar_contatos(listbox)

from tkinter import *
from tkinter import messagebox
from .core import salvar_contato, listar_contatos, remover_contato
from .utils import exportar_pdf, fazer_backup

def iniciar_interface():
    fazer_backup()

    def on_salvar():
        salvar_contato(entry_nome.get(), entry_telefone.get(), entry_email.get(), listbox)

    def on_remover():
        selecionado = listbox.curselection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um contato para remover.")
            return
        linha = listbox.get(selecionado[0])
        nome = linha.split('|')[0].strip()
        remover_contato(nome, listbox)

    root = Tk()
    root.title("Agenda de Contatos")
    root.geometry("500x500")
    root.resizable(False, False)

    Label(root, text="Nome:").pack()
    entry_nome = Entry(root, width=50)
    entry_nome.pack(pady=2)

    Label(root, text="Telefone:").pack()
    entry_telefone = Entry(root, width=50)
    entry_telefone.pack(pady=2)

    Label(root, text="E-mail:").pack()
    entry_email = Entry(root, width=50)
    entry_email.pack(pady=2)

    FrameBotoes = Frame(root)
    FrameBotoes.pack(pady=10)

    Button(FrameBotoes, text="Salvar Contato", command=on_salvar, width=18).grid(row=0, column=0, padx=5)
    Button(FrameBotoes, text="Remover Selecionado", command=on_remover, width=18).grid(row=0, column=1, padx=5)
    Button(FrameBotoes, text="Exportar para PDF", command=exportar_pdf, width=38).grid(row=1, column=0, columnspan=2, pady=10)

    Label(root, text="Contatos:").pack()
    listbox = Listbox(root, width=70)
    listbox.pack(pady=10)

    listar_contatos(listbox)

    root.mainloop()

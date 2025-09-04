import re 
import os
import shutil
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from tkinter import messagebox
from tkinter import *


ARQUIVO = os.path.join(os.path.dirname(__file__), 'contatos.csv')

def validar_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)

def validar_telefone(telefone):
    return re.match(r'^\d{10,11}$', telefone)

def fazer_backup():
    if not os.path.exists('backups'):
        os.makedirs('backups')
    if os.path.exists(ARQUIVO):
        data = datetime.now().strftime('%Y%m%d_%H%M%S')
        destino = os.path.join('backups', f'contatos_{data}.csv')
        shutil.copy(ARQUIVO, destino)

def exportar_pdf():
    if not os.path.exists(ARQUIVO):
        messagebox.showwarning('Aviso', "Nenhum contato para exportar")
        return
    
    c = canvas.Canvas('Contatos.pdf', pagesize=A4)
    width, height = A4
    y =  height - 50
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, y, 'Agenda de Contatos')
    y -= 30

    with open(ARQUIVO, 'r', encoding='utf8') as f:
        next(f)
        for linha in f:
            partes = linha.strip().split(',')
            if len(partes) < 3:
                continue

            texto = f'Nome: {partes} | Tel: {partes[1]} | E-mail: {partes[2]}' 
            c.setFont("Helvetica", 10)
            c.drawString(50, y, texto)
            y -= 20
            if y < 50:
                c.showPage()
                y = height - 50

    c.save()
    messagebox.showinfo('Sucesso', "Arquivo PDF 'contatos.pdf' criado")

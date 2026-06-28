import os
import sqlite3
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 1. Caminho relativo (o mesmo do app.py)
base_dir = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(base_dir, 'contratos.db')

# 2. Busca a senha das variáveis de ambiente
MINHA_SENHA = os.environ.get('EMAIL_SENHA') 

def verificar_e_enviar_alertas():
    if not MINHA_SENHA:
        print("❌ Erro: Variável de ambiente EMAIL_SENHA não encontrada.")
        return

    dia_atual = int(datetime.now().strftime('%d'))

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT numero_contrato, nome_cliente, email_notificacao, dia_faturamento FROM contratos WHERE dia_alerta = ?', (dia_atual,))
    contratos_de_hoje = cursor.fetchall()
    conn.close()

    if not contratos_de_hoje:
        print(f"[SystemFlow] Dia {dia_atual}: Nenhum lembrete para hoje.")
        return

    MEU_EMAIL = "systemflow.automacao@gmail.com"
    SERVIDOR_SMTP = "smtp.gmail.com"
    PORTA_SMTP = 587

    try:
        servidor = smtplib.SMTP(SERVIDOR_SMTP, PORTA_SMTP)
        servidor.starttls()
        servidor.login(MEU_EMAIL, MINHA_SENHA)

        for contrato in contratos_de_hoje:
            numero_contrato, nome_cliente, email_notificacao, dia_faturamento = contrato

            mensagem = MIMEMultipart()
            mensagem['From'] = f"SystemFlow <{MEU_EMAIL}>"
            mensagem['To'] = email_notificacao
            mensagem['Subject'] = f"🚨 TAREFA: Faturamento Contrato Nº {numero_contrato}"

            corpo_email = f"""
            🚨 LEMBRETE DE FATURAMENTO - SYSTEMFLOW
            Atenção,
            O contrato {numero_contrato} ({nome_cliente}) precisa ser faturado no dia {dia_faturamento}.
            Bom trabalho,
            Robô de Alertas SystemFlow
            """
            mensagem.attach(MIMEText(corpo_email, 'plain', 'utf-8'))
            
            servidor.sendmail(MEU_EMAIL, [email_notificacao, MEU_EMAIL], mensagem.as_string())
            print(f"[SystemFlow] E-mail enviado para {email_notificacao}")

        servidor.quit()

    except Exception as erro:
        print(f"❌ Erro na execução do robô: {erro}")

if __name__ == '__main__':
    verificar_e_enviar_alertas()
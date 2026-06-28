import os
import sqlite3
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Definição dos caminhos para o banco de dados local
base_dir = "/home/maria/Projetos/systemflow" # Corrigi para a pasta que você usa
DB_PATH = os.path.join(base_dir, 'contratos.db')

def verificar_e_enviar_alertas():
    # Obtém o dia atual do mês
    dia_atual = int(datetime.now().strftime('%d'))

    # Conecta ao banco de dados e busca os contratos agendados para o dia de hoje
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT numero_contrato, nome_cliente, email_notificacao, dia_faturamento FROM contratos WHERE dia_alerta = ?', (dia_atual,))
    contratos_de_hoje = cursor.fetchall()
    conn.close()

    # Encerra a execução caso não haja alertas
    if not contratos_de_hoje:
        print(f"[SystemFlow] Dia {dia_atual}: Nenhum lembrete agendado para hoje.")
        return

    # CONFIGURAÇÕES DE E-MAIL (Agora fora do if!)
    MEU_EMAIL = "systemflow.automacao@gmail.com"  
    SERVIDOR_SMTP = "smtp.gmail.com"
    PORTA_SMTP = 587

    try:
        # Inicializa a conexão
        servidor = smtplib.SMTP(SERVIDOR_SMTP, PORTA_SMTP)
        servidor.starttls()
        servidor.login(MEU_EMAIL, MINHA_SENHA)

        # Percorre a lista de contratos
        for contrato in contratos_de_hoje:
            numero_contrato, nome_cliente, email_notificacao, dia_faturamento = contrato

            mensagem = MIMEMultipart()
            mensagem['From'] = f"SystemFlow <{MEU_EMAIL}>"
            mensagem['To'] = email_notificacao
            mensagem['Bcc'] = MEU_EMAIL # Cópia oculta para você
            mensagem['Subject'] = f"🚨 TAREFA: Faturamento Contrato Nº {numero_contrato}"

            corpo_email = f"""
            🚨 LEMBRETE DE FATURAMENTO - SYSTEMFLOW

            Atenção,

            O contrato {numero_contrato} ({nome_cliente}) precisa ser faturado no dia {dia_faturamento}.

            Bom trabalho,
            Robô de Alertas SystemFlow
            """
            mensagem.attach(MIMEText(corpo_email, 'plain', 'utf-8'))
            
            # Envia para o destino e para você
            servidor.sendmail(MEU_EMAIL, [email_notificacao, MEU_EMAIL], mensagem.as_string())
            print(f"[SystemFlow] E-mail enviado com sucesso!")

        servidor.quit()

    except Exception as erro:
        print(f"❌ Erro na execução do robô: {erro}")

if __name__ == '__main__':
    verificar_e_enviar_alertas()
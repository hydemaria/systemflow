import os
import sqlite3
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, request, jsonify

import os
from flask import Flask, render_template, request, jsonify

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, 
            template_folder=os.path.join(basedir, 'templates'),
            static_folder=os.path.join(basedir, 'static'))

DB_PATH = os.path.join(basedir, 'contratos.db')

app.secret_key = "chave-secreta-para-sistema-financeiro-systemflow"


def init_db():
    # Cria a tabela de contratos se ela não existir
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contratos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_contrato TEXT NOT NULL,
            nome_cliente TEXT NOT NULL,
            email_notificacao TEXT NOT NULL,
            dia_faturamento INTEGER NOT NULL,
            dia_alerta INTEGER NOT NULL,
            possui_printwayy BOOLEAN NOT NULL,
            data_inicio TEXT NOT NULL,
            meses_duracao INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


@app.route('/')
def home():
    # Carrega a página inicial do painel
    return render_template('index.html')


@app.route('/api/contratos', methods=['GET'])
def listar_contratos():
    # Busca os contratos armazenados no banco de dados
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contratos')
    linhas = cursor.fetchall()
    conn.close()

    contratos = []
    for r in linhas:
        contratos.append({
            'id': r[0],
            'numero_contrato': r[1],
            'nome_cliente': r[2],
            'email_notificacao': r[3],
            'dia_faturamento': r[4],
            'dia_alerta': r[5],
            'possui_printwayy': bool(r[6]),
            'data_inicio': r[7],
            'meses_duracao': r[8]
        })
    return jsonify(contratos)


@app.route('/api/contratos', methods=['POST'])
def adicionar_contrato():
    # Recebe os dados do formulário e salva no banco de dados
    dados = request.json
    hoje = datetime.now().strftime('%Y-%m-%d')

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO contratos (numero_contrato, nome_cliente, email_notificacao, dia_faturamento, dia_alerta, possui_printwayy, data_inicio, meses_duracao)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        dados['numero_contrato'],
        dados['nome_cliente'],
        dados['email_notificacao'],
        dados['dia_faturamento'],
        dados['dia_alerta'],
        dados['possui_printwayy'],
        hoje,
        dados['meses_duracao']
    ))
    conn.commit()
    conn.close()
    return jsonify({'status': 'sucesso'})


@app.route('/api/contratos/<int:id>', methods=['DELETE'])
def deletar_contrato(id):
    # Remove um contrato específico do banco de dados
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM contratos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'sucesso'})


@app.route('/api/contratos/<int:id>/enviar-alerta', methods=['POST'])
def enviar_alerta(id):
    # Envia um e-mail de alerta manual usando o servidor SMTP
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT numero_contrato, nome_cliente, email_notificacao, dia_faturamento FROM contratos WHERE id = ?', (id,))
    contrato = cursor.fetchone()
    conn.close()

    if not contrato:
        return jsonify({'status': 'erro', 'mensagem': 'Contrato não encontrado'}), 404

    numero_contrato, nome_cliente, email_notificacao, dia_faturamento = contrato

    # Configurações do servidor de e-mail (SMTP)
    MEU_EMAIL = "systemflow.automacao@gmail.com"
    MINHA_SENHA = "klaa irop dzlu xlhb "
    SERVIDOR_SMTP = "smtp.gmail.com"
    PORTA_SMTP = 587

# Configurações do servidor de e-mail (SMTP)
    MEU_EMAIL = "systemflow.automacao@gmail.com"
    MINHA_SENHA = "klaairopdzluxlhb"  # Removi os espaços extras que estavam aqui
    SERVIDOR_SMTP = "smtp.gmail.com"
    PORTA_SMTP = 587

    try:
        mensagem = MIMEMultipart()
        mensagem['From'] = MEU_EMAIL
        mensagem['To'] = email_notificacao
        mensagem['Subject'] = f"🚨 TAREFA: Faturamento Contrato Nº {numero_contrato} ({nome_cliente})"

        corpo_email = f"Este é um alerta automático para o contrato {numero_contrato}."
        mensagem.attach(MIMEText(corpo_email, 'plain', 'utf-8'))

        servidor = smtplib.SMTP(SERVIDOR_SMTP, PORTA_SMTP)
        servidor.starttls()
        servidor.login(MEU_EMAIL, MINHA_SENHA)
        servidor.sendmail(MEU_EMAIL, email_notificacao, mensagem.as_string())
        servidor.quit()

        return jsonify({'status': 'sucesso', 'mensagem': 'E-mail enviado!'})

except Exception as erro:
    print(f"❌ Ocorreu um erro: {erro}") 
    return jsonify({'status': 'erro', 'mensagem': str(erro)}), 500 

    
if __name__ == '__main__':
    init_db()
    print("Banco de dados local contratos.db pronto!")
    app.run(debug=True, port=5000)
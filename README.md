# 🚀 SystemFlow

Sistema web de automação de alertas de faturamento.

O SystemFlow permite cadastrar contratos, monitorar datas de cobrança e enviar lembretes automáticos por e-mail, simulando um sistema interno usado em empresas.

O projeto combina painel web + robô de automação em Python.

## Funcionalidades

- Cadastro de contratos
- Definição de datas de faturamento e alerta
- Lista de contratos em painel web
- Envio manual de e-mails
- Robô automático de envio de alertas
- Remoção de contratos
- Banco de dados local SQLite

---

## Como funciona

O sistema tem duas partes:

### Painel Web (Flask)
- Interface para cadastrar e visualizar contratos
- Permite envio manual de e-mails de teste

### Robô de automação
- Verifica diariamente os contratos no banco
- Envia e-mails quando o dia de alerta é atingido
- Funciona de forma automática via Python

---

## Tecnologias

Backend:
- Python
- Flask
- SQLite
- SMTP

Frontend:
- HTML
- TailwindCSS
- JavaScript
- SweetAlert2

---

## Estrutura do projeto

systemflow/
├── app.py
├── bot_alertas.py
├── contratos.db
├── templates/
│   └── index.html
└── static/

---

## Como executar

Instalar dependências:
pip install flask

Rodar o sistema web:
python app.py

Acessar:
http://localhost:5000

Rodar o robô:
python bot_alertas.py

---

## Automação (Linux - cron)

0 8 * * * python3 /home/maria/Projetos/systemflow/bot_alertas.py

---

## Configuração de e-mail

No bot_alertas.py:

MEU_EMAIL = "seu_email@gmail.com"
MINHA_SENHA = "senha_de_app"
SERVIDOR_SMTP = "smtp.gmail.com"
PORTA_SMTP = 587

---

## Objetivo

Projeto criado para praticar:

- Backend com Flask
- Automação com Python
- Banco de dados SQLite
- Integração com e-mail
- Sistema web completo

---

## Desenvolvido por

Maria Luiza  
GitHub: https://github.com/hydemaria

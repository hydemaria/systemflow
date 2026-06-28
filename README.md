# 🚀 SystemFlow

Sistema web de automação de alertas de faturamento.

O SystemFlow permite cadastrar contratos, monitorar datas de cobrança e enviar lembretes automáticos por e-mail, simulando um sistema interno usado em empresas.

O projeto combina painel web + robô de automação em Python.

---

## 💡 Funcionalidades

- Cadastro de contratos
- Definição de datas de faturamento e alerta
- Lista de contratos em painel web
- Envio manual de e-mails de teste
- Remoção de contratos
- Banco de dados local (SQLite)
- Robô automático de envio de alertas por e-mail

---

## ⚙️ Como funciona

### 🌐 Painel Web (Flask)

- Interface para cadastrar e visualizar contratos
- Permite envio manual de e-mails

### 🤖 Robô de automação

- Verifica diariamente o banco de dados
- Envia e-mails quando o dia de alerta é atingido
- Pode ser executado manualmente ou via cron no Linux

---

## 🛠️ Tecnologias

### Backend

- Python  
- Flask  
- SQLite  
- SMTP  

### Frontend

- HTML  
- TailwindCSS  
- JavaScript  
- SweetAlert2  

---

## 📁 Estrutura do projeto

systemflow/

├── app.py  
├── bot_alertas.py  
├── contratos.db  
├── templates/  
│   └── index.html  
└── static/  

---

## ⚙️ Como executar o projeto

### 1. Clonar o repositório

git clone https://github.com/hydemaria/systemflow.git  

cd systemflow  

---

### 2. Instalar dependências

pip install flask  

---

### 3. Rodar o sistema web

python app.py  

---

### 4. Acessar no navegador

http://localhost:5000  

---

## 🤖 Automação (robô de alertas)

Executar manualmente:

python bot_alertas.py  

---

Agendar no Linux (cron):

0 8 * * * python3 /home/maria/Projetos/systemflow/bot_alertas.py  

---

## 🔐 Configuração de e-mail

No arquivo bot_alertas.py:

MEU_EMAIL = "seu_email@gmail.com"  
MINHA_SENHA = "senha_de_app"  
SERVIDOR_SMTP = "smtp.gmail.com"  
PORTA_SMTP = 587  

---

## 🎯 Objetivo do projeto

- Backend com Flask  
- Automação com Python  
- Banco de dados SQLite  
- Integração com e-mail  
- Sistema web completo  

---

## 👩‍💻 Desenvolvido por

Maria Luiza  
GitHub: https://github.com/hydemaria

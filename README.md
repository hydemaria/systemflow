# SystemFlow

Sistema de alertas de faturamento desenvolvido em Flask.

O SystemFlow permite cadastrar contratos e enviar alertas automáticos por e-mail antes da data de faturamento, ajudando no controle operacional.

---

## 🚀 Funcionalidades

- Cadastro de contratos
- Listagem de contratos
- Remoção de contratos
- Envio de alertas por e-mail
- API em Flask
- Banco de dados SQLite

---

## 🧠 Tecnologias utilizadas

- Python
- Flask
- SQLite
- HTML
- SMTP

---

## 📁 Estrutura do projeto

systemflow/
├── app.py
├── requirements.txt
├── templates/
├── static/
├── .gitignore
└── README.md

---

## 🔐 Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

EMAIL_SENHA=sua_senha_de_app

⚠️ Esse arquivo NÃO deve ser enviado ao GitHub.

---

## ⚙️ Como executar o projeto

```bash
git clone git@github.com:hydemaria/systemflow.git
cd systemflow

python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
python app.py
```

---

## 👩‍💻 Autora

Maria Luiza (Hyde)

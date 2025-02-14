# 💬 Chat com IA

Este projeto é um **chat interativo com IA**, desenvolvido usando **Python (Flask)** no backend e **HTML, CSS e JavaScript** no frontend. O sistema permite que o usuário envie mensagens e receba respostas automáticas.

---

## 🚀 Tecnologias Utilizadas

- **Python 3**
- **Flask**
- **HTML5, CSS3 e JavaScript**
- **Fetch API (AJAX)**
- **JSON**

---

## 📂 Estrutura do Projeto

📁 chat-ia │-- 📄 app.py # Backend (Flask) - Processa as mensagens │-- 📄 templates/ │ │-- 📄 index.html # Frontend - Interface do chat │-- 📄 static/ │ │-- 📄 style.css # Arquivo de estilos │ │-- 📄 script.js # Lógica do frontend │-- 📄 README.md # Este arquivo explicativo

## 📌 Como Executar o Projeto

### 🔹 1️⃣ Instale o Python (se ainda não tiver)
Se ainda não tem o **Python 3** instalado, faça o download em:  
🔗 [https://www.python.org/downloads/](https://www.python.org/downloads/)

### 🔹 2️⃣ Instale as dependências
Abra o terminal na pasta do projeto e execute:

```bash
pip install flask

Inicie o servidor-

python app.py

veja a saida  * Running on http://127.0.0.1:5000/ copie e cole na URL

🛠️ Como o Código Funciona
🔹 Backend (app.py - Flask)
O Flask é usado para criar um servidor web.
A página principal é servida através da rota /.
A rota /chat recebe mensagens do usuário e retorna uma resposta.


 Frontend (index.html, style.css, script.js)
O HTML contém um formulário onde o usuário pode digitar mensagens.
O JavaScript captura a mensagem e envia para o backend usando fetch().
As respostas da IA são exibidas dinamicamente na tela.

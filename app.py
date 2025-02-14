from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# Inicializa o app Flask
app = Flask(__name__)

# Substitua pela sua chave de API correta
api_key = "AIzaSyDGIqK2m4_Q4Euxpxb2y-1LQFhpsWW6TtQ"
genai.configure(api_key=api_key)

# Configuração do modelo
generation_config = {
    "candidate_count": 1,
    "temperature": 0.5,
}

safety_settings = {
    "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
}

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Rota para o front-end
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form.get("user_input")

   
    chat = model.start_chat(history=[])
    response = chat.send_message(user_input)
    
    
    return jsonify({"message": response.text})

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template_string, request
from transformers import pipeline

# Initialisation de l’application Flask
app = Flask(__name__)

# Chargement d’un modèle IA léger et gratuit (parfait pour Render)
chatbot = pipeline("text2text-generation", model="google/flan-t5-base")

# Contenu HTML de la page
page_html = """
<!doctype html>
<html>
<head>
  <title>JuriCongo AI</title>
</head>
<body style="font-family:Arial; margin:50px;">
  <h2>⚖️ Bienvenue sur JuriCongo AI</h2>
  <p>Assistant juridique congolais — propulsé par l’IA.</p>
  <form method="post">
      <label>Votre question :</label><br>
      <textarea name="question" rows="5" cols="80"></textarea><br><br>
      <input type="submit" value="Envoyer">
  </form>

  {% if reponse %}
  <hr>
  <h3>Réponse :</h3>
  <p>{{ reponse }}</p>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    reponse = None
    if request.method == "POST":
        question = request.form["question"]
        # Génération de la réponse avec le modèle léger
        result = chatbot(question, max_length=200)
        reponse = result[0]["generated_text"]
    return render_template_string(page_html, reponse=reponse)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

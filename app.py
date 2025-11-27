from flask import Flask, render_template_string, request
from transformers import pipeline

app = Flask(__name__)
chatbot = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1")

page_html = """
<!doctype html>
<html>
<head><title>JuriCongo AI</title></head>
<body style="font-family:Arial; margin:50px;">
<h2>⚖️ Bienvenue sur JuriCongo AI</h2>
<p>Assistant juridique congolais — basé sur le droit local.</p>
<form method="post">
  <label>Question :</label><br>
  <textarea name="question" rows="5" cols="80"></textarea><br><br>
  <input type="submit" value="Envoyer">
</form>
{% if reponse %}
<hr><h3>Réponse :</h3><p>{{ reponse }}</p>{% endif %}
</body></html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    reponse = None
    if request.method == "POST":
        q = request.form["question"]
        result = chatbot(q, max_length=200, do_sample=True)
        reponse = result[0]['generated_text']
    return render_template_string(page_html, reponse=reponse)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

import os
from flask import Flask, request, render_template_string

app = Flask(__name__)

page_html = """
<!doctype html>
<html>
<head><title>JuriCongo AI</title></head>
<body style="font-family:Arial;margin:40px;">
<h2>⚖️ Bienvenue sur JuriCongo AI</h2>
<p>Assistant juridique congolais (version de test)</p>
<form method="post">
<textarea name="question" rows="5" cols="70"></textarea><br><br>
<input type="submit" value="Envoyer">
</form>
{% if reponse %}
<hr><b>Réponse :</b><br>{{ reponse }}
{% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    reponse = None
    if request.method == "POST":
        q = request.form["question"].lower()
        if "licenciement" in q:
            reponse = "Selon le Code du travail congolais, un licenciement sans cause juste ouvre droit à indemnité."
        elif "congé" in q:
            reponse = "Tout travailleur a droit à un congé annuel payé."
        elif "contrat" in q:
            reponse = "Le contrat de travail peut être à durée déterminée ou indéterminée."
        else:
            reponse = "Je n’ai pas trouvé d’article correspondant. Essayez un autre mot-clé (licenciement, congé, contrat...)."
    return render_template_string(page_html, reponse=reponse)

# Render fournit automatiquement un port dans la variable d’environnement PORT
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

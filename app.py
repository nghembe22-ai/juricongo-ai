from flask import Flask, render_template_string, request

app = Flask(__name__)

# Mini base juridique locale (sans IA)
base_juridique = {
    "licenciement": "Selon le Code du travail congolais, tout licenciement sans cause juste et sérieuse ouvre droit à une indemnité compensatoire équivalente à trois mois de salaire.",
    "congé": "Le salarié a droit à un congé annuel payé dont la durée est fixée par le Code du travail.",
    "contrat": "Un contrat de travail peut être à durée déterminée ou indéterminée. Il doit être écrit pour éviter tout litige.",
}

page_html = """
<!doctype html>
<html>
<head><title>JuriCongo AI</title></head>
<body style="font-family:Arial; margin:50px;">
<h2>⚖️ Bienvenue sur JuriCongo AI</h2>
<p>Assistant juridique congolais simplifié.</p>
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
        question = request.form["question"].lower()
        # Recherche simple dans la base juridique
        for mot_cle, texte in base_juridique.items():
            if mot_cle in question:
                reponse = texte
                break
        if not reponse:
            reponse = "Je n’ai pas trouvé d’article correspondant. Essayez un autre sujet juridique (licenciement, congé, contrat, etc.)."
    return render_template_string(page_html, reponse=reponse)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

"""
Minimal web interface for AI Dev Platform.
"""

from flask import Flask, request, render_template
from ai_checks.syntax import check_syntax
from ai_checks.style import check_style

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        file = request.files.get("codefile")
        if file:
            filepath = f"temp_upload.py"
            file.save(filepath)
            syntax_ok, syntax_msg = check_syntax(filepath)
            style_ok, style_msg = check_style(filepath)
            result = {
                "syntax": syntax_msg,
                "style": style_msg
            }
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

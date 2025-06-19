import os
from flask import Flask, request, render_template_string, send_from_directory
from transformers import LlamaTokenizer, LlamaForCausalLM
import torch

MODEL_PATH = os.environ.get("LLAMA_MODEL_PATH", "./llama")

app = Flask(__name__)

# Load model and tokenizer once at startup
try:
    tokenizer = LlamaTokenizer.from_pretrained(MODEL_PATH)
    model = LlamaForCausalLM.from_pretrained(MODEL_PATH)
except Exception as e:
    tokenizer = None
    model = None
    print(f"Could not load Llama model: {e}")

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

CHAT_TEMPLATE = """
<!doctype html>
<title>Llama Chatbot</title>
<h2>Llama Chatbot</h2>
<form method=post>
  <textarea name=message rows=4 cols=50></textarea><br>
  <input type=submit value=Send>
</form>
{% if response %}
<p><strong>You:</strong> {{message}}</p>
<p><strong>Llama:</strong> {{response}}</p>
{% endif %}
<p><a href="/upload">Upload Document</a></p>
<p><a href="/dashboard">Student Dashboard</a></p>
"""

UPLOAD_TEMPLATE = """
<!doctype html>
<title>Upload Document</title>
<h2>Upload Document</h2>
<form method=post enctype=multipart/form-data>
  <input type=file name=file>
  <input type=submit value=Upload>
</form>
<p><a href="/">Back to Chat</a></p>
"""

@app.route('/', methods=['GET', 'POST'])
def chat():
    response = None
    message = None
    if request.method == 'POST':
        message = request.form.get('message', '')
        if tokenizer is None or model is None:
            response = "Model not loaded. Check LLAMA_MODEL_PATH."
        else:
            input_ids = tokenizer.encode(message + tokenizer.eos_token, return_tensors='pt')
            output_ids = model.generate(input_ids, max_new_tokens=100)
            response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return render_template_string(CHAT_TEMPLATE, response=response, message=message)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            file.save(os.path.join(UPLOAD_DIR, file.filename))
            return f"Uploaded {file.filename}<br><a href='/upload'>Upload another</a>"
    return render_template_string(UPLOAD_TEMPLATE)

@app.route('/dashboard')
def dashboard_page():
    return send_from_directory('.', 'dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)

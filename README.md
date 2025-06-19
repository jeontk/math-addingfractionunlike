# 🧮 Fraction Addition Instruction Software

This project is an interactive educational tool that teaches students how to **add fractions with unlike denominators**, step by step. It is designed to support conceptual understanding using visual models and clear instructions.

## 🌟 Features

- Enter two fractions with different denominators
- Step-by-step breakdown of:
  - Finding the Least Common Denominator (LCD)
  - Converting to equivalent fractions
  - Adding numerators
  - Simplifying the final result
- Fully interactive in the browser (HTML + JavaScript)
- Beginner-friendly design for elementary and middle school students

## 💻 How to Use

1. Open `index.html` in any modern web browser.
2. Enter two fractions.
3. Click **"Add Fractions"**.
4. Follow the visual steps shown below the button.

## 🚀 Live Demo

You can try the app here (after setting up GitHub Pages):  
👉 [https://jeontk.github.io/math-addingfractionunlike](https://jeontk.github.io/math-addingfractionunlike)

## 📁 Files

- `index.html` — Main application file
- `README.md` — Project overview and usage instructions

## 🧑‍🏫 Use Case

This tool can be used in classrooms, tutoring sessions, or at home to reinforce fraction concepts. It’s particularly helpful for visual learners and students who need step-by-step breakdowns.

---

### 📬 Contributions

Feel free to fork the repo and suggest improvements or new features like:
- Voice guidance
- Visual fraction bars
- Practice quizzes

## 🤖 Llama Chatbot Interface

The repository includes `chatbot_app.py`, a small Flask application that provides
a graphical interface for a locally installed Llama model. To use it:

1. Install dependencies: `pip install flask transformers torch`.
2. Download your Llama weights and set the environment variable
   `LLAMA_MODEL_PATH` to that directory.
3. Run `python chatbot_app.py` and open `http://localhost:5000` in a browser.
4. From the chat page you can upload text files that may be useful for answering
   questions.

## 📊 Student Dashboard

`dashboard.html` offers example learning activities to help students memorize
terms, build concepts, and practice procedures. Access it directly or via the
link at the bottom of `index.html`.

---

## License

MIT License — free to use, modify, and share.

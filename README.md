<!-- Styled README -->

<h1 align="center">🤖 Customer Support Chatbot API</h1>

<p align="center">
  A lightweight AI-powered chatbot built with <b>FastAPI</b> and <b>TF-IDF NLP</b><br>
  Designed for customer support automation with context awareness.
</p>

---

<h2>🚀 Features</h2>

<ul>
  <li>Intent detection using <b>TF-IDF + Cosine Similarity</b></li>
  <li>Context-aware follow-up handling</li>
  <li>Conversation memory (last 3 turns)</li>
  <li>FastAPI-based REST API</li>
  <li>CLI chatbot interface</li>
  <li>Easy-to-edit knowledge base</li>
</ul>

---

<h2>🧠 Tech Stack</h2>

<p>
  Python • FastAPI • Scikit-learn • NumPy • Uvicorn
</p>

---

<h2>📁 Project Structure</h2>

<pre>
.
├── app.py
├── chatbot.py
├── knowledge_base.py
├── test_chat.py
</pre>

---

<h2>⚙️ Installation</h2>

<pre>
git clone https://github.com/your-username/customer-support-chatbot.git
cd customer-support-chatbot

python -m venv .venv
source .venv/bin/activate

pip install fastapi uvicorn scikit-learn numpy pydantic requests
</pre>

---

<h2>▶️ Run the Server</h2>

<pre>
uvicorn app:app --reload --port 8000
</pre>


---

<h2>🧪 API Endpoints</h2>

<h3>POST /chat</h3>

<pre>{
  "message": "where is my order"
}</pre>

<p><b>Response:</b></p>

<pre>{
  "response": "To track your order...",
  "intent": "order_status",
  "confidence": 87.3
}</pre>

---

<h3>Other Endpoints</h3>

<ul>
  <li><b>POST /reset</b> → Clear conversation memory</li>
  <li><b>GET /health</b> → Check server status</li>
  <li><b>GET /intents</b> → List all intents</li>
</ul>

---

<h2>💻 CLI Chat</h2>

<pre>
python test_chat.py
</pre>

<pre>
You: hello
Bot: Hey there! How can I help you today?
(intent: greeting | confidence: 98.2%)
</pre>

---

<h2>⚡ How It Works</h2>

<ol>
  <li>Input is cleaned and normalized</li>
  <li>TF-IDF converts text into vectors</li>
  <li>Cosine similarity finds closest intent</li>
  <li>Context manager handles follow-ups</li>
  <li>Response is returned from knowledge base</li>
</ol>

---

<h2>🛠️ Customization</h2>

<p>Edit <code>knowledge_base.py</code> to add new intents:</p>

<pre>
"new_intent": {
  "patterns": ["example query"],
  "responses": ["example response"]
}
</pre>

---

<h2>📌 Future Improvements</h2>

<ul>
  <li>LLM / Transformer-based understanding</li>
  <li>Frontend UI (React / Web)</li>
  <li>Multi-user session handling</li>
  <li>Deployment (Render / Docker)</li>
</ul>

---

<p align="center">
  ⚡ Simple • Fast • Extendable
</p>

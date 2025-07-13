
# 🛢️ AskMySQL – Natural‑Language MySQL Assistant


AskMySQL lets anyone query a MySQL database by simply **chatting in plain English**.  
Built with **LangChain**, **Groq Llama‑3**, and **Streamlit**, it converts natural‑language questions into safe SQL, executes them, and streams back concise answers.

---

## ✨ Features

| Capability | Details |
|------------|---------|
| **Zero‑SQL Chat** | Ask “Top 5 customers by revenue?” – the agent infers tables, joins, and filters automatically. |
| **Streamlit UI** | Familiar ChatGPT‑style interface with chat history and bubble alignment (user → right, bot → left). |
| **Schema Auto‑Introspection** | LangChain toolkit inspects table/column names so you don’t hard‑code anything. |
| **Groq‑Hosted Llama‑3** | Lightning‑fast 8‑B model for low‑latency answers (or swap in any OpenAI / local LLM). |
| **Secure Connection** | Credentials kept client‑side; works with read‑only users for production safety. |
| **One‑click Deploy** | Deploy to Streamlit Cloud, Docker, or Fly.io in minutes. |

---

## 🗂️ Project Structure


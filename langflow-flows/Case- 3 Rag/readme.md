# Langflow Basic LLM Flow - Starter Example

This project demonstrates a simple **Langflow** setup using a local **LLM (Large Language Model)** running through **Ollama**.

The example flow shows how to send user input to the model, process it, and display the result.  
It includes multiple usage variations and explains how to import and run the flow.

---

## 🚀 Flow Variations

This example contains three different flow configurations:

### 1️⃣ **Basic Flow (Stateless)**

**Text Input → Ollama → Text Output**

- Basic flow using direct **text input**.
- Sends user input to Ollama and displays the model’s response.
- Suitable for simple Playground testing.

### 2️⃣ **Chat Flow with Redis Memory**

**Chat Input → Redis Chat Memory → Message History → Prompt Template → Ollama → Chat Output → Message Store**

- Designed for **chat-based** interaction.
- Uses Redis to store and retrieve conversation history.
- Supports multi-turn, context-aware conversations.

### 3️⃣ **RAG (Retrieval Augmented Generation) Flow**

**File → Split Text → Ollama Embeddings → Local DB (Ingest)**  
**Chat Input → Ollama Embeddings → Local DB (Retrieve) → Parser → Prompt Template → Ollama → Chat Output**

- Implements a **RAG pipeline**.
- LLM can answer questions grounded in document content.
- Uses a local vector store for retrieval.

---

## 🛠️ System Prompt (Prompt Template)

- The flow uses a **Prompt Template** to guide the model’s tone and behavior.
- Example template:
  ```
  You are a helpful assistant that answers questions.
  Use markdown to format your answer, properly embedding images and urls.
  ```
- In RAG Flow, the prompt also includes **retrieved document context**.

---

## ℹ️ Notes

- **Chat memory is enabled** using Redis in chat flow.
- **Document context** is used in RAG flow.
- You need to have a **Redis** instance running for chat memory:
  - Hostname: `redis`
  - Port: `6379`
  - Database: `1`
- Example models:
  - `gemma3:latest`
  - `smollm2:1.7b`
  - `llama3.2:8b`
  - `qwen3:latest`
  - `snowflake-arctic-embed:2:latest` (for embeddings)

---

## 🖥️ Tested With

- **Langflow version:** `v1.4.3`
- **Ollama version:** `v0.9.2` or newer
- **Tested LLM models:**
  - `gemma3:latest`
  - `smollm2:1.7b`
  - `llama3.2:8b`
  - `qwen3:latest`
  - `snowflake-arctic-embed:2:latest`

---

## 📥 How to Import This Flow into Langflow

You can easily import this flow into your local Langflow instance:

1. Download or export the `.json` file:  
   Example: `case-1-flow.json`, `case-2-flow.json`, `case-3-rag-flow.json`

2. Open your **Langflow** UI in the browser.

3. Click the **Import** button.

4. Select the `.flow.json` file.

5. The flow will load and is ready to use!

---

## 📚 Components Used

- **Basic Flow**
  - Text Input
  - Ollama Node
  - Text Output

- **Chat Flow with Redis**
  - Chat Input / Chat Output
  - Redis Chat Memory
  - Message History
  - Prompt Template
  - Ollama Node
  - Message Store

- **RAG Flow**
  - File Upload
  - Split Text
  - Ollama Embeddings (Ingest & Query)
  - Local DB (Vector Store)
  - Chat Input / Chat Output
  - Parser
  - Prompt Template
  - Ollama Node

---

Enjoy building **context-aware chatbots** and **local RAG-powered LLM apps** with Langflow + Ollama + Redis! 🚀
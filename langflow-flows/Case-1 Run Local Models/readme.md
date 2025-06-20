# Langflow Basic LLM Flow - Starter Example

This project demonstrates a simple **Langflow** setup using a local **LLM (Large Language Model)** running through **Ollama**.

The example flow shows how to send user input to the model, process it, and display the result.
It includes multiple usage variations and explains how to import and run the flow.

---

## 🚀 Flow Variations

This example contains three different flow configurations:

### 1️⃣ **Text Input → Ollama → Text Output**

- Basic flow using direct **text input**.
- Sends user input to Ollama and displays the model’s response.
- Suitable for simple Playground testing.

### 2️⃣ **Text Input → Ollama (with System Prompt) → Text Output**

- Adds a **System Prompt** to guide the model’s tone and behavior.
- Helps ensure more consistent and controlled responses.

### 3️⃣ **Chat Input → Ollama → Chat Output**

- Designed for **chat-based** interaction.
- Uses **Chat Input** and **Chat Output** instead of Text nodes.
- Suitable for multi-turn conversations (⚠️ **no memory** in this example).

---

## 🛠️ System Prompt

- The **System Prompt** defines how the LLM should behave.
- It sets the tone, style, and role of the assistant.
- Useful for creating different personas or response styles.

---

## ℹ️ Notes

- **Chat memory** is **not used** in this flow — each message is processed independently.
- You can easily add a **memory node** if needed (Langchain or other memory components).
- The **model name** and **base URL** can be customized in the Ollama node:
  - Example Base URL: `http://host.docker.internal:11434`
  - Example Models:
    - `smollm2:1.7b`
    - `llama3.2:8b`
    - `qwen3:latest`
    - `gemma3:latest`
- Works great for creating simple assistants, chatbots, or testing local models.

---

## 🖥️ Tested With

- **Langflow version:** `v1.4.3`
- **Ollama version:** `v0.9.2` or newer
- **Tested LLM models:**
  - `smollm2:1.7b`
  - `llama3.2:8b`
  - `qwen3:latest`
  - `gemma3:latest`

---

## 📥 How to Import This Flow into Langflow

You can easily import this flow into your local Langflow instance:

1. Download or export the `.json` file:
   Example: `Case - 1 _ Work with Local Models.json`

2. Open your **Langflow** UI in the browser.

3. Click the **Import** button (usually top-left, or in the "File" menu).

4. Select the `.flow.json` file.

5. The flow will load into Langflow and you can start running it!

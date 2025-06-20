# Langflow LLM Agent with Notion Integration - Example

This flow demonstrates an **LLM Agent** that can search the web (DuckDuckGo), generate a response, and automatically save the result into a **Notion page**.

---

## 🚀 Flow Structure

**Chat Input → Agent (Tools: DuckDuckGo Search) → Ollama → Notion Add Content → Chat Output**

---

## 🧭 How the Flow Works

1. **Chat Input**
   - User submits a question or query.

2. **Agent**
   - Agent instructions define behavior:
     ```
     You are a helpful assistant that can search the web and save results to Notion.
     ```
   - The agent decides when to use tools and generates a response.

3. **Available Tools**
   - **DuckDuckGo Search**
     - Performs real-time web search.
     - Returns web content to the agent.

4. **Ollama (LLM)**
   - Model: `llama3.2:3b`
   - Generates a well-formatted answer.

5. **Notion Add Content to Page**
   - Converts the generated response into markdown.
   - Automatically appends the result to a given Notion page.
     - `Page/Block ID`: your Notion page ID
     - `Notion Secret`: your Notion API token

6. **Chat Output**
   - Displays the agent’s response to the user (in parallel to saving it to Notion).

---

## 🛠️ Purpose

- Demonstrates how to build an **LLM agent that writes to Notion**.
- Automates:
  - Searching the web.
  - Generating content.
  - Saving content to Notion pages.
- Useful for:
  - Knowledge base building.
  - Personal note-taking bots.
  - Content summarization & storage.

---

## ℹ️ Notes

- **Ollama LLM:** `llama3.2:3b`
- Requires a valid **Notion API token (integration)** and target **Page/Block ID**.
- No chat memory — purely agent + tool + action to Notion.
- Web search via **DuckDuckGo**.

---

## 🖥️ Tested With

- **Langflow version:** `v1.4.3`
- **Ollama version:** `v0.9.2` or newer
- **Tested LLM models:**
  - `llama3.2:3b`

---

## 📥 How to Import This Flow into Langflow

1. Download the `.flow.json` file  
   Example: `case-5-agent-notion-flow.json`

2. Open **Langflow UI**

3. Click **Import**

4. Select the `.flow.json`

5. Run the flow and test saving content to Notion!

---

## 📚 Components Used

- Chat Input / Chat Output
- Agent
- Ollama (LLM)
- DuckDuckGo Search (Tool)
- Add Content to Notion Page (Integration)

---

This flow is a great starting point for building **LLM-based knowledge bots** or **automated Notion assistants** with Langflow + Ollama 🚀

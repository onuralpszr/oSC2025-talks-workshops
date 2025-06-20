# Langflow LLM Agent with Tool Use - Example

This flow demonstrates how to build an **LLM Agent** using **Langflow**, where the agent can use multiple tools (APIs) to enhance its answers.

The agent uses a local LLM (**Ollama**) and three tools:
- **Wikipedia Search**
- **Calculator**
- **DuckDuckGo Web Search**

---

## 🚀 Flow Structure

**Chat Input → Agent (Tools: Wikipedia, Calculator, DuckDuckGo) → Ollama → Chat Output**

---

## 🧭 How the Flow Works

1. **Chat Input**
   - User submits a query.

2. **Agent**
   - Agent instructions define behavior:
     ```
     You are a helpful assistant that can use tools to answer questions.
     ```
   - The agent receives user input and decides when and how to use tools.

3. **Available Tools**
   - **Wikipedia**
     - Language: `tr`
     - Fetches Wikipedia content in Turkish.

   - **Calculator**
     - Performs basic arithmetic calculations.

   - **DuckDuckGo Search**
     - Performs real-time web search using DuckDuckGo.

4. **Ollama LLM**
   - The local LLM (`llama3.2:3b`) generates a final response using tool outputs + agent context.

5. **Chat Output**
   - Displays the agent’s final response.

---

## 🛠️ Purpose

- Demonstrates how to build an **LLM agent with tool usage**.
- Agent can:
  - Retrieve factual knowledge from Wikipedia.
  - Perform calculations.
  - Perform web searches (DuckDuckGo).
- Agent dynamically decides when to use which tool based on user queries.

---

## ℹ️ Notes

- **Tools are connected** to the agent as a Toolset.
- The **LLM** used:
  - `llama3.2:3b`
- Wikipedia language: `tr` (Turkish)
- No external memory — agent relies on tools + LLM context.

---

## 🖥️ Tested With

- **Langflow version:** `v1.4.3`
- **Ollama version:** `v0.9.2` or newer
- **Tested LLM models:**
  - `llama3.2:3b`

---

## 📥 How to Import This Flow into Langflow

1. Download the `.flow.json` file
   Example: `case-4-agent-tools-flow.json`

2. Open **Langflow UI**

3. Click **Import**

4. Select the `.flow.json`

5. Run the flow and start chatting with the agent!

---

## 📚 Components Used

- Chat Input / Chat Output
- Agent
- Ollama (LLM)
- Wikipedia Search (Tool)
- Calculator (Tool)
- DuckDuckGo Search (Tool)

---

This flow is a great starting point for **Tool-Augmented LLM Agents** built with Langflow + Ollama 🚀

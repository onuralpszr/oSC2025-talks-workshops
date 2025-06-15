# Conférence: openSUSE Conferance 2025 - Run your LLM locally and turn them into Agents  🎤

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/onuralpszr/oSC2025-talks-workshops/main.svg)](https://results.pre-commit.ci/latest/github/onuralpszr/oSC2025-talks-workshops/main)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![🔧 MyPy Test Workflow](https://github.com/onuralpszr/oSC2025-talks-workshops/actions/workflows/mypy-test.yml/badge.svg)](https://github.com/onuralpszr/oSC2025-talks-workshops/actions/workflows/mypy-test.yml)

openSUSE Conference 2025 Workshop and Talks



## 🛠️ Workshop: Run your LLM locally and turn them into Agents

**🗓️ Date:** 26.06.2025
**⏰ Time:** 60 Minutes

**📢 Headline:** Large Language Models (LLMs) are powerful tools, but running them locally unlocks new possibilities—enhancing privacy 🤫, reducing costs 💰, and allowing full customization 🎨. In this talk, we’ll explore how to set up and optimize LLMs on your machine, leveraging open-source models and efficient inference techniques. We’ll then take it a step further by turning these models into intelligent agents that can interact with external tools 🛠️, retrieve information 📄, and automate tasks 🤖. Whether you\'re a developer 👩‍💻, researcher 🧑‍🔬, or AI enthusiast 🤩, this session will provide practical insights into running LLMs locally and building AI-driven agents that work for you.

### 📜 Agenda

#### 🚀 Introduction (Ollama) [10 Minutes]
*   👋 Welcome and Introductions
*   🎯 Workshop Objectives and Expectations
*   🤝 Icebreaker or Opening Activity
*   🧠 Introduce to Ollama
*   ⚙️ How to install Ollama
*   💨 Run Ollama quickly
*   📥 Download Ollama model
*   🌐 Introduce Ollama library website for more
*   📄 Introduce Modelfile

#### 🤖 Session 1 (Smolagent - https://github.com/huggingface/smolagents) [20 Minutes]
*   🐜 Introduce the SmolAgent
*   🤗 Introduce the HF Platform short
*   💻 How to Install SmolAgent and quick-start (uv/pip and basic code)
*   🛠️ How to use tool or create custom tool
*   🔗 How to use MCP / how to create custom MCP (if exists)

#### 🌊 Session 2 (Langflow - https://github.com/langflow-ai/langflow)
*   🧪 Basic Agent Demo
*   🛠️ Basic Agent Tooling Demo (*MCP)
*   🔍 RAG Demo
*   🔌 API Demo (Langflow deployment API)
*   🌍 Real world demo

### 📓 Notebooks

| Notebook Name          | Badges                                                                                                                                                                                                                                                                     |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `quick-ollama.ipynb`   | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/onuralpszr/oSC2025-talks-workshops/blob/main/notebooks/quick-ollama.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/onuralpszr/oSC2025-talks-workshops/blob/main/notebooks/quick-ollama.ipynb) |
| `quick-smollagent.ipynb` | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/onuralpszr/oSC2025-talks-workshops/blob/main/notebooks/quick-smollagent.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/onuralpszr/oSC2025-talks-workshops/blob/main/notebooks/quick-smollagent.ipynb) |

### ⚙️ Project Installation

To run the notebooks and scripts in this repository, you need to install the project dependencies. You can use either `uv` or `pip`.

**📦 Using uv:**

1.  Install the base dependencies:
    ```bash
    uv pip install -e .
    ```
2.  To install optional dependencies for specific hardware (e.g., CPU, CUDA versions, ROCm), you can specify them as extras. For example, to install dependencies for CPU:
    ```bash
    uv pip install -e ".[cpu]"
    ```
    Refer to the `pyproject.toml` file for all available optional dependencies (e.g., `cu126`, `rocm61`).

**🐍 Using pip:**

1.  Install the base dependencies:
    ```bash
    pip install -e .
    ```
2.  To install optional dependencies:
    ```bash
    pip install -e ".[cpu]"
    ```
    Similarly, refer to `pyproject.toml` for other optional dependency groups.

**🐳 Ollama Installation:**

1. Method Install via Ollama Installation script: (linux)
    ```bash
    curl -fsSL https://ollama.com/install.sh | sh
    ```
2. Method Install via openSUSE repository command:
    ```bash
    zypper install ollama
    ```

**🧪 NodeJS Installation:**

1. Method Install via NVM Installation script: (linux)
    ```bash
    # Download and install nvm:
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash

    # in lieu of restarting the shell
    \. "$HOME/.nvm/nvm.sh"

    # Download and install Node.js:
    nvm install 24

    # Verify the Node.js version:
    node -v # Should print "v24.2.0".
    nvm current # Should print "v24.2.0".

    # Verify npm version:
    npm -v # Should print "11.3.0".
    ```
2. Method Install via openSUSE repository command:
    ```bash
    zypper install nodejs22
    ```

### 🐍 Python Scripts

Below is a list of Python scripts included in this repository, with a brief description of their purpose:

| Script Name                           | Description                                                                 |
| ------------------------------------- | --------------------------------------------------------------------------- |
| `quick-smollagent.py`                 | Demonstrates a basic implementation and usage of the Smolagent library.     |
| `quick-smollagent-mcp.py`             | Shows how to use Smolagent with the Model Context Protocol (MCP).           |
| `quick-smollagent-mcp-streamable.py`  | Illustrates using Smolagent with MCP and streaming capabilities.            |

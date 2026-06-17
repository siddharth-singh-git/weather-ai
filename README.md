# 🌦️ Weather AI Agent

An intelligent, lightweight command-line weather assistant powered by **Google Gemini**, **LangChain**, and **Open-Meteo**.

Unlike standard weather applications, this project implements an autonomous **AI Agent**. It understands natural language queries, determines when it needs external data, dynamically invokes weather tools, and returns human-friendly, real-time insights—all without needing a dedicated weather API key.

---

## ✨ Features

* **🤖 Autonomous AI Agent:** Powered by Google Gemini and LangChain tool calling.
* **🌍 Real-Time Intelligence:** Fetches live weather data globally (temperature, wind speed, conditions).
* **🔑 Zero Cost Weather API:** Uses Open-Meteo (open-source, free, no API key required).
* **⚡ Blazing Fast Setup:** Managed natively with the `uv` package manager.
* **🧩 Modular Architecture:** Clean separation of prompts, tools, and agent logic.

---

## 🏗️ Architecture Flow

```text
User Query
     │
     ▼
 Google Gemini (Reasoning)
     │
     ▼
 LangChain Agent (Tool Selection)
     │
     ▼
 Weather Tool (Extraction)
     │
     ▼
 Open-Meteo API (Data Fetching)
     │
     ▼
 Final Natural Language Response
```

---

## 📂 Project Structure

```text
WEATHER-AI/
│
├── src/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── prompt.py          # Agent system prompts & persona
│   └── tools.py           # Open-Meteo API tool implementation
│
├── tests/
│   └── test.ipynb         # Jupyter notebook for agent experimentation
│
├── .env                   # Environment variables (Ignored by git)
├── .gitignore
├── LICENSE
├── main.py                # Application entry point
├── pyproject.toml         # Project metadata and dependencies
├── README.md              # Project documentation
├── requirements.txt       # Fallback dependency list
└── uv.lock                # Deterministic lockfile for uv
```

---

## 🛠️ Tech Stack

| Component       | Technology                                     |
| --------------- | ---------------------------------------------- |
| Language        | Python                                         |
| Agent Framework | LangChain (`langchain`, `langchain-community`) |
| LLM Provider    | Google Gemini (`langchain-google-genai`)       |
| Weather Source  | Open-Meteo API                                 |
| Env Management  | `python-dotenv`                                |
| Package Manager | `uv` (Recommended) / `pip`                     |

---

## 🚀 Installation & Setup

This project uses `uv`, an extremely fast Python package and project manager written in Rust. Standard `pip` instructions are also provided.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/weather-ai.git
cd weather-ai
```

### 2. Setup via `uv` (Recommended ⚡)

Using `uv` with the included `pyproject.toml` and `uv.lock` ensures a perfectly reproducible and lightning-fast environment.

```bash
# Install uv (if you haven't already)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Sync the project (This automatically creates a .venv and installs dependencies)
uv sync

# Activate the virtual environment

# On Windows:
.venv\Scripts\activate

# On Linux/macOS:
source .venv/bin/activate
```

### 3. Setup via pip (Alternative)

```bash
# Create a virtual environment
python -m venv .venv

# Activate the environment

# On Windows:
.venv\Scripts\activate

# On Linux/macOS:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 📦 Managing Dependencies

If you want to add or remove packages in the future, here are the commands for both package managers:

### Using uv

```bash
# Add a new package (updates pyproject.toml and uv.lock automatically)
uv add <package_name>

# Remove a package
uv remove <package_name>
```

### Using pip

```bash
# Install a new package
pip install <package_name>

# Update the requirements.txt file
pip freeze > requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory. You only need an API key for Google Gemini. Open-Meteo does not require an API key.

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

---

## ▶️ Usage

Once your environment is activated and keys are set, run the agent:

```bash
# Standard Python execution
python main.py

# OR run directly via uv without manually activating the venv
uv run main.py
```

### Example Interaction

```text
Enter your query: What's the weather in Delhi right now?

Agent:
The current temperature in Delhi is 34°C with a wind speed of 12 km/h.
The conditions are clear skies.
```

---

## 🧪 Testing

You can experiment with the agent's logic and tool outputs interactively using the provided Jupyter Notebook:

```bash
# Ensure Jupyter is installed, then run:
jupyter notebook tests/test.ipynb
```

---

## 🔮 Roadmap

*  Multi-day weather forecasts
*  Severe weather alerts and push notifications
*  FastAPI backend integration
*  Streamlit/Gradio visual dashboard
*  Voice assistant compatibility

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the Project
2. Create your Feature Branch

```bash
git checkout -b feature/AmazingFeature
```

3. Commit your Changes

```bash
git commit -m "Add some AmazingFeature"
```

4. Push to the Branch

```bash
git push origin feature/AmazingFeature
```

5. Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 👨‍💻 Author

**Siddharth Singh**
AI/ML Developer | Rust Enthusiast | Agentic AI Explorer

GitHub Profile • LinkedIn

---

⭐ If you found this project useful or interesting, please consider giving it a star!

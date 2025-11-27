# 🧳 Travel Planning Assistant using LangGraph + MCP

Successfully developed an intelligent **Travel Planner Assistant** powered by **LangGraph**, **FastMCP**, and **Modular MCP Servers**, providing real-time trip planning with flights, hotels, weather, places, and timezone information—all orchestrated through an LLM agent and delivered via a clean Streamlit UI.

---

## 🚀 Overview

This project implements a fully modular, agent-driven travel planning system capable of:

- Retrieving **live flight options** using the Amadeus API  
- Searching **hotel availability & pricing**  
- Fetching **real-time weather** for any city  
- Recommending **nearby attractions and points of interest**  
- Detecting **timezones and local times**  
- Coordinating results through a **LangGraph-powered LLM workflow**

The system uses **MCP (Model Context Protocol)** servers for each data source—allowing plug-and-play scalability, clean separation of services, and fault-tolerant tool execution.

---

## 🧩 Key Components

### **1. LangGraph Workflow**
- Core agent loop implemented with LangGraph  
- Integrated routing via `ToolNode` and `tools_condition`  
- Persistent thread state using SQLite checkpoints  
- Handles user queries, tool execution, and final answer synthesis  

### **2. MCP Servers (FastMCP-based)**

Each microservice runs as an independent MCP server:

- `flights_mcp.py` → Live flights via Amadeus API  
- `hotels_mcp.py` → Hotel search & filtering  
- `weather_mcp.py` → Current weather + forecast  
- `places_mcp.py` → Attractions & POIs  
- `math_mcp.py` → Utility math operations  
- Fully typed tool definitions with FastMCP decorators  

### **3. Streamlit Interface**
- Chat-style conversation interface  
- Threads persisted and reloadable  
- Supports user messages, agent messages, and tool results  
- Real-time server logs shown inside Streamlit  

---

## 🔍 Features

- End-to-end travel planning from a single prompt  
- Real-time data retrieval (flights, hotels, weather, timezone)  
- LLM-based reasoning with multiple MCP tools  
- Robust agent orchestration using LangGraph  
- Stateless UI, stateful backend with saved chat threads  
- Easily extendable (add new MCP tools in minutes)

---

## 🛠️ Tech Stack

- **LangGraph** – LLM agent workflow engine  
- **FastMCP + MCP** – Modular tool servers  
- **LangChain** – Message and tool abstractions  
- **Streamlit** – Frontend UI  
- **Amadeus SDK** – Flight data retrieval  
- **Geopy & TimezoneFinder** – Geo and timezone utilities  
- **Python 3.10+**

---

## 📂 Project Structure

```bash
├── app.py                      # Streamlit frontend
├── travel_planner_chatbot.py   # LangGraph agent & workflow
├── flights_mcp.py              # Live flight search MCP server
├── hotels_mcp.py               # Hotel search MCP server
├── weather_mcp.py              # Weather MCP server
├── places_mcp.py               # Places & attractions MCP server
├── math_mcp.py                 # Utility MCP server
├── requirements.txt            # Dependencies
└── README.md
```

---

## 🧠 How It Works
	1.	User sends a travel-related query through Streamlit.
	2.	LangGraph agent receives the message and evaluates needed tools.
	3.	Tools are executed via MCP servers running in separate processes.
	4.	Agent collects tool results, reasons over them, and generates a plan.
	5.	Final structured response is sent back to the UI.

---

### 📦 Installation & Setup

Clone repo:

```bash
git clone https://github.com/your-username/travel-planning-assistant-using-fastmcp
cd travel-planning-assistant-using-fastmcp
```

Install requirements:

```bash
pip install -r requirements.txt
```

Start MCP servers:

```bash
python flights_mcp.py
python hotels_mcp.py
python weather_mcp.py
python places_mcp.py
python math_mcp.py
```

Run Streamlit app

```bash
streamlit run app.py
```

---

## 🤝 Contributions

Pull requests are welcome!
You can add more MCP tools (car rentals, restaurants, currency converters, maps, etc.) to extend functionality.

## 📜 License

MIT License.
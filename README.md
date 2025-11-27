\section*{\emoji{1f9f3} Travel Planning Assistant using LangGraph + MCP}

Successfully developed an intelligent \textbf{Travel Planner Assistant} powered by \textbf{LangGraph}, \textbf{FastMCP}, and \textbf{Modular MCP Servers}, providing real-time trip planning with flights, hotels, weather, places, and timezone information—all orchestrated through an LLM agent and delivered via a clean Streamlit UI.

\noindent\rule{\linewidth}{0.4pt}

\section*{\emoji{1f680} Overview}

This project implements a fully modular, agent-driven travel planning system capable of:

\begin{itemize}
    \item Retrieving live flight options using the Amadeus API
    \item Searching hotel availability \& pricing
    \item Fetching real-time weather for any city
    \item Recommending nearby attractions and points of interest
    \item Detecting timezones and local times
    \item Coordinating results through a LangGraph-powered LLM workflow
\end{itemize}

The system uses \textbf{MCP (Model Context Protocol)} servers for each data source—allowing plug-and-play scalability, clean separation of services, and fault-tolerant tool execution.

\noindent\rule{\linewidth}{0.4pt}

\section*{\emoji{1f9e9} Key Components}

\subsection*{1. LangGraph Workflow}
\begin{itemize}
    \item Core agent loop implemented with LangGraph
    \item Integrated routing via \texttt{ToolNode} and \texttt{tools\_condition}
    \item Persistent thread state using SQLite checkpoints
    \item Handles user queries, tool execution, and final answer synthesis
\end{itemize}

\subsection*{2. MCP Servers (FastMCP-based)}
Each microservice runs as an independent MCP server:
\begin{itemize}
    \item \texttt{flights\_mcp.py} → Live flights via Amadeus API
    \item \texttt{hotels\_mcp.py} → Hotel search \& filtering
    \item \texttt{weather\_mcp.py} → Current weather + forecast
    \item \texttt{places\_mcp.py} → Attractions \& POIs
    \item \texttt{math\_mcp.py} → Utility math operations
    \item Fully typed tool definitions with FastMCP decorators
\end{itemize}

\subsection*{3. Streamlit Interface}
\begin{itemize}
    \item Chat-style conversation interface
    \item Threads persisted and reloadable
    \item Supports user messages, agent messages, and tool results
    \item Real-time server logs shown inside Streamlit
\end{itemize}

\noindent\rule{\linewidth}{0.4pt}

\section*{\emoji{1f50d} Features}
\begin{itemize}
    \item End-to-end travel planning from a single prompt
    \item Real-time data retrieval (flights, hotels, weather, timezone)
    \item LLM-based reasoning with multiple MCP tools
    \item Robust agent orchestration using LangGraph
    \item Stateless UI, stateful backend with saved chat threads
    \item Easily extendable (add new MCP tools in minutes)
\end{itemize}

\noindent\rule{\linewidth}{0.4pt}

\section*{\emoji{1f6e0} Tech Stack}
\begin{itemize}
    \item LangGraph – LLM agent workflow engine
    \item FastMCP + MCP – Modular tool servers
    \item LangChain – Message and tool abstractions
    \item Streamlit – Frontend UI
    \item Amadeus SDK – Flight data retrieval
    \item Geopy \& TimezoneFinder – Geo and timezone utilities
    \item Python 3.10+
\end{itemize}
# Travel Agent Assistant with MCP Toolbox and ADK

An intelligent AI-powered travel assistant built using Google's Agent Development Kit (ADK) and MCP Toolbox for Databases. This application helps users search for hotels through a beautiful Streamlit interface.

## 🌟 Features

- **Smart Hotel Search**: Find hotels by location or name
- **AI-Powered Agent**: Uses Gemini 2.0 Flash for intelligent responses
- **Database Integration**: MCP Toolbox for secure database access
- **Beautiful UI**: Clean, modern Streamlit interface
- **Production-Ready**: Built with Google's ADK framework

## 🏗️ Architecture

```
User Interface (Streamlit)
    ↓
Travel Agent (Google ADK)
    ↓
MCP Toolbox Server
    ↓
PostgreSQL Database
```

## 📋 Prerequisites

- Python 3.9+
- PostgreSQL 15+
- Google Cloud Project

## 🚀 Quick Start

### 1. Setup

```bash
# Create project directory
mkdir travel-agent-streamlit
cd travel-agent-streamlit

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Setup PostgreSQL Database

```bash
# Run database setup
psql -U postgres -f database_setup.sql
```

### 3. Configure Environment

Update `.env` with your settings:
```env
GOOGLE_GENAI_USE_VERTEXAI=1
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
MCP_TOOLBOX_URL=http://localhost:5000
```

### 4. Start MCP Toolbox

```bash
cd mcp-toolbox
./toolbox --tools-file tools.yaml
```

### 5. Run Streamlit App

```bash
streamlit run streamlit_app.py
```

Access at `http://localhost:8501`

## 💡 Usage

Ask questions like:
- "Find hotels in Basel"
- "Show me luxury hotels in Zurich"
- "Tell me about the Hilton Basel"

## 📁 Project Structure

```
travel-agent-streamlit/
├── requirements.txt
├── .env
├── streamlit_app.py
├── agent.py
├── tools.yaml
└── database_setup.sql
```

## 🚢 Deployment

See DEPLOYMENT.md for:
- Local development
- Google Cloud Run
- Docker Compose
- Kubernetes

## 📚 Resources

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [MCP Toolbox Documentation](https://googleapis.github.io/genai-toolbox/)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

Built during DevFest Vizag 2025 at GITAM with ❤️
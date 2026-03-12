# 🚀 The Marketing Department | Agency

A high-performance, multi-agent marketing agency built with the **Google Agent Development Kit (ADK)** and powered by **Gemini 3 Flash**. This agency coordinates specialized AI experts to deliver grounded, real-time marketing strategies and deep data analytics.

## ✨ Features

- **Brainy Orchestration**: A central `Marketing Manager` that analyzes complex missions and delegates tasks.
- **Advanced Data Analytics**: 
    - **Data Analyst**: Expert in BigQuery OTA datasets and **Market Penetration**. It joins official tourism data (MOTS) with internal bookings to calculate True Market Share.
    - **Titan Analyst**: Specialized in the **Thailand (TITAN) Demo**, synthesizing governmental arrival data and Agoda internal performance.
- **Specialized Expert Team**:
    - **SEO Specialist**: Search engine visibility and SERP analysis.
    - **App Store Optimizer (ASO)**: Mobile app growth and conversion.
    - **Social Media Strategist**: Brand authority and community building.
    - **Content Creator**: Compelling storytelling and editorial planning.
- **Low-Latency Intelligence**: Powered by `gemini-3-flash-preview` for snappier, more efficient responses.
- **Persistent Memory**: Uses session state to ensure agents remember sub-task outputs across multiple turns.
- **Premium UI**: A sleek, glassmorphism chat interface with light/dark theme support.

## 📊 Data Foundation
This agency is powered by a multi-source BigQuery data layer that correlates internal Agoda performance with official travel statistics.
- **Detailed Schema**: See [DATA_FOUNDATION.md](DATA_FOUNDATION.md) for full table definitions and join logic.

## 🏗️ Architecture

The system follows a hierarchical multi-agent pattern:

```mermaid
graph TD
    User([User]) --> UI[Chat UI - Glassmorphism]
    UI --> Server[Python aiohttp Server]
    Server --> ADK[Google ADK Runner]
    ADK --> Manager[Marketing Manager - Orchestrator]
    Manager --> Data[Data Analyst - BigQuery]
    Manager --> Titan[Titan Analyst - Thailand Demo]
    Manager --> SEO[SEO Specialist]
    Manager --> Social[Social Media Specialist]
    Manager --> Content[Content Strategist]
    Data & Titan & SEO & Social & Content --> Vertex[Gemini 3 Flash via Vertex AI]
    Vertex --> Grounding[Google Search & Maps]
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.10+
- Google Cloud Project with Vertex AI enabled.
- `gcloud` CLI installed and authenticated.

### 1. Clone the Repository
```bash
git clone https://github.com/emailandy/MarketingADKagent.git
cd MarketingADKagent
```

### 2. Set Up Environment
Create a virtual environment and install the required dependencies.
```bash
python -m venv venv
source venv/bin/activate
pip install google-adk aiohttp pandas google-cloud-bigquery
```

### 3. Configure Authentication
Ensure your Google Cloud credentials are set up:
```bash
gcloud auth application-default login
```

### 4. Run the Agency
```bash
python main.py
```
The agency will be live at `http://localhost:8080`.

## 📂 Project Structure
- `backend/agents/`: Agent definitions and personas.
- `frontend/ui/`: Static files and templates for the glassmorphism UI.
- `data/`: Mock datasets for MOTS arrivals and Agoda bookings.
- `main.py`: The unified entry point serving the app and ADK logic.

---
Built with ❤️ using [Google ADK](https://github.com/google/adk-python).

# Case 3: End-to-End Mini Project

## Prerequisites

- [Python 3.12](https://www.python.org/downloads/) or higher
- [Google API Key](https://aistudio.google.com/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (optional)
- [Docker](https://www.docker.com/get-started/) (optional)

## Setup

**1. Clone the repository**

```bash
git clone https://github.com/taufiqdp/case-3-mini-project.git
cd case-3-mini-project
```

**2. Set up environment variables**

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Click "Get API Key" and create/copy your key
4. Rename `.env.example` to `.env` and add your Google API key:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

## Usage (Python)

**1. Installation:**

### Option A: Using uv (Recommended)

```bash
uv sync
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Option B: Using pip

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

**2. Run the application**

```bash
python server.py
```

The server will start on http://localhost:8000

## Usage (Docker)

**1. Run the Docker container**

```bash
docker compose up -d
```

The server will start on http://localhost:8000

# Case 3: End-to-End Mini Project

## Prerequisites

- [Python 3.12](https://www.python.org/downloads/) or higher
- [Google API Key](https://aistudio.google.com/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (optional)

## Installation

### Option 1: Using UV (Recommended)

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd case-3-mini-project
   ```

2. **Install dependencies**

   ```bash
   uv sync
   ```

3. **Set up environment variables**
   Rename the `.env.example` file to `.env` in the project root and add your Google API key:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

### Option 2: Using pip

1. **Clone the repository**

   ```bash
   git clone https://github.com/taufiqdp/case-3-mini-project.git
   cd case-3-mini-project
   ```

2. **Create virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Rename the `.env.example` file to `.env` in the project root and add your Google API key:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## Getting Your Google API Key

1. Go to the [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Click on "Get API Key"
4. Create a new API key or use an existing one
5. Copy the API key and add it to your `.env` file

## Usage

### Starting the Server

```bash
python server.py
```

The server will start on `http://localhost:8000`

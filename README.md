# RAG Frontend

Simple, clean FastAPI frontend with TailwindCSS for the RAG Chat System.

## Features

- ✅ **Simple FastAPI Server** - No complex build process
- ✅ **TailwindCSS** - Beautiful, responsive design
- ✅ **2 Pages** - Chat and Admin
- ✅ **Easy Customization** - Change colors via CSS variables
- ✅ **Streaming Chat** - Real-time token streaming
- ✅ **Batch Ingestion** - Add multiple documents at once

## Quick Start

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Server

```bash
python main.py
```

Visit `http://localhost:3000`

## Pages

- **`/chat`** - Chat interface with streaming support
- **`/admin`** - Knowledge ingestion (single & batch)

## Customization

Edit `templates/base.html` to customize colors:

```css
:root {
    --primary: #3b82f6;        /* Main brand color */
    --primary-dark: #2563eb;   /* Hover state */
    --secondary: #8b5cf6;      /* Secondary color */
    --success: #10b981;        /* Success messages */
    --error: #ef4444;          /* Error messages */
    --background: #ffffff;     /* Page background */
    --surface: #f9fafb;        /* Card/surface background */
    --text: #111827;           /* Primary text */
    --text-muted: #6b7280;     /* Muted text */
    --border: #e5e7eb;         /* Borders */
}
```

## Configuration

Set API base URL via environment variable:

```bash
export API_BASE_URL=http://localhost:8000
python main.py
```

Or edit `main.py`:

```python
API_BASE_URL = "http://localhost:8000"
```

## Project Structure

```
frontend/
├── main.py              # FastAPI server
├── requirements.txt     # Python dependencies
├── templates/
│   ├── base.html       # Base template with header
│   ├── chat.html       # Chat page
│   └── admin.html      # Admin page
└── README.md
```

## License

MIT

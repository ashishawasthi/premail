# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

PreMail is a Flask-based email preview application for testing marketing emails across different devices and email clients. It's a stateless, lightweight application with no database requirements.

## Architecture

### Core Application Structure

**Flask Application ([app.py](app.py))**
- Simple Flask app with 4 main routes:
  - `/` - Main form interface
  - `/preview` - POST endpoint that renders email preview
  - `/api/preview` - JSON API endpoint for programmatic access
  - `/health` - Health check endpoint
- The app runs on port 8080 by default (configured in [app.py:80](app.py#L80))
- Maximum content size: 16MB

**Configuration System ([config.py](config.py))**
- Three configuration classes: `Config` (base), `DevelopmentConfig`, `ProductionConfig`
- Environment variables for customization:
  - `PREMAIL_HOST` - Server host (default: 0.0.0.0)
  - `PREMAIL_PORT` - Server port (default: 5000, but [app.py](app.py) overrides to 8080)
  - `PREMAIL_DEBUG` - Debug mode
  - `SECRET_KEY` - Flask secret key
  - `CORS_ENABLED` - CORS toggle

**Presets System ([presets.py](presets.py))**
- `DEVICE_PRESETS` - Dictionary containing device viewport configurations (iPhone 17, Galaxy S25, iPad Pro, etc.)
- `EMAIL_CLIENT_PRESETS` - Dictionary containing email client styling (Gmail, Outlook, Apple Mail, Yahoo Mail)
- Each preset includes dimensions, colors, fonts, and UI toolbar settings
- These presets are passed to templates for dynamic device/client switching

### Template Architecture

**Main Interface ([templates/index.html](templates/index.html))**
- Landing page with form for subject, HTML content, and image URLs
- Contains "Load Sample" functionality for demo purposes

**Preview Interface ([templates/preview.html](templates/preview.html))**
- Receives `subject`, `content`, `images`, `devices`, and `clients` from backend
- JavaScript-based device and client switcher
- Dynamically applies viewport dimensions and styling based on selected preset
- Renders authentic email client toolbars (Gmail archive/delete buttons, Outlook ribbon, etc.)

### Static Assets

**Styling ([static/style.css](static/style.css))**
- Elegant, enterprise-friendly color scheme
- Responsive design with device simulation capabilities
- Email client-specific toolbar styles

## Development Commands

### Running the Application

**Quick Start (Recommended):**
```bash
./run.sh
```
This automatically creates a venv, installs dependencies, and starts the server on port 8080.

**Manual Development:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

**Production Deployment:**
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

**Docker:**
```bash
docker-compose up -d
# OR
docker build -t premail .
docker run -p 5000:5000 premail
```

### Testing the API

```bash
curl -X POST http://localhost:8080/api/preview \
  -H "Content-Type: application/json" \
  -d '{
    "subject": "Test Email",
    "content": "<h1>Hello World</h1>",
    "images": ["https://example.com/image.jpg"]
  }'
```

### Health Check

```bash
curl http://localhost:8080/health
```

## Key Design Patterns

### Stateless Architecture
- No database or session storage
- All preview data is passed via POST requests
- Makes horizontal scaling trivial

### Preset-Driven Configuration
- Device and email client configurations are centralized in [presets.py](presets.py)
- To add new devices or email clients, add entries to `DEVICE_PRESETS` or `EMAIL_CLIENT_PRESETS`
- Frontend automatically picks up new presets via template rendering

### Template Data Flow
1. User submits form at `/`
2. POST to `/preview` with `subject`, `content`, `images`
3. [app.py:20-42](app.py#L20-L42) processes data and passes to template along with presets
4. [preview.html](templates/preview.html) renders with JavaScript-based device/client switcher

## Modifying Devices or Email Clients

To add a new device preset in [presets.py](presets.py):
```python
'new-device': {
    'name': 'Device Name',
    'width': '400px',
    'height': '800px',
    'icon': '📱'
}
```

To add a new email client in [presets.py](presets.py):
```python
'new-client': {
    'name': 'Client Name',
    'icon': '📧',
    'background': '#ffffff',
    'font': 'Arial, sans-serif',
    'max_width': '700px',
    'header_color': '#f0f0f0',
    'toolbar_color': '#ffffff',
    'primary_color': '#333333',
    'has_toolbar': True  # Set to False if no toolbar needed
}
```

## Port Configuration Note

There's a discrepancy in port configuration:
- [config.py](config.py) defaults to port 5000
- [app.py:80](app.py#L80) hardcodes port 8080
- [run.sh](run.sh) references port 8080
- When running directly with `python app.py`, the application uses **8080**
- When using gunicorn or Docker, the port can be configured via the deployment command

## Dependencies

Minimal Python dependencies ([requirements.txt](requirements.txt)):
- Flask 3.0.0 - Web framework
- gunicorn 21.2.0 - Production WSGI server
- Werkzeug 3.0.1 - WSGI utility library

Python 3.7+ required.

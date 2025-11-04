# PreMail - Email Preview Application

A simple, lightweight email preview application for marketing emails with images. Easily run on desktop machines or Linux servers.

## Features

- Preview marketing emails with embedded images
- Support for HTML email content
- Image rendering from URLs
- Responsive email preview
- Easy to deploy and run
- No database required

## Requirements

- Python 3.7 or higher
- pip (Python package manager)

## Quick Start

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd premail
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

#### Easy Start (Recommended):

**Linux/macOS:**
```bash
./run.sh
```

**Windows:**
```bash
run.bat
```

These scripts will automatically create a virtual environment, install dependencies, and start the application.

#### Manual Start:

**On Desktop/Development:**
```bash
python app.py
```

**On Linux Server (Production):**
```bash
# Using gunicorn for production
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

#### Docker (Easiest for Server Deployment):

```bash
# Build and run with Docker Compose
docker-compose up -d

# Or build and run with Docker directly
docker build -t premail .
docker run -p 5000:5000 premail
```

The application will be available at `http://localhost:5000`

## Usage

1. Open the application in your web browser
2. Enter your email subject
3. Paste your HTML email content
4. Add image URLs (one per line) if needed
5. Click "Preview Email" to see the rendered preview

## API Usage

You can also use the API endpoint directly:

```bash
curl -X POST http://localhost:5000/api/preview \
  -H "Content-Type: application/json" \
  -d '{
    "subject": "Marketing Campaign",
    "content": "<h1>Hello!</h1><p>Check out our products!</p>",
    "images": ["https://example.com/image1.jpg", "https://example.com/image2.jpg"]
  }'
```

## Configuration

Edit `config.py` to customize:
- Host and port settings
- Debug mode
- Maximum content size

## Project Structure

```
premail/
├── app.py              # Main Flask application
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── run.sh              # Linux/macOS startup script
├── run.bat             # Windows startup script
├── Dockerfile          # Docker container configuration
├── docker-compose.yml  # Docker Compose configuration
├── templates/          # HTML templates
│   ├── index.html     # Main interface
│   └── preview.html   # Email preview template
└── static/            # Static assets (CSS, JS)
    └── style.css      # Styles
```

## License

MIT License

# PreMail - Email Preview Application

A simple, lightweight email preview application for marketing emails with images. Easily run on desktop machines or Linux servers.

## Features

- **Multi-Device Preview**: Test emails on popular device sizes
  - iPhone 17 & iPhone 17 Pro
  - Samsung Galaxy S25 & S25 Ultra
  - iPad Pro
  - Desktop & Tablet views
- **Email Client Simulation**: Preview how emails appear in different clients with authentic UI
  - Gmail (with archive, delete, and action buttons)
  - Outlook (with Microsoft-style toolbar)
  - Apple Mail (with iOS/macOS design)
  - Yahoo Mail (with Yahoo interface)
- **HTML Email Support**: Full support for HTML content with inline styles
- **Image Gallery**: Display and manage image URLs
- **Responsive Design**: Beautiful, modern interface
- **Easy Deployment**: Run on desktop or server with minimal setup
- **No Database Required**: Completely stateless application
- **Print-Friendly**: Print preview for documentation

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

### Creating a Preview

1. Open the application in your web browser
2. Enter your email subject
3. Paste your HTML email content
4. Add image URLs (one per line) if needed
5. Click "Preview Email" to see the rendered preview

### Testing Across Devices and Clients

In the preview window:
1. Use the **Device** dropdown to switch between:
   - Desktop view
   - iPhone 17 / 17 Pro
   - Samsung Galaxy S25 / S25 Ultra
   - iPad Pro
   - Generic Tablet
2. Use the **Email Client** dropdown to simulate:
   - **Gmail** - Complete with archive, delete, and action buttons just like the real app
   - **Outlook** - Microsoft-style toolbar with flag and archive options
   - **Apple Mail** - iOS/macOS design with reply and compose buttons
   - **Yahoo Mail** - Yahoo's purple-themed interface with star and move actions
3. Each client displays authentic toolbars and UI elements
4. See how your email renders in different environments instantly!

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
├── presets.py          # Device and email client presets
├── requirements.txt    # Python dependencies
├── run.sh              # Linux/macOS startup script
├── run.bat             # Windows startup script
├── Dockerfile          # Docker container configuration
├── docker-compose.yml  # Docker Compose configuration
├── templates/          # HTML templates
│   ├── index.html     # Main interface
│   └── preview.html   # Email preview with device/client switcher
└── static/            # Static assets (CSS, JS)
    └── style.css      # Styles
```

## License

MIT License

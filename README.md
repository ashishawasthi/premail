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
python3 -m venv venv
. ./venv/bin/activate
pip3 install -r requirements.txt
```

### Running the Application

#### Easy Start (Recommended):

**Linux/macOS:**
```bash
. ./venv/bin/activate
./run.sh
```

**Windows:**
```
sh venv\bin\activate
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

## Testing

PreMail includes automated end-to-end tests using Playwright, available in TypeScript, Java, and Python.

### TypeScript/Playwright Tests

**Prerequisites:**
- Node.js 16 or higher
- npm

**Setup and Run:**

```bash
# Install dependencies
npm install

# Install Playwright browsers
npx playwright install

# Run tests (headless mode)
npm test

# Run tests with visible browser
npm run test:headed

# Run tests in debug mode
npm run test:debug

# Run tests in UI mode (interactive)
npm run test:ui
```

**Test Location:** `tests/email-preview.spec.ts`

### Java/Playwright Tests

**Prerequisites:**
- Java 11 or higher
- Maven

**Setup and Run:**

```bash
# First time setup - install Playwright browsers
mvn exec:java -e -D exec.mainClass=com.microsoft.playwright.CLI -D exec.args="install"

# Run all tests
mvn test

# Run with verbose output
mvn test -X

# Run specific test class
mvn test -Dtest=EmailPreviewTest
```

**Test Location:** `src/test/java/com/premail/EmailPreviewTest.java`

### Python/Playwright Tests

**Prerequisites:**
- Python 3.7 or higher
- pip

**Setup:**

First, install test dependencies and Playwright browsers:

```bash
# Install test dependencies
pip3 install -r requirements-test.txt

# Install Playwright browsers
playwright install
```

**Run Tests:**

```bash
# Run all tests
pytest

# Run tests with verbose output
pytest -v

# Run tests with live logs
pytest -s

# Run tests in parallel (faster)
pytest -n auto

# Generate HTML report
pytest --html=test-results/report.html
```

**Test Location:** `tests_python/test_email_preview.py`

### What the Tests Do

All test suites perform the same validations:
1. Navigate to the application homepage
2. Click "Load Sample" to populate the form with sample email content
3. Click "Preview Email" to open the preview in a new window
4. Verify the promotion image is displayed correctly
5. Verify the "DBS digiWealth" heading is visible

The tests automatically start the Flask server (via `run.sh`) before running, so you don't need to start it manually.

## Configuration

Edit `config.py` to customize:
- Host and port settings
- Debug mode
- Maximum content size

## Project Structure

```
premail/
├── app.py                    # Main Flask application
├── config.py                 # Configuration settings
├── presets.py                # Device and email client presets
├── requirements.txt          # Python application dependencies
├── requirements-test.txt     # Python test dependencies
├── run.sh                    # Linux/macOS startup script
├── run.bat                   # Windows startup script
├── Dockerfile                # Docker container configuration
├── docker-compose.yml        # Docker Compose configuration
├── package.json              # Node.js dependencies for TypeScript tests
├── playwright.config.ts      # Playwright configuration for TypeScript
├── pytest.ini                # Pytest configuration for Python tests
├── pom.xml                   # Maven configuration for Java tests
├── templates/                # HTML templates
│   ├── index.html           # Main interface
│   └── preview.html         # Email preview with device/client switcher
├── static/                  # Static assets (CSS, JS)
│   └── style.css            # Styles
├── tests/                   # TypeScript/Playwright tests
│   └── email-preview.spec.ts
├── tests_python/            # Python/Playwright tests
│   ├── __init__.py
│   ├── conftest.py          # Pytest configuration
│   └── test_email_preview.py
└── src/test/java/           # Java/Playwright tests
    └── com/premail/
        └── EmailPreviewTest.java
```

## License

MIT License

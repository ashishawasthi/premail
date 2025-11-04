# PreMail Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Get the Code
```bash
git clone <repository-url>
cd premail
```

### Step 2: Run the Application

Choose your preferred method:

#### Option A: Use the Run Script (Easiest)
**Linux/macOS:**
```bash
chmod +x run.sh
./run.sh
```

**Windows:**
```bash
run.bat
```

#### Option B: Docker (Best for Servers)
```bash
docker-compose up -d
```

#### Option C: Manual Python
```bash
pip install -r requirements.txt
python app.py
```

### Step 3: Open Your Browser
Navigate to: **http://localhost:5000**

## 📝 Create Your First Preview

1. **Enter Subject**: Type your email subject line
2. **Add Content**: Paste your HTML email content
3. **Add Images** (optional): Add image URLs, one per line
4. **Preview**: Click "Preview Email" button

## 📱 Test Across Devices & Email Clients

In the preview window, you can:

**Switch Devices:**
- iPhone 17 / iPhone 17 Pro
- Samsung Galaxy S25 / S25 Ultra
- iPad Pro
- Desktop / Tablet views

**Switch Email Clients:**
- Gmail
- Outlook
- Apple Mail
- Yahoo Mail
- ProtonMail

Simply use the dropdown menus in the preview toolbar to see how your email looks!

## 💡 Sample Email

Click the "Load Sample" button on the main page to see an example!

## 🔧 Common Tasks

### Change Port
Edit `app.py` or set environment variable:
```bash
export PREMAIL_PORT=8080
python app.py
```

### Production Deployment
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Use API
```bash
curl -X POST http://localhost:5000/api/preview \
  -H "Content-Type: application/json" \
  -d '{
    "subject": "Test Email",
    "content": "<h1>Hello World</h1>",
    "images": []
  }'
```

## ❓ Troubleshooting

**Port already in use?**
- Change the port in `app.py` (default is 5000)
- Or kill the process using the port

**Dependencies not installing?**
- Make sure you have Python 3.7+ installed
- Try upgrading pip: `pip install --upgrade pip`

**Can't access from other machines?**
- Make sure the app is bound to `0.0.0.0` (default)
- Check your firewall settings

## 📚 More Information
See [README.md](README.md) for full documentation.

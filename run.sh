#!/bin/bash

# PreMail - Email Preview Application Runner
# Simple script to run the application

echo "🚀 Starting PreMail - Email Preview Application"
echo "=============================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "Please install Python 3.7 or higher"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install/update dependencies
echo "📥 Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt

# Run the application
echo "✅ Starting application..."
echo ""
echo "Application will be available at:"
echo "  http://localhost:5000"
echo "  http://127.0.0.1:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python3 app.py

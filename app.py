#!/usr/bin/env python3
"""
PreMail - Email Preview Application
A simple Flask application for previewing marketing emails with images
"""

from flask import Flask, render_template, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max content

@app.route('/')
def index():
    """Main page with email input form"""
    return render_template('index.html')

@app.route('/preview', methods=['POST'])
def preview():
    """Render email preview"""
    try:
        subject = request.form.get('subject', 'No Subject')
        content = request.form.get('content', '')
        images = request.form.get('images', '').strip()

        # Parse image URLs
        image_list = [img.strip() for img in images.split('\n') if img.strip()]

        # Get current timestamp for preview
        preview_date = datetime.now().strftime('%B %d, %Y at %I:%M %p')

        return render_template('preview.html',
                             subject=subject,
                             content=content,
                             images=image_list,
                             preview_date=preview_date)
    except Exception as e:
        return f"Error rendering preview: {str(e)}", 400

@app.route('/api/preview', methods=['POST'])
def api_preview():
    """API endpoint for email preview"""
    try:
        data = request.get_json()

        if not data:
            return jsonify({'error': 'No data provided'}), 400

        subject = data.get('subject', 'No Subject')
        content = data.get('content', '')
        images = data.get('images', [])

        preview_date = datetime.now().strftime('%B %d, %Y at %I:%M %p')

        return jsonify({
            'success': True,
            'subject': subject,
            'content': content,
            'images': images,
            'preview_date': preview_date
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'premail'}), 200

if __name__ == '__main__':
    # Create templates and static directories if they don't exist
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)

    # Run the application
    app.run(host='0.0.0.0', port=5000, debug=True)

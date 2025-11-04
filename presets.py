"""
Device and Email Client Presets for PreMail
Contains viewport dimensions and email client specific styles
"""

DEVICE_PRESETS = {
    'desktop': {
        'name': 'Desktop',
        'width': '100%',
        'height': '100%',
        'icon': '🖥️'
    },
    'iphone-17': {
        'name': 'iPhone 17',
        'width': '393px',
        'height': '852px',
        'icon': '📱'
    },
    'iphone-17-pro': {
        'name': 'iPhone 17 Pro',
        'width': '430px',
        'height': '932px',
        'icon': '📱'
    },
    'galaxy-s25': {
        'name': 'Samsung Galaxy S25',
        'width': '412px',
        'height': '915px',
        'icon': '📱'
    },
    'galaxy-s25-ultra': {
        'name': 'Samsung Galaxy S25 Ultra',
        'width': '480px',
        'height': '1020px',
        'icon': '📱'
    },
    'ipad-pro': {
        'name': 'iPad Pro',
        'width': '1024px',
        'height': '1366px',
        'icon': '📱'
    },
    'tablet': {
        'name': 'Tablet (Generic)',
        'width': '768px',
        'height': '1024px',
        'icon': '📱'
    }
}

EMAIL_CLIENT_PRESETS = {
    'gmail': {
        'name': 'Gmail',
        'icon': '📧',
        'background': '#f2f6fc',
        'font': '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
        'max_width': '700px'
    },
    'outlook': {
        'name': 'Outlook',
        'icon': '📧',
        'background': '#ffffff',
        'font': 'Calibri, Arial, sans-serif',
        'max_width': '680px'
    },
    'apple-mail': {
        'name': 'Apple Mail',
        'icon': '📧',
        'background': '#e5e5ea',
        'font': '-apple-system, BlinkMacSystemFont, sans-serif',
        'max_width': '750px'
    },
    'yahoo': {
        'name': 'Yahoo Mail',
        'icon': '📧',
        'background': '#f5f5f5',
        'font': 'Arial, sans-serif',
        'max_width': '700px'
    },
    'protonmail': {
        'name': 'ProtonMail',
        'icon': '📧',
        'background': '#f6f7fb',
        'font': '-apple-system, BlinkMacSystemFont, sans-serif',
        'max_width': '720px'
    },
    'default': {
        'name': 'Default',
        'icon': '📧',
        'background': '#ffffff',
        'font': 'Arial, sans-serif',
        'max_width': '100%'
    }
}

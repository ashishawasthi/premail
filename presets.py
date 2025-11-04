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
        'font': 'Roboto, Arial, sans-serif',
        'max_width': '700px',
        'header_color': '#ffffff',
        'toolbar_color': '#f5f5f5',
        'primary_color': '#1a73e8',
        'has_toolbar': True
    },
    'outlook': {
        'name': 'Outlook',
        'icon': '📧',
        'background': '#faf9f8',
        'font': '"Segoe UI", Calibri, Arial, sans-serif',
        'max_width': '680px',
        'header_color': '#0078d4',
        'toolbar_color': '#ffffff',
        'primary_color': '#0078d4',
        'has_toolbar': True
    },
    'apple-mail': {
        'name': 'Apple Mail',
        'icon': '📧',
        'background': '#ffffff',
        'font': '-apple-system, BlinkMacSystemFont, "SF Pro Display", sans-serif',
        'max_width': '750px',
        'header_color': '#f5f5f5',
        'toolbar_color': '#fafafa',
        'primary_color': '#007aff',
        'has_toolbar': True
    },
    'yahoo': {
        'name': 'Yahoo Mail',
        'icon': '📧',
        'background': '#f5f5f5',
        'font': 'Arial, sans-serif',
        'max_width': '700px',
        'header_color': '#6e00d1',
        'toolbar_color': '#ffffff',
        'primary_color': '#6e00d1',
        'has_toolbar': True
    },
    'default': {
        'name': 'Default',
        'icon': '📧',
        'background': '#ffffff',
        'font': 'Arial, sans-serif',
        'max_width': '100%',
        'header_color': '#f0f0f0',
        'toolbar_color': '#ffffff',
        'primary_color': '#333333',
        'has_toolbar': False
    }
}

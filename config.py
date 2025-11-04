"""
Configuration settings for PreMail application
"""

import os

class Config:
    """Base configuration"""
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'

    # Server settings
    HOST = os.environ.get('PREMAIL_HOST', '0.0.0.0')
    PORT = int(os.environ.get('PREMAIL_PORT', 5000))
    DEBUG = os.environ.get('PREMAIL_DEBUG', 'False').lower() == 'true'

    # Content limits
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

    # CORS settings (if needed)
    CORS_ENABLED = os.environ.get('CORS_ENABLED', 'False').lower() == 'true'


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

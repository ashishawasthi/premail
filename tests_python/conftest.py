"""
Pytest configuration for PreMail tests
"""

import logging
import pytest
from playwright.sync_api import sync_playwright

# Configure logging for tests
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """
    Configure browser context arguments
    """
    return {
        **browser_context_args,
    }


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """
    Configure browser launch arguments
    """
    return {
        **browser_type_launch_args,
        "headless": True,
    }


def pytest_configure(config):
    """
    Pytest configuration hook
    """
    logger.info("Initializing Playwright tests for PreMail")


def pytest_unconfigure(config):
    """
    Pytest cleanup hook
    """
    logger.info("Closing Playwright tests")

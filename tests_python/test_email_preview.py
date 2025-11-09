"""
Email Preview Test using Playwright and Pytest

This test verifies the email preview functionality by:
1. Loading the sample email
2. Opening the preview in a popup
3. Verifying the promotion image is visible
4. Verifying the DBS digiWealth heading is visible
"""

import logging
import os
from datetime import datetime
from pathlib import Path
import pytest
from playwright.sync_api import Page, expect

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def take_screenshot(page: Page, name: str) -> str:
    """
    Takes a screenshot and saves it with a timestamp

    Args:
        page: The Playwright page object
        name: Name/description for the screenshot

    Returns:
        Path to the saved screenshot
    """
    try:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"screenshot_{name}_{timestamp}.png"
        screenshot_dir = Path("test-results") / "screenshots"

        # Create screenshots directory if it doesn't exist
        screenshot_dir.mkdir(parents=True, exist_ok=True)

        screenshot_path = screenshot_dir / filename
        page.screenshot(path=str(screenshot_path), full_page=True)

        logger.warning(f"⚠️  SCREENSHOT SAVED: {screenshot_path}")
        print(f"\n⚠️  SCREENSHOT SAVED: {screenshot_path}\n", flush=True)
        return str(screenshot_path)
    except Exception as e:
        logger.error(f"Failed to take screenshot: {e}")
        return ""


def test_load_sample_email_and_verify_promotion_elements(page: Page):
    """
    Test that loads sample email and verifies promotion elements are visible
    """
    popup = None

    try:
        logger.info("TEST STARTED: Load sample email and verify promotion elements")

        # Navigate to the main page
        logger.info("Step 1: Navigating to http://localhost:8080/")
        page.goto("http://localhost:8080/")
        logger.info("Successfully navigated to main page")

        # Click the "Load Sample" button to populate the form
        logger.info('Step 2: Clicking "Load Sample" button')
        page.get_by_role("button", name="Load Sample").click()
        logger.info('Successfully clicked "Load Sample" button')

        # Set up listener for the popup window that will open
        logger.info("Step 3: Waiting for popup window to open")
        with page.expect_popup() as popup_info:
            # Click "Preview Email" which opens preview in new tab
            logger.info('Step 3a: Clicking "Preview Email" button')
            page.get_by_role("button", name="Preview Email").click()

        popup = popup_info.value
        logger.info("Popup window opened successfully")

        # Wait for the popup to load completely
        logger.info("Step 4: Waiting for popup to load completely")
        popup.wait_for_load_state("networkidle")
        logger.info("Popup loaded successfully (network idle)")

        # Check for the promotion image
        logger.info("Step 5: Verifying promotion image is visible")
        promotion_image = popup.get_by_role("img", name="Promotion")

        try:
            expect(promotion_image).to_be_visible()
            logger.info("✓ ASSERTION PASSED: Promotion image is visible")
        except AssertionError as e:
            logger.error("✗ ASSERTION FAILED: Promotion image is NOT visible")
            take_screenshot(popup, "promotion-image-assertion-failure")
            raise AssertionError(
                "Promotion image with alt text 'Promotion' was not found or not visible in the preview"
            ) from e

        # Check for the DBS digiWealth heading
        logger.info("Step 6: Verifying DBS digiWealth heading is visible")
        dbs_heading = popup.get_by_role("heading", name="DBS digiWealth")

        try:
            expect(dbs_heading).to_be_visible()
            logger.info("✓ ASSERTION PASSED: DBS digiWealth heading is visible")
        except AssertionError as e:
            logger.error("✗ ASSERTION FAILED: DBS digiWealth heading is NOT visible")
            take_screenshot(popup, "dbs-heading-assertion-failure")
            raise AssertionError(
                "Heading with text 'DBS digiWealth' was not found or not visible in the preview"
            ) from e

        logger.info("TEST COMPLETED SUCCESSFULLY: All assertions passed")

    except Exception as e:
        logger.error(f"TEST FAILED with exception: {str(e)}")
        if popup:
            take_screenshot(popup, "test-exception-failure")
        raise

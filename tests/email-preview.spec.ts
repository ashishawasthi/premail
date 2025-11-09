import { test, expect, Page } from '@playwright/test';
import * as fs from 'fs';
import * as path from 'path';

/**
 * Takes a screenshot and saves it with a timestamp
 */
async function takeScreenshot(page: Page, name: string): Promise<string> {
  try {
    const timestamp = new Date().toISOString().replace(/[:.]/g, '-').replace('T', '_').split('.')[0];
    const filename = `screenshot_${name}_${timestamp}.png`;
    const screenshotDir = path.join('test-results', 'screenshots');

    // Create screenshots directory if it doesn't exist
    if (!fs.existsSync(screenshotDir)) {
      fs.mkdirSync(screenshotDir, { recursive: true });
    }

    const screenshotPath = path.join(screenshotDir, filename);
    await page.screenshot({ path: screenshotPath, fullPage: true });

    console.warn(`⚠️  SCREENSHOT SAVED: ${screenshotPath}`);
    return screenshotPath;
  } catch (error) {
    console.error('Failed to take screenshot:', error);
    return '';
  }
}

test('load sample email and verify promotion element exists in preview', async ({ page }) => {
  let popup: Page | null = null;

  try {
    console.log('TEST STARTED: Load sample email and verify promotion elements');

    // Navigate to the main page
    console.log('Step 1: Navigating to http://localhost:8080/');
    await page.goto('http://localhost:8080/');
    console.log('Successfully navigated to main page');

    // Click the "Load Sample" button to populate the form
    console.log('Step 2: Clicking "Load Sample" button');
    await page.getByRole('button', { name: 'Load Sample' }).click();
    console.log('Successfully clicked "Load Sample" button');

    // Set up listener for the popup window that will open
    console.log('Step 3: Waiting for popup window to open');
    const popupPromise = page.waitForEvent('popup');

    // Click "Preview Email" which opens preview in new tab
    console.log('Step 3a: Clicking "Preview Email" button');
    await page.getByRole('button', { name: 'Preview Email' }).click();

    // Get the popup window
    popup = await popupPromise;
    console.log('Popup window opened successfully');

    // Wait for the popup to load completely
    console.log('Step 4: Waiting for popup to load completely');
    await popup.waitForLoadState('networkidle');
    console.log('Popup loaded successfully (network idle)');

    // Check for the promotion image
    console.log('Step 5: Verifying promotion image is visible');
    const promotionImage = popup.getByRole('img', { name: 'Promotion' });

    try {
      await expect(promotionImage).toBeVisible();
      console.log('✓ ASSERTION PASSED: Promotion image is visible');
    } catch (error) {
      console.error('✗ ASSERTION FAILED: Promotion image is NOT visible');
      await takeScreenshot(popup, 'promotion-image-assertion-failure');
      throw new Error(`Promotion image with alt text 'Promotion' was not found or not visible in the preview. ${error}`);
    }

    // Check for the DBS digiWealth heading
    console.log('Step 6: Verifying DBS digiWealth heading is visible');
    const dbsHeading = popup.getByRole('heading', { name: 'DBS digiWealth' });

    try {
      await expect(dbsHeading).toBeVisible();
      console.log('✓ ASSERTION PASSED: DBS digiWealth heading is visible');
    } catch (error) {
      console.error('✗ ASSERTION FAILED: DBS digiWealth heading is NOT visible');
      await takeScreenshot(popup, 'dbs-heading-assertion-failure');
      throw new Error(`Heading with text 'DBS digiWealth' was not found or not visible in the preview. ${error}`);
    }

    console.log('TEST COMPLETED SUCCESSFULLY: All assertions passed');

  } catch (error) {
    console.error('TEST FAILED with exception:', error);
    if (popup) {
      await takeScreenshot(popup, 'test-exception-failure');
    }
    throw error;
  }
});

import { test, expect } from '@playwright/test';

test('load sample email and verify promotion element exists in preview', async ({ page }) => {
  // Navigate to the main page
  await page.goto('http://localhost:8080/');

  // Click the "Load Sample" button to populate the form
  await page.getByRole('button', { name: 'Load Sample' }).click();

  // Set up listener for the popup window that will open
  const page1Promise = page.waitForEvent('popup');

  // Click "Preview Email" which opens preview in new tab
  await page.getByRole('button', { name: 'Preview Email' }).click();

  // Get the popup window
  const page1 = await page1Promise;

  // Wait for the popup to load completely
  await page1.waitForLoadState('networkidle');

  // Check for the promotion image
  const promotionImage = page1.getByRole('img', { name: 'Promotion' });
  await expect(promotionImage).toBeVisible();

  // Check for the DBS digiWealth heading
  const dbsHeading = page1.getByRole('heading', { name: 'DBS digiWealth' });
  await expect(dbsHeading).toBeVisible();
});

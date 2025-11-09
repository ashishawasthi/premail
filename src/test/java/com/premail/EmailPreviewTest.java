package com.premail;

import com.microsoft.playwright.*;
import com.microsoft.playwright.options.AriaRole;
import com.microsoft.playwright.options.LoadState;
import org.junit.jupiter.api.*;

import java.nio.file.Paths;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.logging.Logger;
import java.util.logging.Level;

import static com.microsoft.playwright.assertions.PlaywrightAssertions.assertThat;

public class EmailPreviewTest {

    private static final Logger logger = Logger.getLogger(EmailPreviewTest.class.getName());

    // Shared between all tests in this class.
    static Playwright playwright;
    static Browser browser;

    // New instance for each test method.
    BrowserContext context;
    Page page;

    @BeforeAll
    static void launchBrowser() {
        logger.info("Initializing Playwright and launching browser");
        playwright = Playwright.create();
        browser = playwright.chromium().launch(new BrowserType.LaunchOptions()
            .setHeadless(true));
        logger.info("Browser launched successfully");
    }

    @AfterAll
    static void closeBrowser() {
        logger.info("Closing browser and Playwright");
        playwright.close();
    }

    @BeforeEach
    void createContextAndPage() {
        logger.info("Creating new browser context and page");
        context = browser.newContext();
        page = context.newPage();
    }

    @AfterEach
    void closeContext() {
        logger.info("Closing browser context");
        context.close();
    }

    @Test
    void testLoadSampleEmailAndVerifyPromotionElementsExist() {
        Page popup = null;

        try {
            logger.info("TEST STARTED: Load sample email and verify promotion elements");

            // Navigate to the main page
            logger.info("Step 1: Navigating to http://localhost:8080/");
            page.navigate("http://localhost:8080/");
            logger.info("Successfully navigated to main page");

            // Click the "Load Sample" button to populate the form
            logger.info("Step 2: Clicking 'Load Sample' button");
            page.getByRole(AriaRole.BUTTON, new Page.GetByRoleOptions().setName("Load Sample"))
                .click();
            logger.info("Successfully clicked 'Load Sample' button");

            // Set up listener for the popup window that will open
            logger.info("Step 3: Waiting for popup window to open");
            popup = page.waitForPopup(() -> {
                // Click "Preview Email" which opens preview in new tab
                logger.info("Step 3a: Clicking 'Preview Email' button");
                page.getByRole(AriaRole.BUTTON, new Page.GetByRoleOptions().setName("Preview Email"))
                    .click();
            });
            logger.info("Popup window opened successfully");

            // Wait for the popup to load completely
            logger.info("Step 4: Waiting for popup to load completely");
            popup.waitForLoadState(LoadState.NETWORKIDLE);
            logger.info("Popup loaded successfully (network idle)");

            // Check for the promotion image
            logger.info("Step 5: Verifying promotion image is visible");
            Locator promotionImage = popup.getByRole(AriaRole.IMG,
                new Page.GetByRoleOptions().setName("Promotion"));

            try {
                assertThat(promotionImage).isVisible();
                logger.info("✓ ASSERTION PASSED: Promotion image is visible");
            } catch (AssertionError e) {
                logger.severe("✗ ASSERTION FAILED: Promotion image is NOT visible");
                takeScreenshot(popup, "promotion-image-assertion-failure");
                throw new AssertionError("Promotion image with alt text 'Promotion' was not found or not visible in the preview", e);
            }

            // Check for the DBS digiWealth heading
            logger.info("Step 6: Verifying DBS digiWealth heading is visible");
            Locator dbsHeading = popup.getByRole(AriaRole.HEADING,
                new Page.GetByRoleOptions().setName("DBS digiWealth"));

            try {
                assertThat(dbsHeading).isVisible();
                logger.info("✓ ASSERTION PASSED: DBS digiWealth heading is visible");
            } catch (AssertionError e) {
                logger.severe("✗ ASSERTION FAILED: DBS digiWealth heading is NOT visible");
                takeScreenshot(popup, "dbs-heading-assertion-failure");
                throw new AssertionError("Heading with text 'DBS digiWealth' was not found or not visible in the preview", e);
            }

            logger.info("TEST COMPLETED SUCCESSFULLY: All assertions passed");

        } catch (Exception e) {
            logger.log(Level.SEVERE, "TEST FAILED with exception: " + e.getMessage(), e);
            if (popup != null) {
                takeScreenshot(popup, "test-exception-failure");
            }
            throw e;
        }
    }

    /**
     * Takes a screenshot and saves it with a timestamp
     */
    private void takeScreenshot(Page page, String name) {
        try {
            String timestamp = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyyMMdd_HHmmss"));
            String filename = String.format("screenshot_%s_%s.png", name, timestamp);
            String path = Paths.get("target", "screenshots", filename).toString();

            // Create screenshots directory if it doesn't exist
            Paths.get("target", "screenshots").toFile().mkdirs();

            page.screenshot(new Page.ScreenshotOptions().setPath(Paths.get(path)));
            logger.warning("Screenshot saved: " + path);
            System.err.println("⚠️  SCREENSHOT SAVED: " + path);
        } catch (Exception e) {
            logger.log(Level.WARNING, "Failed to take screenshot", e);
        }
    }
}

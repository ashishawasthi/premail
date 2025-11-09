package com.premail;

import com.microsoft.playwright.*;
import com.microsoft.playwright.options.AriaRole;
import org.junit.jupiter.api.*;

import static com.microsoft.playwright.assertions.PlaywrightAssertions.assertThat;

public class EmailPreviewTest {

    // Shared between all tests in this class.
    static Playwright playwright;
    static Browser browser;

    // New instance for each test method.
    BrowserContext context;
    Page page;

    @BeforeAll
    static void launchBrowser() {
        playwright = Playwright.create();
        browser = playwright.chromium().launch(new BrowserType.LaunchOptions()
            .setHeadless(true));
    }

    @AfterAll
    static void closeBrowser() {
        playwright.close();
    }

    @BeforeEach
    void createContextAndPage() {
        context = browser.newContext();
        page = context.newPage();
    }

    @AfterEach
    void closeContext() {
        context.close();
    }

    @Test
    void testLoadSampleEmailAndVerifyPromotionElementsExist() {
        // Navigate to the main page
        page.navigate("http://localhost:8080/");

        // Click the "Load Sample" button to populate the form
        page.getByRole(AriaRole.BUTTON, new Page.GetByRoleOptions().setName("Load Sample"))
            .click();

        // Set up listener for the popup window that will open
        Page popup = page.waitForPopup(() -> {
            // Click "Preview Email" which opens preview in new tab
            page.getByRole(AriaRole.BUTTON, new Page.GetByRoleOptions().setName("Preview Email"))
                .click();
        });

        // Wait for the popup to load completely
        popup.waitForLoadState(LoadState.NETWORKIDLE);

        // Check for the promotion image
        Locator promotionImage = popup.getByRole(AriaRole.IMG,
            new Page.GetByRoleOptions().setName("Promotion"));
        assertThat(promotionImage).isVisible();

        // Check for the DBS digiWealth heading
        Locator dbsHeading = popup.getByRole(AriaRole.HEADING,
            new Page.GetByRoleOptions().setName("DBS digiWealth"));
        assertThat(dbsHeading).isVisible();
    }
}

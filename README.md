# Automated Web Content Capture and PDF Generation Tool

**For Educational Use Only**

This project provides a set of tools to automate the process of capturing web content, specifically from websites that display paginated content, and converting that content into a single, organized PDF document. The project is designed for educational purposes, to explore web automation, image processing, and PDF creation techniques.

## Technical Overview

The tool leverages several key technologies and concepts:

1.  **Web Automation with Selenium:**
    *   Uses the Selenium WebDriver to control a Chrome browser in headless mode (no GUI).
    *   Automates actions like navigating to specific URLs, logging in with credentials, clicking elements (buttons, links), and executing JavaScript.
    *   Implements custom resolution setting using Chrome DevTools Protocol (CDP) for high-resolution screenshots.
    *   Handles dynamic content loading and waits using explicit delays.
    *   Navigates through pages of content via simulated button clicks.
    *   Detects the end of the content by comparing screenshots.

2.  **Image Processing with Pillow (PIL):**
    *   Captures screenshots of web pages.
    *   Crops images to remove unwanted elements (navigation bars, headers, etc.) using predefined coordinates.
    *   Splits full-page screenshots into individual page images (left and right halves) for books or documents that display two pages at a time.
    *   Offers optional image compression (resizing and JPEG conversion with quality control) to reduce PDF file size.
    *    Uses multithreading to speed up the image cropping process.

3.  **PDF Generation:**
    *   Combines processed images into a single PDF document using Pillow.
    *   Handles image ordering to ensure correct page sequence in the final PDF.

4.  **File Management:**
    *   Organizes screenshots and cropped images into designated directories.
    *   Implements a robust file sorting mechanism to maintain page order based on embedded indices in filenames.
    *   Clears screenshot directories before each run to avoid conflicts.
    *   Provides functions for getting a sorted list of files and loading them by index.

5.  **Utilities:**
    *   `login.py`:  Handles website authentication (username/password login).  Abstracted to keep credentials separate from main logic.
    *   `pause.py`:  Implements a custom countdown timer with dynamic console output for user feedback during delays.
    *   `files_management.py`: Provides utility functions to manage files, get sorted file lists, and handle loading images in order.
    *   `crop_images.py`:  Contains the core image cropping and splitting logic.

6.  **Project Structure:**
    *   Well-organized directory structure for code, screenshots, and recordings.
    *   Uses a `requirements.txt` file for easy dependency management (Selenium, Pillow, python-dotenv).
    *   Employs a modular design with separate files for different functionalities (main script, utility functions, PDF creation).

7. **Chrome Recordings:**
    *   Includes sample Chrome recordings (JSON files) demonstrating user interactions on the target website. These can be used for analysis or to potentially adapt the script to different interaction patterns.

## How it Works (Simplified)

1.  The `main.py` script initializes a headless Chrome browser and logs into a website using provided credentials.
2.  It navigates to the desired content (e.g., an online book).
3.  It iterates through the pages of the content:
    *   Takes a high-resolution screenshot.
    *   Clicks the "next page" button.
    *   Compares the current screenshot with the previous one to detect the end of the content.
4.  The `create_pdf.py` script:
    *   Loads the screenshots.
    *   Uses `crop_images.py` to crop and split the images.
    *    Creates cropped images and saved them in the `crop` directory.
    *   Combines the cropped images into a PDF file.

## Key Implemented Features

*   **Headless Browsing:**  Runs without a visible browser window, making it suitable for server-side execution.
*   **Dynamic Resolution:**  Sets a high resolution for screenshots, enhancing quality.
*   **Automated Navigation:**  Simulates user clicks to navigate through paginated content.
*   **Screenshot Comparison:**  Detects the end of content by comparing consecutive screenshots.
*   **Image Cropping and Splitting:**  Precisely extracts the relevant content from screenshots.
*   **PDF Compilation:**  Combines processed images into a final PDF.
*   **Modular Design:**  Separates concerns into distinct modules for better organization and maintainability.
*   **Multithreading:** Speeds up image processing by using multiple threads.
*   **Error Handling:** Basic error handling.

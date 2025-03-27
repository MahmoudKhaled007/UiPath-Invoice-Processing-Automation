
#  UiPath Invoice Automation

## Overview

This project automates the extraction, processing, and management of vendor invoices from an online portal using UiPath RPA. The bot logs in, retrieves data, processes invoices, and generates a final report, ensuring efficiency and accuracy in invoice handling.

## Features

- Automated Login: Securely logs in to the ACME portal using stored credentials.

- Excel Data Processing: Reads vendor data and prepares it for processing.

- Queue Management: Uses UiPath Orchestrator to handle multiple vendors efficiently.

- Automated Invoice Downloads: Retrieves monthly invoices based on vendor details.

- Data Extraction & Processing: Extracts information using RegEx and calculates invoice totals.

- Cloud Storage Integration: Uploads final reports to Google Drive.

- Email Notification: Sends automated emails with report attachments upon completion.

## Technologies Used

- UiPath Studio & Orchestrator

- Microsoft Excel

- Google Drive API

- Email Automation

## Workflow Structure

- Main.xaml
- ACMEELogIn.xaml
- ExtractDataFromExcel.xaml
- QueueDispatcher.xaml
- NavigateToInternalInvoices.xaml
- QueuePerformer.xaml
- DownloadMonthlyInvoices.xaml
- ExtractAndFillDataVendorSheet.xaml
- UploadToGoogleDrive.xaml
- OutputEmail.xaml

## Process Flow

**1️⃣ Login & Authentication:**
 Logs into https://acme-test.uipath.com/login with retry logic.

**2️⃣ Read Vendor Data:** Extracts vendor names and prepares input for processing.

**3️⃣ Queue Dispatching:** Uploads vendors to Orchestrator for sequential handling.

**4️⃣ Invoice Retrieval:** Navigates to Internal Invoices tab and downloads required files.

**5️⃣ Data Extraction & Processing:** Reads, extracts, and calculates invoice totals.

**6️⃣ Final Report Storage:** Uploads results to Google Drive.

**7️⃣ Completion Notification:** Sends email confirmation with report attachment.


## Exception Handling

- Login Failure: Retries up to 3 times before logging an error.

- Invalid Vendor Data: Skips and flags missing or incorrect vendor data.

- Download Issues: Retries before marking an error.

- Processing Errors: Logs exceptions for further review.

## Contributing
Contributions to enhance the functionality or performance of the application are welcome. Please fork the repository and submit a pull request with your proposed changes.

## License
This project is licensed under the Apache-2.0 License. See the LICENSE file for more details.

📬 Contact

For inquiries, feel free to connect via GitHub or Upwork.

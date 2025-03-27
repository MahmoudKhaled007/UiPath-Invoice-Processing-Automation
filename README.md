
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

## Demo
- [Watch the RPA Invoice Processing Demo](https://www.youtube.com/watch?v=-8cm1Nrzdwk)
  
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
- 
## Installation

Make sure your system fulfills the requirements for UiPath software as outlined in the official [UiPath documentation](https://docs.uipath.com).

### UiPath Tools Required

- **UiPath Studio**
- **UiPath Assistant**
- **UiPath Automation Cloud** (optional for deployment)

### Steps for UiPath Studio Installation:

1. Download and install UiPath Studio from [here](https://www.uipath.com/start-trial).
2. Follow the instructions in the [UiPath Studio Documentation](https://docs.uipath.com/studio/docs).

### How to Connect to UiPath Automation Cloud:

1. Sign in to your UiPath Automation Cloud account.
2. Link your local machine to the cloud for workflow deployment.

---
## Usage

To execute the RPA workflow locally, follow these steps:

1. Download or clone this repository.
2. Open **UiPath Studio**.
3. Open the `Main.xaml` file from the downloaded repository.
4. Click **Run** to initiate the automation.

---

## Acknowledgements

A big thank you to the UiPath community for providing resources, tutorials, and a collaborative platform for learning and growing in the field of RPA.

## License
This project is licensed under the Apache-2.0 License. See the LICENSE file for more details.

📬 Contact

For inquiries, feel free to connect via GitHub or Upwork.

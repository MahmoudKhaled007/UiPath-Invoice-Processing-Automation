import requests


def ApiCall(filePath):
    # Replace these values with your own
    client_id = "cc38761d-192e-43c6-9419-8bc0bc2cb8ae"
    client_secret = "35e810d4-886b-4bff-aa26-39c72cfa7243"
    tenant_id = "9aa99673-73ba-430c-acea-ba1c00766af0"
    token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

    # Construct the request body
    token_payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "Files.ReadWrite User.Read",
    }

    # Obtain the access token
    token_response = requests.post(token_url, data=token_payload)
    access_token = token_response.json()["access_token"]

    # Specify the file path and the destination path on OneDrive
    file_path = filePath
    destination_path = "/drive/root:/Documents/VendorInvoicesData.xlsx:/content"

    # Upload the file
    upload_url = f"https://graph.microsoft.com/v1.0/me/drive/root:{destination_path}"
    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/octet-stream",
    }

    with open(file_path, "rb") as file:
        file_contents = file.read()
        response = requests.put(upload_url, headers=headers, data=file_contents)

    return response.status_code

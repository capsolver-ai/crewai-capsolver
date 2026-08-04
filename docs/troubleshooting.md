# Troubleshooting

## Missing API key
Set CAPSOLVER_API_KEY in the process environment. Never place it in source.

## Browser unavailable
Install the browser extra and Chromium. Token mode does not require a browser.

## Timeout or rate limit
Use bounded backoff for transient failures and confirm balance and service status.

## Tool not selected
Confirm registration, tool descriptions, and exact schema argument names.

## Reporting
Use a redacted reproduction. Never attach credentials, cookies, tokens, proxies, private pages, or personal data.

# Python - Network #0

This project covers how the web works: URLs, HTTP requests and responses,
headers, methods, status codes and cookies, using `curl`.

| File | Description |
|------|-------------|
| 0-body_size.sh | Displays the size in bytes of the body of a response |
| 1-body.sh | Displays the body of a response only if the status is 200 |
| 2-delete.sh | Sends a DELETE request and displays the body |
| 3-methods.sh | Displays the HTTP methods a server accepts |
| 4-header.sh | Sends a request with a custom header |
| 5-post_params.sh | Sends a POST request with form parameters |

Usage example:

    ./0-body_size.sh 0.0.0.0:5000

## Requirements
- Ubuntu 20.04 LTS
- Bash scripts of exactly 3 lines, all `curl` commands use `-s`

# M3U8 Validator

A simple Python script to validate M3U8 links, typically used for live streaming or on-demand playlists in HLS (HTTP Live Streaming). This tool helps check if a given URL is a valid M3U8 file, optionally ensuring it uses HTTPS.

## Features

- **URL Validation**: Checks if a given link is a valid HTTP/HTTPS URL.
- **HTTPS Enforcement**: Allows enforcing HTTPS if required.
- **M3U8 Format Check**: Validates that the URL content starts with the expected `#EXTM3U` identifier, as per the M3U8 format.
- **Timeout Control**: Customizable request timeout for better control over network performance.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/dastgerdidev/m3u8-validator.git

## Usage

The `is_valid_m3u8()` function checks if a provided link is a valid M3U8 file.

  ```python
  from validator import is_valid_m3u8
  
  link = "http://example.com/playlist.m3u8"
  is_secure = True
  timeout = 5
  
  if is_valid_m3u8(link, timeout=timeout, secure=is_secure):
      print("The link is a valid M3U8 file.")
  else:
      print("The link is not a valid M3U8 file.")
  ```

### Parameters

- **link (str)**: The URL to validate.
- **timeout (int)**: Optional. Timeout for the request in seconds (default: 5).
- **secure (bool)**: Optional. Enforces HTTPS if set to `True` (default: `False`).

## Requirements

- Python 3.6+

## Contributing

Contributions are welcome! Feel free to open an issue or create a pull request with improvements, bug fixes, or additional features.

## License

This project is open-source and available under the MIT License.

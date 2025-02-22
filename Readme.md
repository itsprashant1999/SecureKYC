# Secure KYC

This repository includes a script for secure KYC using OpenCV, Tesseract-OCR, and dlib.

## Requirements

- Docker

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. Build the Docker image:
    ```sh
    docker build -t securekyc .
    ```

3. Run the Docker container:
    ```sh
    docker run -it --rm --device /dev/video0 securekyc
    ```

   Adjust the device path as needed to match your webcam device.

## Notes

- Ensure that Docker is installed on your system.
- The Docker container includes Tesseract-OCR and other required dependencies.

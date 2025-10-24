# PDF Merger Tool 
Desktop app to merge multiple PDFs into one single PDF, with option to reorder the files.
Files will be ordered according to top-down.

## Table of contents
- [About](#about)
- [Features](#features)
- [Tech stack](#tech-stack)
- [Getting started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Local development](#local-development)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## About
This is a quick Python app using Python, PyQt, and PyPDF to support merging PDF files on desktop into one singular PDF file. It was built out of frustration of having paid for online service and with long-term personal use in mind.

## Feature
- Supports click and/ or drag-and-drop selection of files.
- Simple, clean layout for convenience and quick usage.

## Tech stack
- Python
- PyQt5
- PyPDF2

## Getting started

### Prerequisites
- Virtual environment venv

### Local development
1. Clone the repo
   ```bash
   git clone https://github.com/tramanhvong/dinosaur_amplify.git
   cd dinosaur_amplify
   ```
2. Create venv
   ```bash
   python -m venv venv
   venv/Scripts/activate
   ```
3. Install dependencies
   ```
   pip install -r requirements.txt
   ```
4. Run app locally
   ```
   python pdf_merger.py
   ```
## Deployment
This project is yet to be deployed.

## Contributing
Contributions are welcome — open an issue or submit a pull request. Keep changes focused and add notes in the PR about what you changed and why.

## License
This project is licensed under the MIT-0 License. See the LICENSE file for details.

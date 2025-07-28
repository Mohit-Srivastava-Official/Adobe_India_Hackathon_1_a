# Adobe India Hackathon 2025 – Connecting the Dots

## Overview
This project is for the Adobe India Hackathon 2025, "Connecting the Dots" challenge. It extracts structured outlines (Title, H1, H2, H3 with page numbers) from PDFs and outputs them as JSON, ready for further document intelligence tasks.

## Approach
- Uses `pdfminer.six` and `PyMuPDF` for robust PDF parsing.
- Heuristics and layout analysis for heading detection (not just font size).
- Modular code, ready for extension in Round 1B.

## How to Build and Run
1. Place your PDFs in the `input/` directory.
2. Build the Docker image:
   ```
   docker build --platform linux/amd64 -t mysolutionname:somerandomidentifier .
   ```
3. Run the container:
   ```
   docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none mysolutionname:somerandomidentifier
   ```
4. Output JSONs will appear in the `output/` directory.

## Dependencies
- Python 3.9+
- pdfminer.six
- PyMuPDF

## Notes
- No internet access required at runtime.
- Model size and runtime constraints are respected.

---

## For Round 1B
The code is modular and will be extended for persona-driven document intelligence in the next round.

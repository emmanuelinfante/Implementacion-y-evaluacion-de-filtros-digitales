# Implementación y evaluación de filtros digitales

This project implements and evaluates various digital filters (Low-pass, High-pass, Band-pass) using Python. It explores both FIR (Finite Impulse Response) and IIR (Infinite Impulse Response) techniques.

## Structure
- `src/`: Source code modules.
  - `signal_gen.py`: Signal generation logic.
  - `filters.py`: FIR and IIR filter implementations.
  - `visualization.py`: Plotting utilities.
- `main.py`: Entry point for running the evaluation.
- `results/`: Directory containing generated plots (created after running `main.py`).
- `report.md`: Detailed evaluation report.
- `requirements.txt`: Python dependencies.

## Installation
Ensure you have Python 3 installed. It is recommended to use a virtual environment.

```bash
pip install -r requirements.txt
```

## Usage
Run the main script to generate signals, apply filters, and save visualizations:

```bash
python main.py
```

## Features
- Synthetic signal generation with multiple frequencies and noise.
- FIR filter design using the windowing method.
- IIR filter design using Butterworth and SOS (Second-Order Sections).
- Visualization of signals in time and frequency (PSD) domains.
- Frequency response analysis of designed filters.

# Report: Implementation and Evaluation of Digital Filters

## Introduction
This report evaluates the performance of Finite Impulse Response (FIR) and Infinite Impulse Response (IIR) digital filters. We implemented Low-pass, High-pass, and Band-pass filters and applied them to a synthetic signal containing multiple frequencies and additive Gaussian noise.

## Methodology
### Signal Generation
A composite signal was generated with the following components:
- Frequencies: 10 Hz, 50 Hz, and 150 Hz.
- Sampling Frequency ($f_s$): 1000 Hz.
- Duration: 1 second.
- Noise: Gaussian white noise with $\sigma = 0.5$.

### Filter Design
1. **FIR Filters**:
   - Method: Windowing (Hamming window).
   - Order (numtaps): 101.
   - Types: Low-pass (30 Hz), High-pass (100 Hz), Band-pass (40-60 Hz).

2. **IIR Filters**:
   - Method: Butterworth (4th order).
   - Implementation: Second-Order Sections (SOS) for numerical stability.
   - Types: Low-pass (30 Hz), High-pass (100 Hz), Band-pass (40-60 Hz).

## Results and Discussion
The results are saved in the `results/` directory.

### 1. Low-pass Filter (LPF)
- **Goal**: Retain the 10 Hz component and suppress 50 Hz, 150 Hz, and high-frequency noise.
- **Observations**: 
  - Both FIR and IIR successfully isolated the 10 Hz signal.
  - FIR filters show a slight delay in the time domain due to their linear phase property (constant group delay).
  - IIR filters provide a sharper transition band for the same computational cost but may introduce phase distortion.

### 2. High-pass Filter (HPF)
- **Goal**: Retain the 150 Hz component and suppress 10 Hz, 50 Hz, and low-frequency noise.
- **Observations**:
  - Successfully attenuated components below 100 Hz.
  - High-frequency noise remains in the pass-band as expected.

### 3. Band-pass Filter (BPF)
- **Goal**: Retain the 50 Hz component.
- **Observations**:
  - The BPF effectively isolated the 50 Hz tone, removing both the 10 Hz and 150 Hz components.

## Comparison: FIR vs. IIR
| Feature | FIR (Window Method) | IIR (Butterworth) |
|---------|---------------------|-------------------|
| Stability | Always stable | Can be unstable (fixed with SOS) |
| Phase | Linear (no distortion) | Non-linear (phase distortion) |
| Efficiency | Lower (requires many taps) | Higher (lower order needed) |
| Design | Easy to design | More complex design |

## Conclusion
Digital filters are essential for signal cleaning and feature extraction. While FIR filters offer linear phase and stability, IIR filters are more computationally efficient for achieving sharp transitions. For most audio or general signal processing where phase is critical, FIR is preferred. If resource constraints are high, IIR is a better choice.

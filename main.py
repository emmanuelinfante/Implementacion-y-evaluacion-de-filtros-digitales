import numpy as np
import os
import matplotlib.pyplot as plt
from src.signal_gen import generate_signal
from src.filters import apply_fir_filter, apply_iir_filter
from src.visualization import plot_signals, plot_psd, plot_frequency_response

def main():
    # Parameters
    fs = 1000  # Sampling frequency
    duration = 1.0  # Duration in seconds
    freqs = [10, 50, 150]  # Frequencies in the signal
    noise_std = 0.5
    
    # Create results directory
    os.makedirs('results', exist_ok=True)
    
    # 1. Generate Signal
    t, original_signal = generate_signal(fs, duration, freqs, noise_std)
    
    # 2. Low-pass Filtering (Cutoff at 30 Hz to keep 10 Hz)
    lp_cutoff = 30
    fir_lp, fir_lp_b = apply_fir_filter(original_signal, lp_cutoff, fs, 'lowpass', numtaps=101)
    iir_lp, iir_lp_sos = apply_iir_filter(original_signal, lp_cutoff, fs, 'lowpass', order=4)
    
    # 3. High-pass Filtering (Cutoff at 100 Hz to keep 150 Hz)
    hp_cutoff = 100
    fir_hp, fir_hp_b = apply_fir_filter(original_signal, hp_cutoff, fs, 'highpass', numtaps=101)
    iir_hp, iir_hp_sos = apply_iir_filter(original_signal, hp_cutoff, fs, 'highpass', order=4)
    
    # 4. Band-pass Filtering (Cutoff at [40, 60] Hz to keep 50 Hz)
    bp_cutoff = [40, 60]
    fir_bp, fir_bp_b = apply_fir_filter(original_signal, bp_cutoff, fs, 'bandpass', numtaps=101)
    iir_bp, iir_bp_sos = apply_iir_filter(original_signal, bp_cutoff, fs, 'bandpass', order=4)
    
    # --- Visualizations ---
    
    # Time Domain Comparison
    plot_signals(t, [original_signal, fir_lp, iir_lp], 
                 ['Original + Noise', 'FIR Low-pass', 'IIR Low-pass'],
                 'Low-pass Filter Comparison (Time Domain)')
    plt.savefig('results/lowpass_time.png')
    
    # PSD Comparison
    plot_psd([original_signal, fir_lp, iir_lp], 
             ['Original + Noise', 'FIR Low-pass', 'IIR Low-pass'], 
             fs, 'Low-pass Filter Comparison (PSD)')
    plt.savefig('results/lowpass_psd.png')
    
    # High-pass PSD
    plot_psd([original_signal, fir_hp, iir_hp], 
             ['Original + Noise', 'FIR High-pass', 'IIR High-pass'], 
             fs, 'High-pass Filter Comparison (PSD)')
    plt.savefig('results/highpass_psd.png')

    # Band-pass PSD
    plot_psd([original_signal, fir_bp, iir_bp], 
             ['Original + Noise', 'FIR Band-pass', 'IIR Band-pass'], 
             fs, 'Band-pass Filter Comparison (PSD)')
    plt.savefig('results/bandpass_psd.png')
    
    # Frequency Response Comparison
    plot_frequency_response(fir_lp_b, fs, is_sos=False, title='FIR Low-pass Frequency Response')
    plt.savefig('results/fir_lp_freq_response.png')
    
    plot_frequency_response(iir_lp_sos, fs, is_sos=True, title='IIR Low-pass Frequency Response')
    plt.savefig('results/iir_lp_freq_response.png')

    print("Filtering complete. Results saved in 'results/' directory.")

if __name__ == "__main__":
    main()

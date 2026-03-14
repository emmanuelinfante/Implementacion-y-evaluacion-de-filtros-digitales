import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

def plot_signals(t, signals, labels, title='Time-Domain Signals'):
    """
    Plot time-domain signals.

    Args:
        t (np.ndarray): Time vector.
        signals (list of np.ndarray): List of signals to plot.
        labels (list of str): Labels for each signal.
        title (str): Title of the plot.
    """
    plt.figure(figsize=(10, 6))
    for sig, label in zip(signals, labels):
        plt.plot(t, sig, label=label)
    plt.title(title)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

def plot_psd(signals, labels, fs, title='Power Spectral Density (PSD)'):
    """
    Plot Power Spectral Density of signals.

    Args:
        signals (list of np.ndarray): List of signals to plot.
        labels (list of str): Labels for each signal.
        fs (float): Sampling frequency in Hz.
        title (str): Title of the plot.
    """
    plt.figure(figsize=(10, 6))
    for sig, label in zip(signals, labels):
        f, Pxx_den = signal.welch(sig, fs, nperseg=1024)
        plt.semilogy(f, Pxx_den, label=label)
    plt.title(title)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('PSD (V^2/Hz)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

def plot_frequency_response(b_or_sos, fs, is_sos=False, title='Frequency Response'):
    """
    Plot the frequency response of a filter.

    Args:
        b_or_sos (np.ndarray): Filter coefficients or SOS.
        fs (float): Sampling frequency in Hz.
        is_sos (bool): True if b_or_sos is SOS, False if it's FIR coefficients (b).
        title (str): Title of the plot.
    """
    if is_sos:
        w, h = signal.sosfreqz(b_or_sos, worN=8000, fs=fs)
    else:
        w, h = signal.freqz(b_or_sos, worN=8000, fs=fs)
    
    plt.figure(figsize=(10, 6))
    plt.plot(w, 20 * np.log10(np.abs(h)))
    plt.title(title)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude (dB)')
    plt.grid(True)
    plt.tight_layout()

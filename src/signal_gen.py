import numpy as np

def generate_signal(fs, duration, freqs, noise_std=0.1):
    """
    Generate a composite signal with multiple frequencies and Gaussian white noise.

    Args:
        fs (float): Sampling frequency in Hz.
        duration (float): Duration of the signal in seconds.
        freqs (list of float): List of frequencies to include in the signal.
        noise_std (float): Standard deviation of the Gaussian white noise.

    Returns:
        t (np.ndarray): Time vector.
        signal (np.ndarray): Generated composite signal.
    """
    t = np.arange(0, duration, 1/fs)
    signal = np.zeros_like(t)
    
    for f in freqs:
        signal += np.sin(2 * np.pi * f * t)
        
    noise = np.random.normal(0, noise_std, size=t.shape)
    signal += noise
    
    return t, signal

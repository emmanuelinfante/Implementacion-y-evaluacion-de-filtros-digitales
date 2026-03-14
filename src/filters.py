from scipy import signal
import numpy as np

def apply_fir_filter(data, cutoff, fs, filter_type='lowpass', numtaps=101, window='hamming'):
    """
    Apply an FIR filter using the windowing method.

    Args:
        data (np.ndarray): The input signal.
        cutoff (float or list of float): Cutoff frequency(ies) in Hz.
        fs (float): Sampling frequency in Hz.
        filter_type (str): Type of filter: 'lowpass', 'highpass', 'bandpass'.
        numtaps (int): Number of filter coefficients.
        window (str): Window type for firwin.

    Returns:
        filtered_data (np.ndarray): The filtered signal.
        b (np.ndarray): The filter coefficients.
    """
    nyq = 0.5 * fs
    
    # Normalize cutoff frequencies
    if isinstance(cutoff, list):
        normalized_cutoff = [c / nyq for c in cutoff]
    else:
        normalized_cutoff = cutoff / nyq

    b = signal.firwin(numtaps, normalized_cutoff, window=window, pass_zero=(filter_type == 'lowpass'))
    filtered_data = signal.lfilter(b, 1.0, data)
    
    return filtered_data, b

def apply_iir_filter(data, cutoff, fs, filter_type='lowpass', order=4, btype='butter'):
    """
    Apply an IIR filter using Butterworth design and Second-Order Sections (SOS).

    Args:
        data (np.ndarray): The input signal.
        cutoff (float or list of float): Cutoff frequency(ies) in Hz.
        fs (float): Sampling frequency in Hz.
        filter_type (str): Type of filter: 'lowpass', 'highpass', 'bandpass', 'bandstop'.
        order (int): Order of the filter.
        btype (str): Filter design type: 'butter' or 'cheby1'.

    Returns:
        filtered_data (np.ndarray): The filtered signal.
        sos (np.ndarray): Second-order sections.
    """
    nyq = 0.5 * fs
    
    # Translate filter_type to scipy btype
    scipy_btype = filter_type
    if filter_type == 'lowpass':
        scipy_btype = 'low'
    elif filter_type == 'highpass':
        scipy_btype = 'high'
    elif filter_type == 'bandpass':
        scipy_btype = 'band'

    if isinstance(cutoff, list):
        normalized_cutoff = [c / nyq for c in cutoff]
    else:
        normalized_cutoff = cutoff / nyq

    if btype == 'butter':
        sos = signal.butter(order, normalized_cutoff, btype=scipy_btype, output='sos')
    elif btype == 'cheby1':
        sos = signal.cheby1(order, 0.5, normalized_cutoff, btype=scipy_btype, output='sos')
    else:
        raise ValueError("Unsupported IIR filter type.")

    filtered_data = signal.sosfilt(sos, data)
    
    return filtered_data, sos

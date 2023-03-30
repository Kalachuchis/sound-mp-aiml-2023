import librosa
import librosa.display
import matplotlib
import numpy as np
import tkinter as tk
matplotlib.use('TkAgg')

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backend_bases import key_press_handler

from matplotlib.figure import Figure



def plot(filename='./input/voice_recording.wav'):
    

    sampling_rate = 22050
    audio, sr = librosa.load(filename,sr=sampling_rate, mono=False)
    # Apply STFT
    n_fft = 2048
    hop_length = 512

    # Compute the spectrogram
    NFFT = 1024
    spectrogram, freqs, times, _ = plt.specgram(audio, NFFT=NFFT, Fs=sampling_rate)

    # Create a Matplotlib figure
    fig = plt.Figure(figsize=(8,6), dpi=100)
    ax = fig.add_subplot(111)

    # Plot the spectrogram on the figure
    ax.specgram(audio, NFFT=NFFT, Fs=sampling_rate, cmap='viridis')

    # Create a Tkinter canvas and display the figure on it
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # # Add a Matplotlib navigation toolbar to the window
    # toolbar = NavigationToolbar2Tk(canvas, root)
    # toolbar.update()
    # canvas.get_tk_widget().pack(side=window.TOP, fill=window.BOTH, expand=1)







    # canvas = FigureCanvasTkAgg(fig, master = window)

    # canvas.draw()


    # pass
if __name__ =="__main__":
    # the main Tkinter window
    window = tk.Tk()
    
    # setting the title 
    window.title('Plotting in Tkinter')
    
    # dimensions of the main window
    window.geometry("500x500")
    
    # button that displays the plot
    plot_button = tk.Button(master = window, 
                        command = plot,
                        height = 2, 
                        width = 10,
                        text = "Plot")
    
    # place the button 
    # in main window
    plot_button.pack()
    
    # run the gui
    window.mainloop()
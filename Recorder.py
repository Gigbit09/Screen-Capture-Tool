import cv2
import numpy as np
import tkinter as tk
from tkinter import messagebox
from threading import Thread
import mss  


screen_resolution = (1920, 1080)


video_codec = cv2.VideoWriter_fourcc(*"XVID")


output_filename = "ScreenCapture.avi"


frame_rate = 60.0

class ScreenRecorder:
    def __init__(self, output_filename, screen_resolution, frame_rate):
        self.output_filename = output_filename
        self.screen_resolution = screen_resolution
        self.frame_rate = frame_rate
        self.is_recording = False

    def start_recording(self):
        self.is_recording = True
        num_frames = int(self.frame_rate * 10)  

        video_writer = cv2.VideoWriter(self.output_filename, video_codec, self.frame_rate, self.screen_resolution)

        with mss.mss() as sct:  
            for _ in range(num_frames):
                if not self.is_recording:
                    break

              
                screenshot = sct.grab(sct.monitors[1])  

                
                frame_array = np.array(screenshot)

           
                frame_rgb = cv2.cvtColor(frame_array, cv2.COLOR_BGRA2RGB)

                video_writer.write(frame_rgb)

                

        video_writer.release()

    def stop_recording(self):
        self.is_recording = False


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Screen Capture Tool")
        self.geometry("400x200")
        self.config(bg="#3A3B3C")

        self.recorder = ScreenRecorder(output_filename, screen_resolution, frame_rate)

     
        self.start_button = tk.Button(self, text="Start Recording", command=self.start_recording, bg="green", fg="white", font=('calibri', 14))
        self.start_button.pack(pady=20)

        self.stop_button = tk.Button(self, text="Stop Recording", command=self.stop_recording, bg="red", fg="white", font=('calibri', 14))
        self.stop_button.pack(pady=10)
        self.stop_button.config(state=tk.DISABLED)

        self.status_label = tk.Label(self, text="Status: Ready", bg="#3A3B3C", fg="white", font=('calibri', 12))
        self.status_label.pack(pady=10)

    def start_recording(self):
        self.status_label.config(text="Status: Recording...")
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

      
        self.recording_thread = Thread(target=self.recorder.start_recording)
        self.recording_thread.start()

    def stop_recording(self):
        self.status_label.config(text="Status: Stopping...")
        self.recorder.stop_recording()
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        messagebox.showinfo("Recording Stopped", "Screen recording has been saved.")


if __name__ == "__main__":
    app = App()
    app.mainloop()

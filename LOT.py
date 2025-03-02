import pyttsx3
import customtkinter as ctk
import os
import webbrowser
from tkinter import filedialog
from tkinter import messagebox


class OfflineTTSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LOT")
        self.root.geometry("500x400")

        # Initialize pyttsx3 engine
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')

        self.create_widgets()

    def create_widgets(self):
        # Label
        label = ctk.CTkLabel(self.root, text="Enter text for Audio:", font=("Arial", 20))
        label.pack(pady=20)

        # Text entry field
        self.text_input = ctk.CTkEntry(self.root, width=300, font=("Arial", 14))
        self.text_input.pack(pady=20)

        # Dropdown to choose voice
        def on_voice_change(voice_name):
            voice_index = next((i for i, v in enumerate(self.voices) if v.name == voice_name), None)
            if voice_index is not None:
                self.change_voice(voice_index)

        voice_names = [voice.name for voice in self.voices]
        self.voice_dropdown = ctk.CTkOptionMenu(self.root, values=voice_names, command=on_voice_change)
        if self.voices:
            self.voice_dropdown.set(self.voices[0].name)
        self.voice_dropdown.pack(pady=10)

        # Button to generate speech
        speak_button = ctk.CTkButton(self.root, text="Speak", font=("Arial", 16), command=self.on_speak_button_click)
        speak_button.pack(pady=20)

        # Button to save speech as an audio file
        save_button = ctk.CTkButton(self.root, text="Save Audio", font=("Arial", 16),
                                    command=self.on_save_audio_button_click)
        save_button.pack(pady=20)

        # Button to show missing voices and guide for download
        missing_voices_button = ctk.CTkButton(self.root, text="Missing Voices Guide", font=("Arial", 12),
                                              command=self.on_missing_voices_click)
        missing_voices_button.pack(pady=10)

    def change_voice(self, voice_index):
        try:
            self.engine.setProperty('voice', self.voices[voice_index].id)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to change voice: {e}")

    def save_audio_file(self, text):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".wav",
            filetypes=[("WAV files", "*.wav")],
            title="Save Audio File"
        )
        if not file_path:
            return

        try:
            # Directly save the audio to the specified file path
            self.engine.save_to_file(text, file_path)
            self.engine.runAndWait()  # Ensure the engine processes the save request
            messagebox.showinfo("Success", f"Audio saved to {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save audio: {e}")

    def show_missing_voices(self):
        message = (
            "Available voices for download:\n"
            "1. British English (Microsoft Hazel, Female)\n"
            "2. Australian English (Microsoft Karen, Female)\n"
            "3. Indian English (Microsoft Aruna, Female)\n\n"
            "To download more voices:\n"
            "1. Open Windows Settings > Time & Language > Speech.\n"
            "2. Under 'Manage voices', click 'Add voices'.\n"
            "3. Choose the voices you want and install them.\n"
        )
        messagebox.showinfo("Missing Voices Guide", message)

        if os.name == 'nt':
            try:
                webbrowser.open('ms-settings:speech')
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open Windows settings: {e}")

    def on_speak_button_click(self):
        text = self.text_input.get()
        if text:
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to speak text: {e}")

    def on_save_audio_button_click(self):
        text = self.text_input.get()
        if text:
            self.save_audio_file(text)

    def on_missing_voices_click(self):
        self.show_missing_voices()


if __name__ == "__main__":
    app = ctk.CTk()
    tts_app = OfflineTTSApp(app)
    app.mainloop()

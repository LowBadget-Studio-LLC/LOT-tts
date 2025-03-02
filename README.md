Official repo for LOT tts python app. The installer can be downloaded at the release page of this repo, you can also use pyinsaller library to pack this program:)

downbelow is an AI generated instruction for this code :) because I'm too lazy to write one myself

LOT - Offline Text - to - Speech Application README
1. Application Overview
LOT (Offline Text - to - Speech) is an offline text - to - speech application. It enables users to convert input text into speech and play it. Additionally, it supports saving the speech as a WAV - format audio file. This application uses the pyttsx3 library to implement the text - to - speech function and the customtkinter library to build the Graphical User Interface (GUI). It is simple to operate and has practical functions.
2. Function Features
Text - to - Speech: Users input text in the input box and click the "Speak" button. The application will use the selected speech engine to read the text content.
Voice Selection: A dropdown menu is provided. Users can select different voices from the list of installed voices in the system to read the text, such as British English, Australian English, Indian English, and other voice options (depending on the installed voice packages in the system).
Audio Saving: By clicking the "Save Audio" button, users can save the speech corresponding to the input text as a WAV - format audio file for future use.
Voice Download Guide: When the user clicks the "Missing Voices Guide" button, the application will pop up a message box showing available voice download options and detailed guides for downloading more voices in the Windows system. For Windows users, it also provides the function to directly open the Windows speech settings page, facilitating users to quickly download and manage voices.
3. Installation and Usage
(1) Installation
Ensure Python Environment Installation: Ensure that the Python environment has been installed on your computer. You can download and install the latest version of Python from the official Python website.
Install Dependent Libraries: Open the command - line terminal and run the following command to install the required Python libraries:
bash
pip install pyttsx3 customtkinter
(2) Usage
Run the Application: In the command line, navigate to the directory containing the Python script, and then run the following command to start the application:
bash
python your_script_name.py
Input Text: Enter the text you want to convert into speech in the text input box below "Enter text for Audio:" on the main interface of the application.
Select Voice: Click the voice dropdown menu and select the voice you like from the list.
Play Speech: Click the "Speak" button, and the application will use the selected voice to read the input text.
Save Audio: Click the "Save Audio" button. In the popped - up file save dialog box, select the path to save the audio file, enter the file name (the default extension is.wav), and then click the "Save" button to save the speech as a WAV file.
View Voice Download Guide: Click the "Missing Voices Guide" button to view available voice download information and the operation guide for voice download in the Windows system. If you are using the Windows system, you can also directly open the Windows speech settings page by clicking the link in the message box.
4. Technical Implementation
Text - to - Speech Engine: The pyttsx3 library is used to initialize the speech engine. This library supports multiple voices and can work offline. The list of installed voices in the system is obtained through engine.getProperty('voices'), and the voice to be used is set through the engine.setProperty('voice', voice_id) method.
Graphical User Interface: The GUI is built based on the customtkinter library. This library provides modern and customizable Tkinter components, making the interface more beautiful and easy to use. By creating various CTk components such as CTkLabel, CTkEntry, CTkOptionMenu, and CTkButton, and using the pack layout manager to organize the interface elements.
File Operations: The filedialog module in the tkinter library is used to implement the file save dialog box, allowing users to select the path and file name for saving the audio file. The speech is saved as a file through the engine.save_to_file(text, file_path) method.
Error Handling: try - except blocks are used to catch exceptions in key operations (such as changing voices, saving audio files, opening the Windows settings page, etc.), and the messagebox module is used to display error messages to users, improving the stability and user experience of the application.
5. Notes
Voice Availability: The selectable voices in the application depend on the installed voice packages in the system. If the desired voice is not found, you can download it according to the prompts in the "Missing Voices Guide".
File Save Format: Currently, only WAV format is supported for saving audio. If other formats are required, additional audio conversion tools may be needed.
Compatibility: This application has been mainly tested on the Windows system and may have compatibility issues on other operating systems.
6. Frequently Asked Questions
Why is there no sound after I select a voice?
Ensure that the system volume is not muted and the selected voice is correctly installed in the system. If the problem persists, it may be a configuration issue with the speech engine. You can try reinstalling the pyttsx3 library or checking the system speech settings.
What should I do if there is an error when saving the audio file?
Check whether the save file path is correct and whether you have write permissions. If the path is correct but the error still occurs, it may be that the file format is not supported or there is a problem when the speech engine saves the file. Please check the error message and refer to the above notes.
I can't open the Windows speech settings page. What should I do?
Please ensure that your operating system is Windows and the network connection is normal. If you still can't open it, it may be a system setting or browser problem. You can manually search for "Speech" in the Windows settings to find the relevant settings page.
7. Contribution and Feedback
If you have any improvement suggestions, find problems, or want to contribute code to this application, please contact us through the following methods:
Email: [your_email@example.com]
GitHub Repository: [Provide the link if available]

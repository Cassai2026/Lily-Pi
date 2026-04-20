# CONTRACT: text_string, somatic_state -> paced_audio -> bone_conduction_out
# Purpose: Converts text to paced, cognitive-friendly audio for Oakley frames.

import pyttsx3
import time

class SomaticVoice:
    def __init__(self):
        # Initialize the local Windows TTS engine
        self.engine = pyttsx3.init()
        
        # Set to a clear, calm voice (usually index 1 or 2 on Windows)
        voices = self.engine.getProperty('voices')
        if len(voices) > 1:
            self.engine.setProperty('voice', voices[1].id) 
            
        # The 10^47 Cadence: slightly slower than standard conversation
        self.base_rate = 150 
        self.engine.setProperty('rate', self.base_rate)
        print("[VOICE] Somatic Audio Engine Online.")

    def apply_cognitive_pacing(self, text):
        """
        Injects micro-pauses for neuro-absorption.
        Replaces commas and periods with explicit breath marks.
        """
        paced_text = text.replace(". ", "... ").replace(", ", "... ")
        return paced_text

    def speak(self, text, threat_level=0):
        # Adjust cadence based on the system state
        if threat_level > 5:
            # Speak faster and sharper in a high-static environment
            self.engine.setProperty('rate', 180)
            prefix = "ALERT... "
        else:
            # Calm, steady sovereign pace
            self.engine.setProperty('rate', self.base_rate)
            prefix = ""

        final_text = self.apply_cognitive_pacing(prefix + text)
        print(f"[HUD 🔊] SPEAKING: {final_text}")
        
        # Execute the audio pulse
        self.engine.say(final_text)
        self.engine.runAndWait()

if __name__ == "__main__":
    voice = SomaticVoice()
    
    print("--- Testing Sovereign Cadence ---")
    time.sleep(1)
    
    # Standard Lesson
    voice.speak("Observe the copper wire. It is highly conductive.", threat_level=0)
    time.sleep(1)
    
    # High-Static Environment Warning
    voice.speak("Static detected on the right perimeter. Focus center.", threat_level=7)

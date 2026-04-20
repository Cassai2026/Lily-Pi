from game_engine.sovereign_notebook import SovereignNotebook
from game_engine.somatic_voice import SomaticVoice

def create_student_podcast(source_file):
    notebook = SovereignNotebook()
    voice = SomaticVoice()
    
    lesson = notebook.ingest_source(source_file, "Student_Discovery")
    audio_script = f"Hey Architect! Here is the lesson YOU created about {source_file}. Let's dive in."
    voice.speak(audio_script)

if __name__ == "__main__":
    create_student_podcast("Copper_Conductivity_Test.txt")

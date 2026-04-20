from game_engine.object_trigger import ObjectLessonTrigger
from game_engine.somatic_voice import SomaticVoice
from ui.av_sync import AVSync

def start_automatic_lesson(object_name):
    trigger = ObjectLessonTrigger()
    voice = SomaticVoice()
    sync = AVSync()
    
    lesson = trigger.detect_and_load(object_name)
    if lesson:
        # The Teacher starts the lesson
        text = f"Architect, you found {object_name}. Let's learn about its frequency."
        voice.speak(text)
        sync.sync_subtitle("00:01", text)

if __name__ == "__main__":
    start_automatic_lesson("COPPER_SCRAP")

from game_engine.object_trigger import ObjectLessonTrigger
from game_engine.somatic_voice import SomaticVoice

def run_automatic_teaching(detected_item):
    trigger = ObjectLessonTrigger()
    voice = SomaticVoice()
    
    lesson_text = trigger.process_vision_input(detected_item)
    if lesson_text:
        voice.speak(lesson_text)

if __name__ == "__main__":
    # Simulating the Oakley camera seeing copper
    run_automatic_teaching("COPPER_WIRE")

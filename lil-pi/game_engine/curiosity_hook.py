import random

class CuriosityHook:
    def __init__(self):
        self.hooks = {
            "COPPER": ["Did you know Copper was the first metal used by humans?", "This copper can carry data at the speed of light!"],
            "GRAPHENE": ["Graphene is 200 times stronger than steel!", "This material is only one atom thick."],
            "DEFAULT": ["Notice the pattern here?", "How does this fit into the 29th Node?"]
        }

    def get_hook(self, asset_name):
        options = self.hooks.get(asset_name.upper(), self.hooks["DEFAULT"])
        return f"[HUD 💡] {random.choice(options)}"
    def should_trigger(self, focus_time, last_trigger_time):
        # Only trigger if the child has been looking for > 5s but hasn't been nudged in 2mins
        import time
        if focus_time > 5 and (time.time() - last_trigger_time) > 120:
            return True
        return False
    def adjust_tone(self, excitement_level):
        # Low excitement = more mystery, High excitement = more facts
        if excitement_level > 7:
            return "FACT_MODE"
        return "MYSTERY_MODE"
if __name__ == "__main__":
    hook_engine = CuriosityHook()
    print(hook_engine.get_hook("COPPER"))

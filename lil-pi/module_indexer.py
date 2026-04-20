# CONTRACT: module_path -> registry -> discovery_handle
# Purpose: Central authority for module discovery.

class ModuleIndexer:
    def __init__(self):
        self.registry = {
            "VISION": "game_engine.sovereign_vision",
            "SHIELD": "game_engine.sovereign_shield",
            "UI": "ui.expo_hud_render"
        }
    
    def get_module(self, key):
        return self.registry.get(key.upper(), None)

indexer = ModuleIndexer()

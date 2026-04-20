class VisualMnemonic:
    def __init__(self):
        # ASCII Mnemonics for the Sovereign Assets
        self.shapes = {
            "COPPER": "[=== Cu ===]",
            "GRAPHENE": "/ \ / \ \n\ / \ /",
            "VAULT": "[ #### ]",
            "SHIELD": "<( 29 )>"
        }

    def get_shape(self, asset_name):
        # Returns the visual anchor for the HUD
        return self.shapes.get(asset_name.upper(), "[ ? ]")
    def generate_pulse(self, shape):
        # Adds a "Pulse" effect by alternating brackets
        # Used to show the node is "alive" or "syncing"
        return shape.replace("[", "<").replace("]", ">")
    def get_hud_coordinates(self, importance_level):
        # High importance = Center Screen (540, 960)
        # Low importance = Peripheral (100, 100)
        if importance_level > 8:
            return (960, 540)
        return (100, 100)
if __name__ == "__main__":
    vm = VisualMnemonic()
    copper_shape = vm.get_shape("COPPER")
    print(f"HUD RENDER:\n{copper_shape}")
    print(f"PULSE RENDER:\n{vm.generate_pulse(copper_shape)}")

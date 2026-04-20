import random

class EconomicAlchemist:
    def __init__(self):
        # Real-world base values for Stretford assets
        self.market_rates = {
            "9CU_COPPER": 6.80,  # GBP per KG
            "rPET_POLYMER": 0.45, # GBP per KG
            "GRAPHENE_SCRAP": 120.00 # 1047 Sovereign Value
        }

    def calculate_alchemy(self, material, weight_grams):
        base_rate = self.market_rates.get(material, 0)
        value = (weight_grams / 1000) * base_rate
        # Add the 'Sovereign Multiplier' (Value added by cleaning/processing)
        sovereign_value = value * 1.5 
        
        print(f"[HUD] ⚖️ ECONOMIC AUDIT: {material}")
        print(f"[HUD] Raw Market Value: £{value:.2f}")
        print(f"[HUD] 🏺 ALCHEMICAL VALUE (Processed): £{sovereign_value:.2f}")
        print(f"[HUD] TEACHER: 'By cleaning this {material}, you increased its worth by 50%.'")
        return sovereign_value

if __name__ == "__main__":
    alchemist = EconomicAlchemist()
    alchemist.calculate_alchemy("9CU_COPPER", 500)

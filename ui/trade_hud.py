class TradeHUD:
    def __init__(self):
        self.active_bids = ["Node_42_Construction", "Node_07_Art_Studio"]

    def show_marketplace(self, item_value):
        print("[HUD] 🏪 TRAFFORD MESH MARKETPLACE OPEN")
        for node in self.active_bids:
            print(f"[HUD] BID FROM {node}: {item_value} VT (Vulnerability Tokens)")
        print("[HUD] TEACHER: 'Who will you help today with your resources?'")

if __name__ == "__main__":
    th = TradeHUD()
    th.show_marketplace(7.5)

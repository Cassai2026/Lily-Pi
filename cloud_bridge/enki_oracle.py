# CONTRACT: query -> whitelist_check -> safe_data_return
# Purpose: A secure, read-only bridge to trusted internet sources.

import urllib.request
import json

class EnkiOracle:
    def __init__(self):
        # The Iron Shield Whitelist: Only these domains are permitted.
        self.whitelist = [
            "wikipedia.org",
            "kiddle.co",
            "api.open-meteo.com" # Example for safe weather data
        ]
        print("[ORACLE] Initialized with strict whitelist.")

    def _is_safe(self, url):
        return any(domain in url for domain in self.whitelist)

    def fetch_wikipedia_summary(self, topic):
        """Fetches a plain-text summary from Wikipedia's open API."""
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic.replace(' ', '_')}"
        
        if not self._is_safe(url):
            return "[SHIELD 🛡️] BLOCKED: Domain not on Sovereign Whitelist."

        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Lilieth-Pi-Sovereign-Node/1.0'})
            with urllib.request.urlopen(req, timeout=5) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode())
                    # Extract just the plain text extract, no tracking links
                    return data.get('extract', 'No summary available.')
                return "[ORACLE] Error: Non-200 response."
        except Exception as e:
            return f"[ORACLE] Connection Error: {e}"

if __name__ == "__main__":
    oracle = EnkiOracle()
    print("--- Testing Oracle Connection ---")
    
    # 1. Test a safe query
    print("\nQUERY: Copper")
    result = oracle.fetch_wikipedia_summary("Copper")
    print(f"RESULT: {result[:150]}...") # Print first 150 chars
    
    # 2. Test an unsafe query (simulation)
    print("\nQUERY: Unsafe Domain Test")
    unsafe_result = oracle._is_safe("https://reddit.com/r/science")
    print(f"IS SAFE? {unsafe_result}")

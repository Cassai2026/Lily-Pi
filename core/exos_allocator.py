# CONTRACT: app_request -> resource_multiplexer -> hardware_slice
# Purpose: Exokernel-style resource isolation. Protects critical Eye-Node RAM.

class ExOSAllocator:
    def __init__(self, total_ram_mb=8192):
        self.total_ram = total_ram_mb
        self.reservations = {
            "KERNEL": 512,
            "EYE_NODE": 1024, # Vision is non-negotiable
            "ENKI_BRAIN": 4096,
            "GHOST_MESH": 256
        }
        self.active_usage = {k: 0 for k in self.reservations}

    def request_resource(self, module, amount_mb):
        limit = self.reservations.get(module, 0)
        if amount_mb > limit:
            print(f"[🚨 EXOS] REJECTED: {module} requested {amount_mb}MB (Limit: {limit}MB)")
            return False
        
        self.active_usage[module] = amount_mb
        print(f"[📊 EXOS] ALLOCATED: {amount_mb}MB to {module}.")
        return True

    def get_system_vitals(self):
        used = sum(self.active_usage.values())
        print(f"[SYSTEM] Total Load: {used}/{self.total_ram} MB | Overhead: {self.total_ram - used} MB Free")

if __name__ == "__main__":
    allocator = ExOSAllocator()
    # High-Priority Vision Start
    allocator.request_resource("EYE_NODE", 800)
    # AI Brain Start
    allocator.request_resource("ENKI_BRAIN", 3000)
    # Attempting to Over-allocate (The Trap)
    allocator.request_resource("GHOST_MESH", 500) 
    
    allocator.get_system_vitals()

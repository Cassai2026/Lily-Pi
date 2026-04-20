from cloud_bridge.webrtc_mesh import WebRTCMeshNode
from game_engine.knowledge_cache import LocalKnowledgeCache

def bridge_mesh_to_ssd(incoming_data):
    cache = LocalKnowledgeCache()
    # If a peer sends a lesson, we grab it and cache it immediately
    topic = incoming_data.get("topic", "Community_Note")
    content = incoming_data.get("content", "")
    cache.cache_lesson(topic, content)

if __name__ == "__main__":
    test_data = {"topic": "Recycled PET Strength", "content": "rPET has a Young's Modulus of..."}
    bridge_mesh_to_ssd(test_data)

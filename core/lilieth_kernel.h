#ifndef LILIETH_KERNEL_H
#define LILIETH_KERNEL_H

#define NODE_COUNT 17
#define MISSION_STATEMENT "GLOBAL NGO MANDATE: SYSTEM INITIALIZED FOR HUMANITY"

typedef struct {
    const char* node_name;
    int sdg_id;
    const char* mandate;
} SovereignNode;

static const SovereignNode PANTHEON[NODE_COUNT] = {
    {"CassAi", 1, "Financial Sovereignty"},
    {"Lilieth", 2, "Zero Hunger / Logistics"},
    {"Odin", 3, "Good Health / Biometrics"},
    {"Set", 17, "Node Integration"}
};
#endif

// Law 21: Cognitive Sovereignty
// The Architect's focus is the primary asset. All distractions are administrative theft.
#define FOCUS_LOCK_ACTIVE 1

// Law 22: Environmental Mastery
// The Night is not a barrier; it is a forensic canvas.
#define NIGHTRIDE_ENABLED 1
#define THERMAL_THRESHOLD 80

// Law 22: Environmental Mastery
// The Night is not a barrier; it is a forensic canvas.
#define NIGHTRIDE_ENABLED 1
#define THERMAL_THRESHOLD 80

// Law 23: Radical Transparency
// No shadow remains in the presence of the Sovereign Lens.
#define SOCIAL_INTERCEPTOR_ACTIVE 1
#define BIOMETRIC_HUD_OVERLAY 1

// Law 24: The Eternal Student
// The Node must teach to learn, and learn to teach.
#define EDU_SCAFFOLD_ACTIVE 1
#define RESEARCH_MODE_ENABLED 1

// Law 24: The Eternal Student
// The Node must teach to learn, and learn to teach.
#define EDU_SCAFFOLD_ACTIVE 1
#define RESEARCH_MODE_ENABLED 1

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

import pygame

class NPC:
    def __init__(self, name, position, speech):
        self.name = name
        self.position = position
        self.speech = speech
        self.interaction_count = 0
    
    def npc_info():
        npc_data = [
            NPC("Maria", (100, 100), "In the morning, I made breakfast for my husband..."),
            NPC("Willie", (600, 400), "Breakfast with my wife started the day..."),
            NPC("Amber", (600, 100), "In the day, I exercised in the park..."),
            NPC("Officer Marlowe", (100, 400), "Please help me find the killer before it's too late!")
        ]

    def handle_npc_interaction(player_rect, npc_rect, npc, hide_speech):
        pass

# Other NPC-related functions

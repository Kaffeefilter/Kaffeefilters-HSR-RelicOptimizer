CAVERN_RELICS_DETAILS = {
    "band_of_sizzling_thunder": {
        "name": "Band of Sizzling Thunder",
        "set_icon_url": "",
        "head_icon_url": "",
        "hands_icon_url": "",
        "body_icon_url": "",
        "feet_icon_url": "",
        "two_piece_bonus": {
            "description": "Increases Lightning DMG by 10%.",
            "effects": [{"type": "lightning_dmg", "value": 0.10}],
        },
        "four_piece_bonus": {
            "description": (
                "When the wearer uses their Skill, increases the wearer's ATK by 20% "
                "for 1 turn(s)."
            ),
            "effects": [{
                "type": "atk",
                "value": 0.20,
                "duration": 1,
                "trigger_condition": {
                    "type": "on_skill_use",
                    "description": "Trigger when wearer uses their Skill.",
                },
            }],
        },
    },
    "eagle_of_twilight_line": {
        "name": "Eagle of Twilight Line",
        "set_icon_url": "",
        "head_icon_url": "",
        "hands_icon_url": "",
        "body_icon_url": "",
        "feet_icon_url": "",
        "two_piece_bonus": {
            "description": "Increases SPD by 12%.",
            "effects": [{"type": "spd", "value": 0.12}],
        },
        "four_piece_bonus": {
            "description": "After using Ultimate, advances action forward by 25%.",
            "effects": [{
                "type": "action_advance",
                "value": 0.25,
                "trigger_condition": {
                    "type": "on_ultimate",
                    "description": "Trigger after using Ultimate.",
                },
            }],
        },
    },
    "champion_of_streetwise_boxing": {
        "name": "Champion of Streetwise Boxing",
        "set_icon_url": "",
        "head_icon_url": "",
        "hands_icon_url": "",
        "body_icon_url": "",
        "feet_icon_url": "",
        "two_piece_bonus": {
            "description": "Increases Physical DMG by 10%.",
            "effects": [{"type": "physical_dmg", "value": 0.10}],
        },
        "four_piece_bonus": {
            "description": (
                "After the wearer attacks or is hit, their ATK increases by 5% for "
                "the rest of the battle. This effect can stack up to 5 time(s)."
            ),
            "effects": [{
                "type": "atk",
                "stackable": True,
                "stack_value": 0.05,  # 5% pro Stack
                "max_stacks": 5,     # Maximal 5 Stacks
                "trigger_condition": {
                    "type": "on_attack_or_hit",
                    "description": "Trigger after wearer attacks or is hit.",
                },
            }],
        },
    }
    # ...
}

PLANAR_ORNAMENTS_DETAILS = {
    "belobog_of_the_architects": {
        "name": "Belobog of the Architects",
        "set_icon_url": "",  
        "planar_sphere_icon_url": "",  
        "link_rope_icon_url": "",  
        "two_piece_bonus": {
            "description": (
                "Increases the wearer's DEF by 15%. "
                "When the wearer's Effect Hit Rate is 50% or higher, the wearer gains an extra 15% DEF."
            ),
            "effects": [
                {"type": "def", "value": 0.15}, 
                {
                    "type": "def",
                    "value": 0.15,  
                    "trigger_condition": {
                        "type": "effect_hit_rate",
                        "comparison": ">=",
                        "threshold": 50, 
                    },
                },
            ],
        },
    },
    # ...
}
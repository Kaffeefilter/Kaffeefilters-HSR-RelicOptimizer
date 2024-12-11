CAVERN_RELICS_DETAILS = {
    "band_of_sizzling_thunder": {
        "name": "Band of Sizzling Thunder",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/6/6e/Item_Band_of_Sizzling_Thunder.png",
        "head_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/b/b6/Item_Band%27s_Polarized_Sunglasses.png",
        "hands_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/7/7d/Item_Band%27s_Touring_Bracelet.png",
        "body_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/b/b9/Item_Band%27s_Leather_Jacket_With_Studs.png",
        "feet_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/a/ae/Item_Band%27s_Ankle_Boots_With_Rivets.png",
        "two_piece_bonus": {
            "description": "Increases Lightning DMG by 10%.",
            "effects": {"type": "lightning_dmg", "value": 0.10}
        },
        "four_piece_bonus": {
            "description": "When the wearer uses their Skill, increases the wearer's ATK by 20% for 1 turn(s).",
            "effects": [{
                "type": "atk",
                "value": 0.20,
                "duration": 1,
                "trigger_condition": {
                    "type": "on_skill_use"
                }
            }]
        }
    },
    "champion_of_streetwise_boxing": {
        "name": "Champion of Streetwise Boxing",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/b/b9/Item_Champion_of_Streetwise_Boxing.png",
        "head_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/e/ee/Item_Champion%27s_Headgear.png",
        "hands_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/6/6d/Item_Champion%27s_Heavy_Gloves.png",
        "body_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/3/3a/Item_Champion%27s_Chest_Guard.png",
        "feet_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/7/77/Item_Champion%27s_Fleetfoot_Boots.png",
        "two_piece_bonus": {
            "description": "Increases Physical DMG by 10%.",
            "effects": {"type": "physical_dmg", "value": 0.10}
        },
        "four_piece_bonus": {
            "description": "After the wearer attacks or is hit, their ATK increases by 5% for the rest of the battle. This effect can stack up to 5 time(s).",
            "effects": [{
                "type": "atk",
                "stackable": True,
                "stack_value": 0.05,  # 5% pro Stack
                "max_stacks": 5,     # Maximal 5 Stacks
                "trigger_condition": {
                    "type": "on_attack_or_hit"
                }
            }]
        }
    },
    "eagle_of_twilight_line": {
        "name": "Eagle of Twilight Line",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/3/3f/Item_Eagle_of_Twilight_Line.png",
        "head_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/1/13/Item_Eagle%27s_Beaked_Helmet.png",
        "hands_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/9/9b/Item_Eagle%27s_Soaring_Ring.png",
        "body_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/9/9f/Item_Eagle%27s_Winged_Suit_Harness.png",
        "feet_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/f/fd/Item_Eagle%27s_Quilted_Puttees.png",
        "two_piece_bonus": {
            "description": "Increases Wind DMG by 10%.",
            "effects": {"type": "wind_dmg", "value": 0.10}
        },
        "four_piece_bonus": {
            "description": "After the wearer uses their Ultimate, their action is Advanced Forward by 25%.",
            "effects": [{
                "type": "action_advance",
                "value": 0.25,
                "trigger_condition": {
                    "type": "on_ultimate"
                }
            }]
        }
    },
    "firesmith_of_lava-forging": {
        "name": "Firesmith of Lava-Forging",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/9/96/Item_Firesmith_of_Lava-Forging.png",
        "head_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/c/c3/Item_Firesmith%27s_Obsidian_Goggles.png",
        "hands_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/5/5d/Item_Firesmith%27s_Ring_of_Flame-Mastery.png",
        "body_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/b/be/Item_Firesmith%27s_Fireproof_Apron.png",
        "feet_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/6/6c/Item_Firesmith%27s_Alloy_Leg.png",
        "two_piece_bonus": {
            "description": "Increases Fire DMG by 10%.",
            "effects": {"type": "fire_dmg", "value": 0.10}
        },
        "four_piece_bonus": {
            "description": "Increases the wearer's Skill DMG by 12%. After unleashing Ultimate, increases the wearer's Fire DMG by 12% for the next attack.",
            "effects": [{
                "type": "skill_dmg", 
                "value": 0.12
            },{
                "type": "fire_dmg",
                "value": 0.12,
                "duration": "next_attack",
                "trigger_condition": {
                    "type": "on_ultimate"
                }
            }]
        }
    },
    "genius_of_brilliant_stars": {
        "name": "Genius of Brilliant Stars",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/a/aa/Item_Genius_of_Brilliant_Stars.png",
        "head_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/e/ef/Item_Genius%27s_Ultraremote_Sensing_Visor.png",
        "hands_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/1/18/Item_Genius%27s_Frequency_Catcher.png",
        "body_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/5/5c/Item_Genius%27s_Metafield_Suit.png",
        "feet_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/5/59/Item_Genius%27s_Gravity_Walker.png",
        "two_piece_bonus": {
            "description": "Increases Quantum DMG by 10%.",
            "effects": {"type": "quantum_dmg", "value": 0.10}
        },
        "four_piece_bonus": {
            "description": "When the wearer deals DMG to the target enemy, ignores 10% DEF. If the target enemy has Quantum Weakness, the wearer additionally ignores 10% DEF.",
            "effects": [{
                "type": "ignore_def", 
                "value": 0.10,
            },{
                "type": "ignore_def",
                "value": 0.10,
                "trigger_condition": {
                    "type": "on_quantum_weakness"
                }
            }]
        }
    },
    "guard_of_wuthering_snow": {
        "name": "Guard of Wuthering Snow",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/d/d8/Item_Guard_of_Wuthering_Snow.png",
        "head_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/d/d6/Item_Guard%27s_Cast_Iron_Helmet.png",
        "hands_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/6/69/Item_Guard%27s_Shining_Gauntlets.png",
        "body_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/f/f3/Item_Guard%27s_Uniform_of_Old.png",
        "feet_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/5/59/Item_Guard%27s_Silver_Greaves.png",
        "two_piece_bonus": {
            "description": "Reduces DMG taken by 8%.",
            "effects": {"type": "damage_reduction", "value": 0.08}
        },
        "four_piece_bonus": {
            "description": "At the beginning of the turn, if the wearer's HP is equal to or less than 50%, restores HP equal to 8% of their Max HP and regenerates 5 Energy.",
            "effects": [{
                "type": "hp",
                "value": 0.08,
                "trigger_condition": {
                    "type": "hp",
                    "comparison": "<=",
                    "threshold": 0.5
                }
            },{
                "type": "energy_gain",
                "value": 5,
                "trigger_condition": {
                    "type": "hp",
                    "comparison": "<=",
                    "threshold": 0.5
                }
            }]
        }
    },
    "hunter_of_glacial_forest": {
        "name": "Hunter of Glacial Forest",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/e/e8/Item_Hunter_of_Glacial_Forest.png",
        "head_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/e/e2/Item_Hunter%27s_Artaius_Hood.png",
        "hands_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/c/c4/Item_Hunter%27s_Lizard_Gloves.png",
        "body_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/5/57/Item_Hunter%27s_Ice_Dragon_Cloak.png",
        "feet_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/e/e6/Item_Hunter%27s_Soft_Elkskin_Boots.png",
        "two_piece_bonus": {
            "description": "Increases Ice DMG by 10%.",
            "effects": {"type": "ice_dmg", "value": 0.10}
        },
        "four_piece_bonus": {
            "description": "After the wearer uses their Ultimate, their CRIT DMG increases by 25% for 2 turn(s).",
            "effects": {
                "type": "crit_dmg",
                "value": 0.25,
                "duration": 2,
                "trigger_condition": {
                    "type": "on_ultimate"
                }
            }
        }
    },
    "iron_cavalry_against_the_scourge": {
        "name": "Iron Cavalry Against the Scourge",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/4/49/Item_Iron_Cavalry_Against_the_Scourge.png",
        "head_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/0/0d/Item_Iron_Cavalry%27s_Homing_Helm.png",
        "hands_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/1/11/Item_Iron_Cavalry%27s_Crushing_Wristguard.png",
        "body_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/d/d8/Item_Iron_Cavalry%27s_Silvery_Armor.png",
        "feet_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/4/40/Item_Iron_Cavalry%27s_Skywalk_Greaves.png",
        "two_piece_bonus": {
            "description": "Increases Break Effect by 16%.",
            "effects": {"type": "break_effect", "value": 0.16}
        },
        "four_piece_bonus": {
            "description": "If the wearer's Break Effect is 150% or higher, the Break DMG dealt to the enemy target ignores 10% of their DEF. If the wearer's Break Effect is 250% or higher, the Super Break DMG dealt to the enemy target additionally ignores 15% of their DEF.",
            "effects": [{
                "type": "break_dmg_ignore_def",
                "value": 0.10,
                "trigger_condition": {
                    "type": "break_effect",
                    "comparison": ">=",
                    "threshold": 1.5
                }
            },{
                "type": "super_break_dmg_ignore_def",   # super break buffs = normal break buffs + super break buffs
                "value": 0.15,
                "trigger_condition": {
                    "type": "break_effect",
                    "comparison": ">=",
                    "threshold": 2.5
                }
            }]
        }
    },
    "knight_of_purity_palace": {
        "name": "Knight of Purity Palace",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/1/1f/Item_Knight_of_Purity_Palace.png",
        "head_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/7/7c/Item_Knight%27s_Forgiving_Casque.png",
        "hands_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/9/91/Item_Knight%27s_Silent_Oath_Ring.png",
        "body_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/4/4a/Item_Knight%27s_Solemn_Breastplate.png",
        "feet_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/e/ea/Item_Knight%27s_Iron_Boots_of_Order.png",
        "two_piece_bonus": {
            "description": "Increases DEF by 15%.",
            "effects": {"type": "def", "value": 0.15}
        },
        "four_piece_bonus": {
            "description": "Increases the max DMG that can be absorbed by the Shield created by the wearer by 20%.",
            "effects": [{
                "type": "shield_strength",
                "value": 0.20
            }]
        }
    },
    "longevous_disciple": {
        "name": "Longevous Disciple",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/4/4a/Item_Longevous_Disciple.png",
        "head_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/4/4b/Item_Disciple%27s_Prosthetic_Eye.png",
        "hands_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/3/37/Item_Disciple%27s_Ingenium_Hand.png",
        "body_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/b/b3/Item_Disciple%27s_Dewy_Feather_Garb.png",
        "feet_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/7/7f/Item_Disciple%27s_Celestial_Silk_Sandals.png",
        "two_piece_bonus": {
            "description": "Increases Max HP by 12%.",
            "effects": {"type": "max_hp", "value": 0.12}
        },
        "four_piece_bonus": {
            "description": "When the wearer is hit or has their HP consumed by an ally or themselves, their CRIT Rate increases by 8% for 2 turn(s) and up to 2 stacks.",
            "effects": [{
                "type": "crit_rate",
                "stackable": True,
                "stack_value": 0.08,
                "max_stacks": 2,
                "duration": 2,
                "trigger_condition": {
                    "type": "on_hit_or_hp_consumed"
                }
            }]
        }
    },
    "messenger_traversing_hackerspace": {
        "name": "Messenger Traversing Hackerspace",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/a/ac/Item_Messenger_Traversing_Hackerspace.png",
        "head_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/e/e4/Item_Messenger%27s_Holovisor.png",
        "hands_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/a/a5/Item_Messenger%27s_Transformative_Arm.png",
        "body_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/7/7d/Item_Messenger%27s_Secret_Satchel.png",
        "feet_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/b/be/Item_Messenger%27s_Par-kool_Sneakers.png",
        "two_piece_bonus": {
            "description": "Increases SPD by 6%.",
            "effects": {"type": "spd", "value": 0.06}
        },
        "four_piece_bonus": {
            "description": "When the wearer uses their Ultimate on an ally, SPD for all allies increases by 12% for 1 turn(s). This effect cannot be stacked.",
            "effects": {
                "type": "spd",
                "target": "all_allies",
                "value": 0.12,
                "duration": 1,
                "stackable": False,
                "trigger_condition": {
                    "type": "on_ultimate"
                }
            }
        }
    },
    "musketeer_of_wild_wheat": {
        "name": "Musketeer of Wild Wheat",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/f/fc/Item_Musketeer_of_Wild_Wheat.png",
        "head_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/7/7a/Item_Musketeer%27s_Wild_Wheat_Felt_Hat.png",
        "hands_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/8/83/Item_Musketeer%27s_Coarse_Leather_Gloves.png",
        "body_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/e/e8/Item_Musketeer%27s_Wind-Hunting_Shawl.png",
        "feet_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/b/bf/Item_Musketeer%27s_Rivets_Riding_Boots.png",
        "two_piece_bonus": {
            "description": "ATK increases by 12%.",
            "effects": {"type": "atk", "value": 0.12}
        },
        "four_piece_bonus": {
            "description": "The wearer's SPD increases by 6% and Basic ATK DMG increases by 10%.",
            "effects": {[
                {"type": "spd", "value": 0.06}
            ],[
                {"type": "basic_atk_dmg", "value": 0.10}
            ]}
        }
    },
    "passerby_of_wandering_cloud": {
        "name": "Passerby of Wandering Cloud",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/a/aa/Item_Passerby_of_Wandering_Cloud.png",
        "head_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/0/00/Item_Passerby%27s_Rejuvenated_Wooden_Hairstick.png",
        "hands_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/7/7c/Item_Passerby%27s_Roaming_Dragon_Bracer.png",
        "body_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/7/78/Item_Passerby%27s_Ragged_Embroided_Coat.png",
        "feet_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/7/7d/Item_Passerby%27s_Stygian_Hiking_Boots.png",
        "two_piece_bonus": {
            "description": "Increases Outgoing Healing by 10%.",
            "effects": {"type": "outgoing_healing", "value": 0.10}
        },
        "four_piece_bonus": {
            "description": "At the start of the battle, immediately regenerates 1 Skill Point.",
            "effects": [{
                "type": "skill_point_gain",
                "value": 1,
                "trigger_condition": {
                    "type": "start_of_battle"
                }
            }]
        }
    },
    "pioneer_diver_of_dead_waters": {
        "name": "Pioneer Diver of Dead Waters",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/8/86/Item_Pioneer_Diver_of_Dead_Waters.png",
        "head_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/1/16/Item_Pioneer%27s_Heatproof_Shell.png",
        "hands_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/4/48/Item_Pioneer%27s_Lacuna_Compass.png",
        "body_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/5/50/Item_Pioneer%27s_Sealed_Lead_Apron.png",
        "feet_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/0/03/Item_Pioneer%27s_Starfaring_Anchor.png",
        "two_piece_bonus": {
            "description": "Increases DMG dealt to enemies with debuffs by 12%.",
            "effects": {"type": "dmg_to_debuffed", "value": 0.12}
        },
        "four_piece_bonus": {
            "description": "Increases CRIT Rate by 4%. The wearer deals 8%/12% increased CRIT DMG to enemies with at least 2/3 debuffs. After the wearer inflicts a debuff on enemy targets, the aforementioned effects increase by 100%, lasting for 1 turn(s).",
            "effects": [{
                "type": "crit_rate",
                "value": 0.04
            },{
                "type": "crit_dmg",
                "value": 0.08,
                "trigger_condition": {
                    "type": "on_debuff",
                    "comparison": "==",
                    "threshold": 2
                },
                "enhancement": {
                    "value_multiplier": 2,
                    "duration": 1,
                    "trigger_condition": {
                        "type": "on_debuff_inflict"
                    }
                }
            }, {
                "type": "crit_dmg",
                "value": 0.12,
                "trigger_condition": {
                    "type": "on_debuff",
                    "comparison": ">=",
                    "threshold": 3
                },
                "enhancement": {
                    "value_multiplier": 2,
                    "duration": 1,
                    "trigger_condition": {
                        "type": "on_debuff_inflict"
                    }
                }
            }]
        }
    },
    "prisoner_in_deep_confinement": {
        "name": "Prisoner in Deep Confinement",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/b/b3/Item_Prisoner_in_Deep_Confinement.png",
        "head_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/5/54/Item_Prisoner%27s_Sealed_Muzzle.png",
        "hands_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/5/55/Item_Prisoner%27s_Leadstone_Shackles.png",
        "body_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/0/0b/Item_Prisoner%27s_Repressive_Straitjacket.png",
        "feet_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/2/2e/Item_Prisoner%27s_Restrictive_Fetters.png",
        "two_piece_bonus": {
            "description": "ATK increases by 12%.",
            "effects": {"type": "atk", "value": 0.12}
        },
        "four_piece_bonus": { 
            "description": "For every DoT the target enemy is afflicted with, the wearer will ignore 6% of its DEF when dealing DMG to it. This effect is valid for a max of 3 DoTs.",
            "effects": [{
                "type": "def_ignore",
                "stackable": True,
                "stack_value": 0.06,
                "max_stacks": 3,
                "trigger_condition": {
                    "type": "dot_count_on_target",  
                    "comparison": ">=",
                    "threshold": 1,
                    "stacks_from_condition": True,  # Stacks are derived from the number of DoTs
                }
            }]
        }
    },
    "sacerdos'_relived_ordeal": {
        "name": "Sacerdos' Relived Ordeal",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/6/63/Item_Sacerdos%27_Relived_Ordeal.png",
        "head_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/8/82/Item_Sacerdos%27_Melodic_Earrings.png",
        "hands_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/8/8f/Item_Sacerdos%27_Welcoming_Gloves.png",
        "body_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/7/74/Item_Sacerdos%27_Ceremonial_Garb.png",
        "feet_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/6/6e/Item_Sacerdos%27_Arduous_Boots.png",
        "two_piece_bonus": {
            "description": "Increases SPD by 6%.",
            "effects": {"type": "spd", "value": 0.06}
        },
        "four_piece_bonus": {
            "description": "When using Skill or Ultimate on one ally target, increases the ability target's CRIT DMG by 18%, lasting for 2 turn(s). This effect can stack up to 2 time(s).",
            "effects": [{
                "type": "crit_dmg",
                "stackable": True,
                "stack_value": 0.18,
                "max_stacks": 2,
                "duration": 2,
                "target": "ally",
                "trigger_condition": {
                    "type": "on_skill_use_or_ultimate",
                    "target": "ally"
                }
            }]
        }
    },
    "scholar_lost_in_erudition": {
        "name": "Scholar Lost in Erudition",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/f/fc/Item_Scholar_Lost_in_Erudition.png",
        "head_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/6/6d/Item_Scholar%27s_Silver-Rimmed_Monocle.png",
        "hands_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/9/91/Item_Scholar%27s_Auxiliary_Knuckle.png",
        "body_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/8/8d/Item_Scholar%27s_Tweed_Jacket.png",
        "feet_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/f/fa/Item_Scholar%27s_Felt_Snowboots.png",
        "two_piece_bonus": {
            "description": "Increases CRIT Rate by 8%.",
            "effects": {"type": "crit_rate", "value": 0.08}
        },
        "four_piece_bonus": {
            "description": "Increases DMG dealt by Skill and Ultimate by 20%. After using Ultimate, additionally increases the DMG dealt by the next Skill by 25%.",
            "effects": [{
                "type": "skill_dmg",
                "value": 0.20
            },{
                "type": "ultimate_dmg",
                "value": 0.20
            },{
                "type": "skill_dmg",
                "value": 0.25,
                "duration": "next_skill_use",
                "trigger_condition": {
                    "type": "on_ultimate"
                }
            }]
        }
    },
    "the_ashblazing_grand_duke": {
        "name": "The Ashblazing Grand Duke",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/3/36/Item_The_Ashblazing_Grand_Duke.png",
        "head_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/8/86/Item_Grand_Duke%27s_Crown_of_Netherflame.png",
        "hands_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/f/f7/Item_Grand_Duke%27s_Gloves_of_Fieryfur.png",
        "body_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/0/01/Item_Grand_Duke%27s_Robe_of_Grace.png",
        "feet_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/1/1c/Item_Grand_Duke%27s_Ceremonial_Boots.png",
        "two_piece_bonus": {
            "description": "Increases the DMG dealt by follow-up attacks by 20%.",
            "effects": {"type": "follow_up_dmg", "value": 0.20}
        },
        "four_piece_bonus": {
            "description": "When the wearer uses follow-up attacks, increases the wearer's ATK by 6% for every time the follow-up attack deals DMG. This effect can stack up to 8 time(s) and lasts for 3 turn(s). This effect is removed the next time the wearer uses a follow-up attack.",
            "effects": [{
                "type": "atk",
                "value_per_stack": 0.06,
                "max_stacks": 8,
                "duration": 3,
                "stackable": True,
                "stack_removal_condition": { 
                    "type": "on_follow_up"  # Stacks are removed on the next follow-up attack
                },
                "trigger_condition": {
                    "type": "on_follow_up_hit",  # Triggered for each hit within a follow-up attack
                }
            }]
        }
    },
    "the_wind-soaring_valorous": {
        "name": "The Wind-Soaring Valorous",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/1/1e/Item_The_Wind-Soaring_Valorous.png",
        "head_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/1/10/Item_Valorous_Mask_of_Northern_Skies.png",
        "hands_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/b/b8/Item_Valorous_Bracelet_of_Grappling_Hooks.png",
        "body_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/9/95/Item_Valorous_Plate_of_Soaring_Flight.png",
        "feet_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/5/59/Item_Valorous_Greaves_of_Pursuing_Hunt.png",
        "two_piece_bonus": {
            "description": "Increases ATK by 12%.",
            "effects": {"type": "atk", "value": 0.12}
        },
        "four_piece_bonus": {
            "description": "Increases the wearer's CRIT Rate by 6%. When the wearer uses a follow-up attack, increases the DMG dealt by Ultimate by 36%, lasting for 1 turn(s).",
            "effects": [{
                "type": "crit_rate",
                "value": 0.06,
            },{
                "type": "ultimate_dmg",
                "value": 0.36,
                "duration": 1,
                "trigger_condition": {
                    "type": "on_follow_up"
                }
            }]
        }
    },
    "thief_of_shooting_meteor": {
        "name": "Thief of Shooting Meteor",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/9/9c/Item_Thief_of_Shooting_Meteor.png",
        "head_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/8/86/Item_Thief%27s_Myriad-Faced_Mask.png",
        "hands_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/b/b1/Item_Thief%27s_Gloves_With_Prints.png",
        "body_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/7/70/Item_Thief%27s_Steel_Grappling_Hook.png",
        "feet_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/d/d4/Item_Thief%27s_Meteor_Boots.png",
        "two_piece_bonus": {
            "description": "Increases Break Effect by 16%.",
            "effects": {"type": "break_effect", "value": 0.16}
        },
        "four_piece_bonus": {
            "description": "Increases the wearer's Break Effect by 16%. After the wearer inflicts Weakness Break on an enemy, regenerates 3 Energy.",
            "effects": [{
                "type": "break_effect",
                "value": 0.16
            },{
                "type": "energy_gain",
                "value": 3,
                "trigger_condition": {
                    "type": "on_weakness_break"
                }
            }]
        }
    },
    "wastelander_of_banditry_desert": {
        "name": "Wastelander of Banditry Desert",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/a/aa/Item_Wastelander_of_Banditry_Desert.png",
        "head_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/d/d4/Item_Wastelander%27s_Breathing_Mask.png",
        "hands_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/5/5a/Item_Wastelander%27s_Desert_Terminal.png",
        "body_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/f/fb/Item_Wastelander%27s_Friar_Robe.png",
        "feet_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/4/46/Item_Wastelander%27s_Powered_Greaves.png",
        "two_piece_bonus": {
            "description": "Increases Imaginary DMG by 10%.",
            "effects": {"type": "imaginary_dmg", "value": 0.10}
        },
        "four_piece_bonus": {
            "description": "When attacking debuffed enemies, the wearer's CRIT Rate increases by 10%, and their CRIT DMG increases by 20% against Imprisoned enemies.",
            "effects": [{
                "type": "crit_rate",
                "value": 0.10,
                "trigger_condition": {
                    "type": "on_debuff",
                }
            },{
                "type": "crit_damage",
                "value": 0.20,
                "trigger_condition": {
                    "type": "on_imprisoned",
                }
            }]
        }
    },
    "watchmaker,_master_of_dream_machinations": {
        "name": "Watchmaker, Master of Dream Machinations",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/c/ca/Item_Watchmaker%2C_Master_of_Dream_Machinations.png",
        "head_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/3/30/Item_Watchmaker%27s_Telescoping_Lens.png",
        "hands_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/a/a6/Item_Watchmaker%27s_Fortuitous_Wristwatch.png",
        "body_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/0/01/Item_Watchmaker%27s_Illusory_Formal_Suit.png",
        "feet_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/e/e4/Item_Watchmaker%27s_Dream-Concealing_Dress_Shoes.png",
        "two_piece_bonus": {
            "description": "Increases Break Effect by 16%.",
            "effects": {"type": "break_effect", "value": 0.16}
        },
        "four_piece_bonus": {
            "description": "When the wearer uses their Ultimate on an ally, all allies' Break Effect increases by 30% for 2 turn(s). This effect cannot be stacked.",
            "effects": [{
                "type": "break_effect",
                "value": 0.30,
                "duration": 2,
                "target": "all_allies",
                "stackable": True,
                "trigger_condition": {
                    "type": "on_ultimate",
                    "target": "ally"
                }
            }]
        }
    }
}

PLANAR_ORNAMENTS_DETAILS = {
    "belobog_of_the_architects": {
        "name": "Belobog of the Architects",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/9/99/Item_Belobog_of_the_Architects.png",
        "planar_sphere_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/2/2f/Item_Belobog%27s_Fortress_of_Preservation.png",
        "link_rope_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/7/7f/Item_Belobog%27s_Iron_Defense.png",
        "two_piece_bonus": {
            "description": "Increases the wearer's DEF by 15%. When the wearer's Effect Hit Rate is 50% or higher, the wearer gains an extra 15% DEF.",
            "effects": []
        }
    },
    "broken_keel": {
        "name": "Broken Keel",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/0/00/Item_Broken_Keel.png",
        "planar_sphere_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/1/17/Item_Insumousu%27s_Whalefall_Ship.png",
        "link_rope_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/9/92/Item_Insumousu%27s_Frayed_Hawser.png",
        "two_piece_bonus": {
            "description": "Increases the wearer's Effect RES by 10%. When the wearer's Effect RES is at 30% or higher, all allies' CRIT DMG increases by 10%.",
            "effects": []
        }
    },
    "celestial_differentiator": {
        "name": "Celestial Differentiator",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/c/c2/Item_Celestial_Differentiator.png",
        "planar_sphere_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/6/66/Item_Planet_Screwllum%27s_Mechanical_Sun.png",
        "link_rope_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/3/36/Item_Planet_Screwllum%27s_Ring_System.png",
        "two_piece_bonus": {
            "description": "Increases the wearer's CRIT DMG by 16%. When the wearer's current CRIT DMG reaches 120% or higher, after entering battle, the wearer's CRIT Rate increases by 60% until the end of their first attack.",
            "effects": []
        }
    },
    "duran,_dynasty_of_running_wolves": {
        "name": "Duran, Dynasty of Running Wolves",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/d/d5/Item_Duran%2C_Dynasty_of_Running_Wolves.png",
        "planar_sphere_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/2/2e/Item_Duran%27s_Tent_of_Golden_Sky.png",
        "link_rope_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/4/46/Item_Duran%27s_Mechabeast_Bridle.png",
        "two_piece_bonus": {
            "description": "When an ally uses follow-up attacks, the wearer gains 1 stack of Merit, stacking up to 5 time(s). Each stack of Merit increases the DMG dealt by the wearer's follow-up attacks by 5%. When there are 5 stacks, additionally increases the wearer's CRIT DMG by 25%.",
            "effects": []
        }
    },
    "firmament_frontline:_glamoth": {
        "name": "Firmament Frontline: Glamoth",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/f/f7/Item_Firmament_Frontline_Glamoth.png",
        "planar_sphere_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/8/8e/Item_Glamoth%27s_Iron_Cavalry_Regiment.png",
        "link_rope_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/7/7d/Item_Glamoth%27s_Silent_Tombstone.png",
        "two_piece_bonus": {
            "description": "Increases the wearer's ATK by 12%. When the wearer's SPD is equal to or higher than 135/160, the wearer deals 12%/18% more DMG.",
            "effects": []
        }
    },
    "fleet_of_the_ageless": {
        "name": "Fleet of the Ageless",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/a/a1/Item_Fleet_of_the_Ageless.png",
        "planar_sphere_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/9/90/Item_The_Xianzhou_Luofu%27s_Celestial_Ark.png",
        "link_rope_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/0/0b/Item_The_Xianzhou_Luofu%27s_Ambrosial_Arbor_Vines.png",
        "two_piece_bonus": {
            "description": "Increases the wearer's Max HP by 12%. When the wearer's SPD reaches 120 or higher, all allies' ATK increases by 8%.",
            "effects": []
        }
    },
    "forge_of_the_kalpagni_lantern": {
        "name": "Forge of the Kalpagni Lantern",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/b/bb/Item_Forge_of_the_Kalpagni_Lantern.png",
        "planar_sphere_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/1/1b/Item_Forge%27s_Lotus_Lantern_Wick.png",
        "link_rope_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/8/86/Item_Forge%27s_Heavenly_Flamewheel_Silk.png",
        "two_piece_bonus": {
            "description": "Increases the wearer's SPD by 6%. When the wearer hits an enemy target that has Fire Weakness, the wearer's Break Effect increases by 40%, lasting for 1 turn(s).",
            "effects": []
        }
    },
    "inert_salsotto": {
        "name": "Inert Salsotto",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/f/f5/Item_Inert_Salsotto.png",
        "planar_sphere_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/3/3c/Item_Salsotto%27s_Moving_City.png",
        "link_rope_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/c/cc/Item_Salsotto%27s_Terminator_Line.png",
        "two_piece_bonus": {
            "description": "Increases the wearer's CRIT Rate by 8%. When the wearer's current CRIT Rate reaches 50% or higher, the wearer's Ultimate and follow-up attack DMG increases by 15%.",
            "effects": []
        }
    },
    "izumo_gensei_and_takama_divine_realm": {
        "name": "Izumo Gensei and Takama Divine Realm",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/5/5a/Item_Izumo_Gensei_and_Takama_Divine_Realm.png",
        "planar_sphere_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/b/b5/Item_Izumo%27s_Magatsu_no_Morokami.png",
        "link_rope_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/6/66/Item_Izumo%27s_Blades_of_Origin_and_End.png",
        "two_piece_bonus": {
            "description": "Increases the wearer's ATK by 12%. When entering battle, if at least one other ally follows the same Path as the wearer, then the wearer's CRIT Rate increases by 12%.",
            "effects": []
        }
    },
    "lushaka,_the_sunken_seas": {
        "name": "Lushaka, the Sunken Seas",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/6/6b/Item_Lushaka%2C_the_Sunken_Seas.png",
        "planar_sphere_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/6/66/Item_Lushaka%27s_Waterscape.png",
        "link_rope_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/e/eb/Item_Lushaka%27s_Twinlanes.png",
        "two_piece_bonus": {
            "description": "Increases the wearer's Energy Regeneration Rate by 5%. If the wearer is not the first character in the team lineup, then increases the ATK of the first character in the team lineup by 12%.",
            "effects": []
        }
    },
    "pan-cosmic_commercial_enterprise": {
        "name": "Pan-Cosmic Commercial Enterprise",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/9/92/Item_Pan-Cosmic_Commercial_Enterprise.png",
        "planar_sphere_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/7/7f/Item_The_IPC%27s_Mega_HQ.png",
        "link_rope_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/4/47/Item_The_IPC%27s_Trade_Route.png",
        "two_piece_bonus": {
            "description": "Increases the wearer's Effect Hit Rate by 10%. Meanwhile, the wearer's ATK increases by an amount that is equal to 25% of the current Effect Hit Rate, up to a maximum of 25%.",
            "effects": []
        }
    },
    "penacony,_land_of_the_dreams": {
        "name": "Penacony, Land of the Dreams",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/2/21/Item_Penacony%2C_Land_of_the_Dreams.png",
        "planar_sphere_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/8/8d/Item_Penacony%27s_Grand_Hotel.png",
        "link_rope_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/1/13/Item_Penacony%27s_Dream-Seeking_Tracks.png",
        "two_piece_bonus": {
            "description": "Increases wearer's Energy Regeneration Rate by 5%. Increases DMG by 10% for all other allies that are of the same Type as the wearer.",
            "effects": []
        }
    },
    "rutilant_arena": {
        "name": "Rutilant Arena",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/7/70/Item_Rutilant_Arena.png",
        "planar_sphere_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/f/fb/Item_Taikiyan_Laser_Stadium.png",
        "link_rope_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/5/54/Item_Taikiyan%27s_Arclight_Race_Track.png",
        "two_piece_bonus": {
            "description": "Increases the wearer's CRIT Rate by 8%. When the wearer's current CRIT Rate reaches 70% or higher, the wearer's Basic ATK and Skill DMG increase by 20%.",
            "effects": []
        }
    },
    "sigonia,_the_unclaimed_desolation": {
        "name": "Sigonia, the Unclaimed Desolation",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/d/de/Item_Sigonia%2C_the_Unclaimed_Desolation.png",
        "planar_sphere_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/f/f4/Item_Sigonia%27s_Gaiathra_Berth.png",
        "link_rope_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/8/8f/Item_Sigonia%27s_Knot_of_Cyclicality.png",
        "two_piece_bonus": {
            "description": "Increases the wearer's CRIT Rate by 4%. When an enemy target gets defeated, the wearer's CRIT DMG increases by 4%, stacking up to 10 time(s).",
            "effects": []
        }
    },
    "space_sealing_station": {
        "name": "Space Sealing Station",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/7/78/Item_Space_Sealing_Station.png",
        "planar_sphere_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/d/da/Item_Herta%27s_Space_Station.png",
        "link_rope_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/d/da/Item_Herta%27s_Wandering_Trek.png",
        "two_piece_bonus": {
            "description": "Increases the wearer's ATK by 12%. When the wearer's SPD reaches 120 or higher, the wearer's ATK increases by an extra 12%.",
            "effects": []
        }
    },
    "sprightly_vonwacq": {
        "name": "Sprightly Vonwacq",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/b/b6/Item_Sprightly_Vonwacq.png",
        "planar_sphere_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/e/ea/Item_Vonwacq%27s_Island_of_Birth.png",
        "link_rope_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/f/f1/Item_Vonwacq%27s_Islandic_Coast.png",
        "two_piece_bonus": {
            "description": "Increases the wearer's Energy Regeneration Rate by 5%. When the wearer's SPD reaches 120 or higher, the wearer's action is Advanced Forward by 40% immediately upon entering battle.",
            "effects": []
        }
    },
    "talia:_kingdom_of_banditry": {
        "name": "Talia: Kingdom of Banditry",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/9/92/Item_Talia_Kingdom_of_Banditry.png",
        "planar_sphere_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/8/84/Item_Talia%27s_Nailscrap_Town.png",
        "link_rope_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/f/fc/Item_Talia%27s_Exposed_Electric_Wire.png",
        "two_piece_bonus": {
            "description": "Increases the wearer's Break Effect by 16%. When the wearer's SPD reaches 145 or higher, the wearer's Break Effect increases by an extra 20%.",
            "effects": []
        }
    },
    "the_wondrous_bananamusement_park": {
        "name": "The Wondrous BananAmusement Park",
        "set_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/b/b1/Item_The_Wondrous_BananAmusement_Park.png",
        "planar_sphere_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/0/06/Item_BananAmusement_Park%27s_Memetic_Cables.png",
        "link_rope_icon_url": "https://static.wikia.nocookie.net/houkai-star-rail/images/8/8e/Item_BananAmusement_Park%27s_BananAxis_Plaza.png",
        "two_piece_bonus": {
            "description": "Increases the wearer's CRIT DMG by 16%. When a target summoned by the wearer is on the field, CRIT DMG additionally increases by 32%.",
            "effects": []
        }
    }
}
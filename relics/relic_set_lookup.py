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
        }, # <--- you are here
        "four_piece_bonus": {
            "description": "When the wearer is hit or has their HP consumed by an ally or themselves, their CRIT Rate increases by 8% for 2 turn(s) and up to 2 stacks.",
            "effects": {
                "on_hp_loss": {
                    "type": "crit_rate",
                    "stackable": True,
                    "stack_value": 0.08,
                    "max_stacks": 2,
                    "duration": 2
                }
            }
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
                "on_ultimate": {
                    "type": "spd",
                    "target": "all",
                    "value": 0.12,
                    "stackable": False,
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
                {"type": "basic_atk", "value": 0.10}
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
            "effects": []
        },
        "four_piece_bonus": {
            "description": "At the start of the battle, immediately regenerates 1 Skill Point.",
            "effects": []
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
            "effects": []
        },
        "four_piece_bonus": {
            "description": "Increases CRIT Rate by 4%. The wearer deals 8%/12% increased CRIT DMG to enemies with at least 2/3 debuffs. After the wearer inflicts a debuff on enemy targets, the aforementioned effects increase by 100%, lasting for 1 turn(s).",
            "effects": []
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
            "effects": []
        },
        "four_piece_bonus": {
            "description": "For every DoT the target enemy is afflicted with, the wearer will ignore 6% of its DEF when dealing DMG to it. This effect is valid for a max of 3 DoTs.",
            "effects": []
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
            "effects": []
        },
        "four_piece_bonus": {
            "description": "When using Skill or Ultimate on one ally target, increases the ability target's CRIT DMG by 18%, lasting for 2 turn(s). This effect can stack up to 2 time(s).",
            "effects": []
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
            "effects": []
        },
        "four_piece_bonus": {
            "description": "Increases DMG dealt by Skill and Ultimate by 20%. After using Ultimate, additionally increases the DMG dealt by the next Skill by 25%.",
            "effects": []
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
            "effects": []
        },
        "four_piece_bonus": {
            "description": "When the wearer uses follow-up attacks, increases the wearer's ATK by 6% for every time the follow-up attack deals DMG. This effect can stack up to 8 time(s) and lasts for 3 turn(s). This effect is removed the next time the wearer uses a follow-up attack.",
            "effects": []
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
            "effects": []
        },
        "four_piece_bonus": {
            "description": "Increases the wearer's CRIT Rate by 6%. When the wearer uses a follow-up attack, increases the DMG dealt by Ultimate by 36%, lasting for 1 turn(s).",
            "effects": []
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
            "effects": []
        },
        "four_piece_bonus": {
            "description": "Increases the wearer's Break Effect by 16%. After the wearer inflicts Weakness Break on an enemy, regenerates 3 Energy.",
            "effects": []
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
            "effects": []
        },
        "four_piece_bonus": {
            "description": "When attacking debuffed enemies, the wearer's CRIT Rate increases by 10%, and their CRIT DMG increases by 20% against Imprisoned enemies.",
            "effects": []
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
            "effects": []
        },
        "four_piece_bonus": {
            "description": "When the wearer uses their Ultimate on an ally, all allies' Break Effect increases by 30% for 2 turn(s). This effect cannot be stacked.",
            "effects": []
        }
    }
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
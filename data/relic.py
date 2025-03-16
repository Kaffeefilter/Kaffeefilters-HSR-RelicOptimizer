class Relic:
    def __init__(self, relic_id, category, slot, set_id, mainstat, substats, level, max_level):
        """
        :param relic_id: Eindeutige ID des Relics
        :param category: Typ des Relics ("Cavern Relic" oder "Planar Ornament")
        :param slot: Slot des Relics 
        :param set_id: ID des Relic-Sets
        :param mainstat: Dictionary mit Mainstat-Typ und -Wert {"type": String, "value": Float}
        :param substats: Liste von Dictionaries mit Substat-Details
                         [{"type": String, "value": Float, "lvl": Int, "efficiency": Float}]
        :param level: Aktuelles Level des Relics
        :param max_level: Maximal erreichbares Level
        """
        self.relic_id = relic_id
        self.category = category
        self.slot = slot
        self.set_id = set_id
        self.mainstat = mainstat
        self.substats = substats
        self.level = level
        self.max_level = max_level

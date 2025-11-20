import os
import random
from typing import Optional, List
import importlib.resources as resources

class RandomUserAgent():

    def __init__(self, file_w_agents: Optional[str] = None):
        self._user_filename = file_w_agents
        self._base_filename = "agents.txt"


    def _load_agents(self) -> List[str]:
        if self._user_filename:
            if os.path.exists(self._user_filename):
                with open(self._user_filename, "r", encoding="utf-8") as f:
                    return [line.strip() for line in f if line.strip()]

        with resources.files(__package__).joinpath(self._base_filename).open("r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]

    
    def get_random_desktop_agent(self, macOS: bool = True, 
                                 windows: bool = True, 
                                 linux: bool = True) -> str:

        agents: List[str] = self._load_agents()

        if not agents:
            raise RuntimeError("Agents not loaded!")

        while True:
            random_idx: int = random.randint(0, len(agents) - 1)
            value: str = agents[random_idx]

            if "Android" in value or "CriOS" in value:
                continue

            if not macOS and "Macintosh" in value:
                continue
            elif not windows and "Windows" in value:
                continue
            elif not linux and "Linux" in value:
                continue

            return value
    

    def get_random_mobile_agent(self, android: bool = True, ios: bool = True) -> str:
        agents: List[str] = self._load_agents()

        if not agents:
            raise RuntimeError("Agents not loaded!")

        while True:
            random_idx: int = random.randint(0, len(agents) - 1)
            value: str = agents[random_idx]

            if "Windows" in value or "Macintosh" in value or ("Linux" in value and "Android" not in value):
                continue

            if not android and "Android" in value:
                continue
            elif not ios and "CriOS" in value:
                continue

            return value


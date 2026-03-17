class SignalParser:

    def parse(self, text: str) -> str:
        text = text.lower()

        # DSA 
        if "dsa" in text or "data structure" in text:
            return "dsa_practice"
        
        # Hackathon
        if "hackathon" in text:
            return "hackathon_team"
        
        # Startup
        if "startup" in text or "cofounder" in text:
            return "startup_build"
        
        # Backend
        if "backend" in text:
            return "backend_collab"
        
        return "general"
    
signal_parser = SignalParser()

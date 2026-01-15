"""
Base class for AI providers.
All provider-specific code should inherit from this.
"""

class AIProvider:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def analyze(self, code: str):
        """
        Analyze code using AI provider.
        Must be implemented in subclasses.
        """
        raise NotImplementedError("Subclasses must implement analyze method.")

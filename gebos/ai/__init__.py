"""
AI Engine Module - Core AI/ML capabilities for GEBOS

Integrates all AI components:
- Predictive Analytics
- Natural Language Processing
- Automation Engine
- Recommendation System
"""

from .predictive import PredictiveAnalytics
from .nlp import NLPEngine
from .automation import AutomationEngine
from .recommendations import RecommendationEngine

__all__ = [
    'AIEngine',
    'PredictiveAnalytics',
    'NLPEngine',
    'AutomationEngine',
    'RecommendationEngine'
]


class AIEngine:
    """
    Central AI engine coordinating all AI/ML capabilities in GEBOS.
    """
    
    def __init__(self, gebos_instance):
        """
        Initialize AI Engine with all sub-components.
        
        Args:
            gebos_instance: Reference to main GEBOS instance
        """
        self.gebos = gebos_instance
        
        # Initialize AI sub-components
        self.predictive = PredictiveAnalytics(self)
        self.nlp = NLPEngine(self)
        self.automation = AutomationEngine(self)
        self.recommendations = RecommendationEngine(self)
        
    def initialize_models(self):
        """Load and initialize all AI/ML models."""
        self.predictive.load_models()
        self.nlp.load_models()
        
    def train_models(self, training_data):
        """Train or retrain AI models with new data."""
        self.predictive.train(training_data)
        self.nlp.train(training_data)

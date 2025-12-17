"""
GEBOS - Gerege Business Operation System
AI-Driven Enterprise Resource Planning System
Version 1.0.0
"""

__version__ = "1.0.0"
__author__ = "Gerege Core Development Team"

from .core import Finance, HR, Inventory, Sales, Production
from .ai import AIEngine, PredictiveAnalytics, NLPEngine, AutomationEngine


class GEBOS:
    """
    Main GEBOS ERP System class integrating all modules with AI capabilities.
    
    This is the central hub for accessing all ERP functionalities enhanced
    with AI-driven features.
    """
    
    def __init__(self, config=None):
        """
        Initialize GEBOS with optional configuration.
        
        Args:
            config (dict, optional): Configuration dictionary for system setup
        """
        self.config = config or {}
        
        # Initialize core ERP modules
        self.finance = Finance(self)
        self.hr = HR(self)
        self.inventory = Inventory(self)
        self.sales = Sales(self)
        self.production = Production(self)
        
        # Initialize AI engine
        self.ai = AIEngine(self)
        
    def query(self, natural_language_query):
        """
        Process natural language queries using AI.
        
        Args:
            natural_language_query (str): Question or command in natural language
            
        Returns:
            dict: Processed result with data and insights
        """
        return self.ai.nlp.process_query(natural_language_query)
    
    def predict(self, metric, timeframe, **kwargs):
        """
        Make predictions using AI models.
        
        Args:
            metric (str): The metric to predict (revenue, sales, demand, etc.)
            timeframe (str): Prediction timeframe
            **kwargs: Additional parameters for prediction
            
        Returns:
            dict: Prediction results with confidence intervals
        """
        # Route to appropriate prediction method based on metric
        metric_methods = {
            'revenue': self.ai.predictive.predict_revenue,
            'sales': self.ai.predictive.predict_sales,
            'demand': lambda timeframe, **kw: self.ai.predictive.predict_demand(
                kw.get('product_id', 'default'), timeframe
            ),
            'churn': self.ai.predictive.predict_churn,
            'cash_flow': lambda timeframe, **kw: self.ai.predictive.predict_cash_flow(
                months=kw.get('months', 3)
            ),
        }
        
        method = metric_methods.get(metric.lower())
        if method:
            return method(timeframe, **kwargs)
        else:
            return {'error': f'Unknown metric: {metric}'}
    
    def automate(self, workflow_name, **params):
        """
        Execute automated workflows with AI decision-making.
        
        Args:
            workflow_name (str): Name of the workflow to execute
            **params: Workflow parameters
            
        Returns:
            dict: Workflow execution results
        """
        return self.ai.automation.execute(workflow_name, **params)


__all__ = [
    'GEBOS',
    'Finance',
    'HR',
    'Inventory',
    'Sales',
    'Production',
    'AIEngine',
    'PredictiveAnalytics',
    'NLPEngine',
    'AutomationEngine',
]

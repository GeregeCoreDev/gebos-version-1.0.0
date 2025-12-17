"""
Unit tests for GEBOS core functionality
"""

import pytest
from gebos import GEBOS


class TestGEBOSCore:
    """Test suite for GEBOS core functionality"""
    
    def setup_method(self):
        """Set up test fixtures"""
        self.erp = GEBOS()
    
    def test_gebos_initialization(self):
        """Test GEBOS initialization"""
        assert self.erp is not None
        assert hasattr(self.erp, 'finance')
        assert hasattr(self.erp, 'hr')
        assert hasattr(self.erp, 'inventory')
        assert hasattr(self.erp, 'sales')
        assert hasattr(self.erp, 'production')
        assert hasattr(self.erp, 'ai')
    
    def test_natural_language_query(self):
        """Test natural language query processing"""
        result = self.erp.query("What were our top products?")
        assert 'intent' in result
        assert 'result' in result
        assert 'confidence' in result
        assert isinstance(result['confidence'], float)
    
    def test_revenue_forecast(self):
        """Test revenue forecasting"""
        forecast = self.erp.finance.forecast_revenue('next_quarter')
        assert 'forecast' in forecast
        assert 'predicted_revenue' in forecast['forecast']
        assert forecast['forecast']['predicted_revenue'] > 0
    
    def test_demand_forecast(self):
        """Test demand forecasting"""
        demand = self.erp.inventory.forecast_demand('PROD-001', 'next_month')
        assert 'forecast' in demand
        assert 'predicted_units' in demand['forecast']
        assert demand['forecast']['predicted_units'] > 0
    
    def test_lead_scoring(self):
        """Test lead scoring functionality"""
        leads = [
            {'id': 'L001', 'company': 'Test Corp'},
            {'id': 'L002', 'company': 'Example Inc'}
        ]
        scored = self.erp.sales.score_leads(leads)
        assert len(scored) == 2
        assert all('score' in lead for lead in scored)
        assert all('priority' in lead for lead in scored)
    
    def test_sentiment_analysis(self):
        """Test sentiment analysis"""
        feedback = [
            {'text': 'Great product!'},
            {'text': 'Very satisfied'}
        ]
        sentiment = self.erp.ai.nlp.analyze_sentiment(feedback)
        assert 'overall_sentiment' in sentiment
        assert 'distribution' in sentiment
        assert sentiment['overall_sentiment'] in ['positive', 'negative', 'neutral']
    
    def test_predictive_maintenance(self):
        """Test predictive maintenance"""
        maintenance = self.erp.production.predict_maintenance('MACHINE-001')
        assert 'next_maintenance' in maintenance
        assert 'failure_probability' in maintenance['next_maintenance']
    
    def test_workflow_automation(self):
        """Test workflow automation"""
        result = self.erp.automate('test_workflow', param='value')
        assert 'workflow' in result
        assert 'status' in result


class TestAIEngine:
    """Test suite for AI engine"""
    
    def setup_method(self):
        """Set up test fixtures"""
        self.erp = GEBOS()
        self.ai = self.erp.ai
    
    def test_predictive_analytics(self):
        """Test predictive analytics"""
        revenue = self.ai.predictive.predict_revenue('next_quarter')
        assert 'predicted_revenue' in revenue
        assert revenue['confidence_level'] == 0.95
    
    def test_nlp_intent_detection(self):
        """Test NLP intent detection"""
        result = self.ai.nlp.process_query("Show me sales data")
        assert 'intent' in result
        assert 'entities' in result
    
    def test_automation_workflow_creation(self):
        """Test automation workflow creation"""
        workflow = self.ai.automation.create_workflow(
            name='test_workflow',
            steps=[{'name': 'step1', 'type': 'action'}],
            ai_enabled=True
        )
        assert workflow['name'] == 'test_workflow'
        assert workflow['ai_enabled'] is True
        assert workflow['status'] == 'active'
    
    def test_recommendations(self):
        """Test recommendation engine"""
        recs = self.ai.recommendations.recommend_products(
            customer_id='CUST-001',
            context={}
        )
        assert isinstance(recs, list)
        assert all('score' in rec for rec in recs)


class TestFinanceModule:
    """Test suite for Finance module"""
    
    def setup_method(self):
        """Set up test fixtures"""
        self.erp = GEBOS()
        self.finance = self.erp.finance
    
    def test_cash_flow_prediction(self):
        """Test cash flow prediction"""
        cash_flow = self.finance.predict_cash_flow(months_ahead=3)
        assert 'predictions' in cash_flow
        assert len(cash_flow['predictions']) == 3
    
    def test_anomaly_detection(self):
        """Test anomaly detection"""
        transactions = [
            {'id': 'T001', 'amount': 1000},
            {'id': 'T002', 'amount': 2000}
        ]
        anomalies = self.finance.detect_anomalies(transactions)
        assert isinstance(anomalies, list)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])

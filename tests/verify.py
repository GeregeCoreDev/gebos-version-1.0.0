#!/usr/bin/env python3
"""
Simple verification script for GEBOS without external dependencies
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from gebos import GEBOS


def test_basic_functionality():
    """Test basic GEBOS functionality"""
    print("Testing GEBOS Basic Functionality")
    print("=" * 60)
    
    # Initialize
    print("\n1. Initializing GEBOS...")
    erp = GEBOS()
    print("   ✓ GEBOS initialized successfully")
    
    # Test modules
    print("\n2. Testing core modules...")
    modules = ['finance', 'hr', 'inventory', 'sales', 'production', 'ai']
    for module in modules:
        assert hasattr(erp, module), f"Missing module: {module}"
        print(f"   ✓ {module.capitalize()} module available")
    
    # Test NLP query
    print("\n3. Testing natural language query...")
    result = erp.query("Test query")
    assert 'intent' in result
    assert 'result' in result
    print("   ✓ NLP query processing works")
    
    # Test revenue forecast
    print("\n4. Testing revenue forecasting...")
    forecast = erp.finance.forecast_revenue('next_quarter')
    assert 'forecast' in forecast
    assert 'predicted_revenue' in forecast['forecast']
    print(f"   ✓ Revenue forecast: ${forecast['forecast']['predicted_revenue']:,.2f}")
    
    # Test lead scoring
    print("\n5. Testing lead scoring...")
    leads = [{'id': 'L001', 'company': 'Test Corp'}]
    scored = erp.sales.score_leads(leads)
    assert len(scored) == 1
    assert 'score' in scored[0]
    print(f"   ✓ Lead scored: {scored[0]['score']:.2f}")
    
    # Test demand forecasting
    print("\n6. Testing demand forecasting...")
    demand = erp.inventory.forecast_demand('PROD-001', 'next_month')
    assert 'forecast' in demand
    print(f"   ✓ Demand forecast: {demand['forecast']['predicted_units']} units")
    
    # Test sentiment analysis
    print("\n7. Testing sentiment analysis...")
    feedback = [{'text': 'Great product!'}]
    sentiment = erp.ai.nlp.analyze_sentiment(feedback)
    assert 'overall_sentiment' in sentiment
    print(f"   ✓ Sentiment: {sentiment['overall_sentiment']}")
    
    # Test predictive maintenance
    print("\n8. Testing predictive maintenance...")
    maintenance = erp.production.predict_maintenance('MACHINE-001')
    assert 'next_maintenance' in maintenance
    print(f"   ✓ Maintenance prediction available")
    
    # Test automation
    print("\n9. Testing workflow automation...")
    result = erp.automate('test_workflow')
    assert 'status' in result
    print(f"   ✓ Workflow executed: {result['status']}")
    
    print("\n" + "=" * 60)
    print("All tests passed! ✓")
    print("=" * 60)
    return True


if __name__ == "__main__":
    try:
        test_basic_functionality()
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

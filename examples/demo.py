#!/usr/bin/env python3
"""
GEBOS Demo Script

Demonstrates AI-driven ERP capabilities
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from gebos import GEBOS


def print_section(title):
    """Print formatted section header"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def main():
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║   GEBOS - AI-Driven ERP System Demo                      ║
    ║   Gerege Business Operation System v1.0.0                ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    # Initialize GEBOS
    print("Initializing GEBOS...")
    erp = GEBOS()
    print("✓ GEBOS initialized successfully!\n")
    
    # 1. Natural Language Query
    print_section("1. Natural Language Processing")
    query = "What were our top 5 products last month?"
    print(f"Query: '{query}'")
    result = erp.query(query)
    print(f"Intent detected: {result['intent']}")
    print(f"Confidence: {result['confidence']:.1%}")
    if 'data' in result['result']:
        print(f"Found {len(result['result']['data'])} products")
    print(f"Result: {result['result'].get('summary', 'Data retrieved successfully')}")
    
    # 2. Revenue Forecasting
    print_section("2. Predictive Analytics - Revenue Forecast")
    forecast = erp.finance.forecast_revenue('next_quarter', confidence_level=0.95)
    pred = forecast['forecast']
    print(f"Predicted Revenue: ${pred['predicted_revenue']:,.2f}")
    print(f"Confidence Range: ${pred['lower_bound']:,.2f} - ${pred['upper_bound']:,.2f}")
    print(f"Trend: {pred['trend']}")
    print(f"Key Factors: {', '.join(pred['factors'])}")
    
    # 3. Sales Lead Scoring
    print_section("3. AI-Powered Lead Scoring")
    sample_leads = [
        {'id': 'L001', 'company': 'TechCorp', 'budget': 100000, 'engagement': 'high'},
        {'id': 'L002', 'company': 'SmallBiz', 'budget': 5000, 'engagement': 'low'},
        {'id': 'L003', 'company': 'MegaInc', 'budget': 500000, 'engagement': 'medium'}
    ]
    
    scored_leads = erp.sales.score_leads(sample_leads)
    print("\nTop 3 Leads:")
    for i, lead in enumerate(scored_leads[:3], 1):
        print(f"{i}. {lead['lead']['company']}")
        print(f"   Score: {lead['score']:.2f} | Priority: {lead['priority']}")
        print(f"   Conversion Probability: {lead['conversion_probability']:.1%}")
        print(f"   Actions: {', '.join(lead['recommended_actions'])}\n")
    
    # 4. Demand Forecasting
    print_section("4. Inventory - Demand Forecasting")
    demand = erp.inventory.forecast_demand('PROD-001', 'next_month')
    forecast_data = demand['forecast']
    print(f"Product: {forecast_data['product_id']}")
    print(f"Predicted Demand: {forecast_data['predicted_units']} units")
    print(f"Confidence: {forecast_data['confidence']:.1%}")
    print(f"Trend: {forecast_data['trend']}")
    print(f"Peak Periods: {', '.join(forecast_data['peak_periods'])}")
    
    # 5. Customer Sentiment Analysis
    print_section("5. Customer Sentiment Analysis")
    sample_feedback = [
        {'text': 'Great product! Very satisfied with the quality.'},
        {'text': 'Shipping was a bit slow, but overall good experience.'},
        {'text': 'Excellent customer service and fast delivery!'},
        {'text': 'Product met my expectations.'}
    ]
    
    sentiment = erp.sales.analyze_customer_sentiment(
        customer_id='CUST-001',
        interactions=sample_feedback
    )
    
    print(f"Overall Sentiment: {sentiment['sentiment']['overall_sentiment']}")
    dist = sentiment['sentiment']['distribution']
    print(f"Distribution:")
    print(f"  Positive: {dist['positive']:.1%}")
    print(f"  Neutral: {dist['neutral']:.1%}")
    print(f"  Negative: {dist['negative']:.1%}")
    print(f"\nKey Insights:")
    for insight in sentiment['sentiment']['key_insights']:
        print(f"  • {insight}")
    
    # 6. Predictive Maintenance
    print_section("6. Production - Predictive Maintenance")
    maintenance = erp.production.predict_maintenance('MACHINE-001')
    next_maint = maintenance['next_maintenance']
    print(f"Equipment: {maintenance['equipment_id']}")
    print(f"Next Maintenance: {next_maint['next_maintenance_date'][:10]}")
    print(f"Failure Probability: {next_maint['failure_probability']:.1%}")
    print(f"Recommended Action: {next_maint['recommended_action']}")
    
    savings = maintenance['cost_savings']
    print(f"\nCost Savings:")
    print(f"  Predictive: ${savings['predictive_cost']:,}")
    print(f"  Reactive: ${savings['reactive_cost']:,}")
    print(f"  Savings: ${savings['savings']:,}")
    
    # 7. HR - Performance Prediction
    print_section("7. HR - Employee Performance Prediction")
    performance = erp.hr.predict_performance('EMP-123', 'next_quarter')
    pred_perf = performance['predicted_performance']
    print(f"Employee: {performance['employee_id']}")
    print(f"Predicted Rating: {pred_perf['predicted_rating']:.1f}/5.0")
    print(f"Confidence: {pred_perf['confidence']:.1%}")
    print(f"\nStrengths: {', '.join(pred_perf['strengths'])}")
    print(f"Improvement Areas: {', '.join(pred_perf['improvement_areas'])}")
    print(f"\nDevelopment Recommendations:")
    for rec in performance['development_recommendations']:
        print(f"  • {rec}")
    
    # 8. Automated Workflow
    print_section("8. Intelligent Automation - Workflow")
    workflow_result = erp.automate(
        'invoice_processing',
        invoice_id='INV-001'
    )
    print(f"Workflow: {workflow_result['workflow']}")
    print(f"Status: {workflow_result['status']}")
    print(f"Steps Executed: {workflow_result['steps_executed']}")
    print(f"Duration: {workflow_result['duration']}")
    
    # Summary
    print_section("Demo Summary")
    print("""
    ✓ Natural Language Processing - Query understanding
    ✓ Predictive Analytics - Revenue forecasting
    ✓ Sales Optimization - Lead scoring
    ✓ Inventory Management - Demand forecasting
    ✓ Customer Insights - Sentiment analysis
    ✓ Production Optimization - Predictive maintenance
    ✓ HR Analytics - Performance prediction
    ✓ Workflow Automation - Intelligent processes
    
    GEBOS successfully demonstrated AI-driven ERP capabilities!
    """)
    
    print("\n" + "=" * 60)
    print("  For more information, visit: https://github.com/GeregeCoreDev/gebos-version-1.0.0")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()

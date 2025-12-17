# Getting Started with GEBOS

## Overview

GEBOS (Gerege Business Operation System) is an AI-driven Enterprise Resource Planning system that revolutionizes business operations through intelligent automation, predictive analytics, and natural language processing.

## Prerequisites

- Python 3.9 or higher
- PostgreSQL 13 or higher
- Redis 6 or higher
- MongoDB 5 or higher (optional)
- 8GB RAM minimum (16GB recommended for AI features)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/GeregeCoreDev/gebos-version-1.0.0.git
cd gebos-version-1.0.0
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv

# On Linux/Mac
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
cp .env.example .env
# Edit .env with your configuration
```

### 5. Initialize Database

```bash
# Create database
createdb gebos

# Run migrations (when available)
python manage.py migrate
```

### 6. Download AI Models

```bash
# Download pre-trained models
python scripts/download_models.py
```

## Quick Start

### Basic Usage

```python
from gebos import GEBOS

# Initialize GEBOS
erp = GEBOS()

# Use natural language queries
result = erp.query("What were our top 5 products last month?")
print(result)

# Get AI predictions
forecast = erp.predict('revenue', 'next_quarter')
print(f"Predicted revenue: ${forecast['predicted_revenue']:,.2f}")

# Analyze customer sentiment
sentiment = erp.sales.analyze_customer_sentiment(
    customer_id='CUST-001',
    interactions=[{'text': 'Great product and service!'}]
)
print(f"Customer sentiment: {sentiment['sentiment']}")
```

### Running the API Server

```bash
# Development mode
uvicorn gebos.api.main:app --reload --host 0.0.0.0 --port 8000

# Production mode
gunicorn gebos.api.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

### API Examples

```bash
# Get revenue forecast
curl http://localhost:8000/api/v1/finance/forecast/revenue?period=next_quarter

# Natural language query
curl -X POST http://localhost:8000/api/v1/query \
  -H "Content-Type: application/json" \
  -d '{"query": "Show me sales trends for last month"}'

# Predict customer churn
curl http://localhost:8000/api/v1/sales/churn/predict
```

## Core Features

### 1. Finance & Accounting

```python
# Revenue forecasting
forecast = erp.finance.forecast_revenue('next_quarter', confidence_level=0.95)

# Anomaly detection
anomalies = erp.finance.detect_anomalies(transactions)

# Cash flow prediction
cash_flow = erp.finance.predict_cash_flow(months_ahead=6)
```

### 2. Human Resources

```python
# Intelligent candidate matching
matches = erp.hr.match_candidates(job_requirements, candidate_pool)

# Performance prediction
performance = erp.hr.predict_performance('EMP-123', 'next_quarter')

# Sentiment analysis
sentiment = erp.hr.analyze_sentiment(feedback_data)
```

### 3. Inventory Management

```python
# Demand forecasting
demand = erp.inventory.forecast_demand('PROD-001', 'next_month')

# Automated reordering
reorder_plan = erp.inventory.optimize_reordering(inventory_levels)

# Supply chain risk assessment
risk = erp.inventory.assess_supply_chain_risk(suppliers)
```

### 4. Sales & CRM

```python
# Lead scoring
scored_leads = erp.sales.score_leads(leads)

# Sales forecasting
sales_forecast = erp.sales.forecast_sales('next_quarter')

# Churn prediction
churn_analysis = erp.sales.predict_churn()
```

### 5. Production Planning

```python
# Optimize production schedule
schedule = erp.production.optimize_schedule(orders, resources)

# Predictive maintenance
maintenance = erp.production.predict_maintenance('MACHINE-001')

# Quality prediction
quality = erp.production.predict_quality(production_parameters)
```

## AI Features

### Natural Language Processing

```python
# Ask questions in natural language
result = erp.query("What are our best-selling products this quarter?")

# Sentiment analysis
sentiment = erp.ai.nlp.analyze_sentiment(customer_feedback)

# Text classification
category = erp.ai.nlp.classify_text(document, categories)
```

### Predictive Analytics

```python
# Revenue forecasting
revenue_forecast = erp.ai.predictive.predict_revenue('next_quarter')

# Demand forecasting
demand_forecast = erp.ai.predictive.predict_demand('PROD-001', 'next_month')

# Churn prediction
churn_risk = erp.ai.predictive.predict_churn('premium_customers')
```

### Intelligent Automation

```python
# Create automated workflow
erp.ai.automation.create_workflow(
    name='Invoice Processing',
    steps=[
        {'name': 'validate', 'type': 'validation'},
        {'name': 'approve', 'type': 'decision'},
        {'name': 'process', 'type': 'action'}
    ],
    ai_enabled=True
)

# Execute workflow
result = erp.automate('Invoice Processing', invoice_id='INV-001')
```

## Configuration

### AI Model Configuration

Edit `gebos/config/ai_config.yaml`:

```yaml
predictive_analytics:
  revenue_model:
    type: time_series
    algorithm: LSTM
    confidence_threshold: 0.8
    
nlp:
  model: distilbert-base-uncased
  max_length: 512
  batch_size: 32
```

### Database Configuration

Edit `.env`:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/gebos
MONGODB_URL=mongodb://localhost:27017/gebos
REDIS_URL=redis://localhost:6379/0
```

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=gebos --cov-report=html

# Run specific module tests
pytest tests/test_finance.py
pytest tests/test_ai.py
```

## Deployment

### Docker Deployment

```bash
# Build image
docker build -t gebos:1.0.0 .

# Run container
docker run -p 8000:8000 \
  -e DATABASE_URL=postgresql://... \
  gebos:1.0.0
```

### Kubernetes Deployment

```bash
kubectl apply -f deployment/kubernetes/
```

## Monitoring

### Metrics

Access Prometheus metrics at `http://localhost:9090/metrics`

### Logs

```bash
# View logs
tail -f logs/gebos.log

# With log rotation
logrotate gebos-logrotate.conf
```

## Troubleshooting

### Common Issues

1. **AI models not loading**
   - Run `python scripts/download_models.py`
   - Check `AI_MODEL_PATH` in `.env`

2. **Database connection errors**
   - Verify PostgreSQL is running
   - Check `DATABASE_URL` in `.env`

3. **Memory issues with AI features**
   - Reduce batch sizes
   - Disable unused AI features
   - Increase system RAM

## Next Steps

- Read the [AI Features Guide](ai-features.md)
- Check the [API Reference](api-reference.md)
- Review [Configuration Options](configuration.md)
- See [Deployment Guide](deployment.md)

## Support

- Documentation: https://docs.gebos.io
- Community Forum: https://community.gebos.io
- Email: support@gebos.io
- GitHub Issues: https://github.com/GeregeCoreDev/gebos-version-1.0.0/issues

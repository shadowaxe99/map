```python
import json

# Assuming adPerformanceMetrics is a JSON string
adPerformanceMetrics = '{"impressions": 1000, "clicks": 100, "conversions": 10}'

def trackPerformance(adPerformanceMetrics):
    metrics = json.loads(adPerformanceMetrics)
    impressions = metrics['impressions']
    clicks = metrics['clicks']
    conversions = metrics['conversions']
    
    clickThroughRate = (clicks / impressions) * 100
    conversionRate = (conversions / clicks) * 100
    
    return clickThroughRate, conversionRate

def generateReport(clickThroughRate, conversionRate):
    report = f"Click Through Rate: {clickThroughRate}%\nConversion Rate: {conversionRate}%"
    return report

def displayReport(report, performanceReport):
    performanceReport.innerHTML = report

clickThroughRate, conversionRate = trackPerformance(adPerformanceMetrics)
report = generateReport(clickThroughRate, conversionRate)
displayReport(report, performanceReport)
```
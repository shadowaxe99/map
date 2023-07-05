```python
import requests
from src.nlp_models import analyzeUserInput

class API:
    def __init__(self, base_url):
        self.base_url = base_url

    def retrieveAdContent(self, ad_id):
        response = requests.get(f"{self.base_url}/ads/{ad_id}")
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def deliverAd(self, adContent, userPreferences):
        userContext = analyzeUserInput(userPreferences)
        payload = {
            "adContent": adContent,
            "userContext": userContext
        }
        response = requests.post(f"{self.base_url}/deliverAd", json=payload)
        return response.status_code == 200

    def trackAdPerformance(self, ad_id):
        response = requests.get(f"{self.base_url}/ads/{ad_id}/performance")
        if response.status_code == 200:
            return response.json()
        else:
            return None

class AdAPI(API):
    def __init__(self, base_url):
        super().__init__(base_url)

    def updateAd(self, ad_id, adContent):
        payload = {
            "adContent": adContent
        }
        response = requests.put(f"{self.base_url}/ads/{ad_id}", json=payload)
        return response.status_code == 200

class PublisherAPI(API):
    def __init__(self, base_url):
        super().__init__(base_url)

    def getAdPerformance(self, ad_id):
        return self.trackAdPerformance(ad_id)
```

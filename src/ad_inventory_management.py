```python
import json

class AdInventoryManager:
    def __init__(self):
        self.adInventory = []

    def load_inventory(self, inventory_file):
        with open(inventory_file, 'r') as file:
            self.adInventory = json.load(file)

    def monitor_available_spaces(self):
        available_spaces = [ad for ad in self.adInventory if ad['status'] == 'available']
        return available_spaces

    def implement_bidding(self, ad_request):
        available_ads = self.monitor_available_spaces()
        matching_ads = [ad for ad in available_ads if ad['targeting_criteria'] == ad_request['targeting_criteria']]
        if matching_ads:
            highest_bid_ad = max(matching_ads, key=lambda x:x['bid'])
            return highest_bid_ad
        else:
            return None

    def allocate_ad_slot(self, ad_request):
        winning_ad = self.implement_bidding(ad_request)
        if winning_ad:
            winning_ad['status'] = 'allocated'
            return winning_ad
        else:
            return None

    def update_inventory(self, inventory_file):
        with open(inventory_file, 'w') as file:
            json.dump(self.adInventory, file)

if __name__ == "__main__":
    manager = AdInventoryManager()
    manager.load_inventory('ad_inventory.json')
    ad_request = {
        'targeting_criteria': 'sports',
        'userPreferences': 'soccer'
    }
    allocated_ad = manager.allocate_ad_slot(ad_request)
    manager.update_inventory('ad_inventory.json')
```
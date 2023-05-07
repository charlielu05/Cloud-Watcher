import boto3
from typing import Protocol
from dataclasses import dataclass

@dataclass
class Costs:
    costs: object
    
class CloudCost(Protocol):
    # cloud sdk client
    client: object
    
    def get_costs(self)->dict:
        ...

class AWSCost:
    def __init__(self) -> None:
        self.client = boto3.client('ce')    
    
    def get_costs(self, start_date:str, end_date:str)->dict:
        response = self.client.get_cost_and_usage(
            TimePeriod={
            'Start': start_date,
            'End': end_date,
            },
            Filter = { 
                'Not': { 
                    'Dimensions': {
                        'Key': "RECORD_TYPE",
                        'Values': ["Refund", "Credit"]
                    }
                },
            },
            Granularity = 'MONTHLY',
            Metrics=[ 'UnblendedCost' ],
            GroupBy=[{"Type": "DIMENSION","Key": "SERVICE"}]
        )
        
        return response
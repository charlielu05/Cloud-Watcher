import boto3
from typing import Protocol
from dataclasses import dataclass
from toolz.dicttoolz import get_in

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
        self.raw_response = self.client.get_cost_and_usage(
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

        return self.raw_response
    
    def _boto_response_filter(self):
        start_date_key =['TimePeriod', 'Start']
        end_date_key = ['TimePeriod', 'End']
        services_key = ['Groups']
        
        self.costs = [{'date_period': (get_in(start_date_key, period), get_in(end_date_key, period)), 
                'services': [(x.get('Keys')[0], get_in(['Metrics', 'UnblendedCost', 'Amount'], x))
                            for x
                            in get_in(services_key, period)]}
                for period
                in self.raw_response.get('ResultsByTime')]
        
        return self.costs
    
    @property
    def costs(self):
        self._boto_response_filter()
        
        return self.costs
from src.domain.user_query import CLIQuery
from src.domain.cloud_costs import AWSCost
import boto3 

def test_cli_query():
    query = CLIQuery(raw_input=" abcd ")
    assert query.return_query() == "abcd" 
    
def test_aws_cloud_cost(monkeypatch):
    def mock_client(*args, **kwargs):
        def mock_return_costs(*args, **kwargs):
            return dict({"foo":"bar"})
        mock_client.get_cost_and_usage = mock_return_costs
        
        return mock_client
    
    monkeypatch.setattr(boto3, 'client', mock_client)
    
    aws_cost = AWSCost()
    assert aws_cost.get_costs(start_date='2022-01-20', end_date="2023-12-10") == {'foo': 'bar'}
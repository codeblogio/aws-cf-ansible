from ansible.plugins.lookup import LookupBase
import boto3

class LookupModule(LookupBase):

  def run(self, terms, inject=None, **kwargs):

    client = boto3.client('ec2', region_name=terms[0])
    azs = [ az['ZoneName'] for az in client.describe_availability_zones()['AvailabilityZones'] ]

    return azs

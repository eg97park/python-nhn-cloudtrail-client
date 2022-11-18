"""
Simple usage of https://docs.toast.com/ko/CloudTrail/ko/api-guide/.
"""
import time
import json

from nhn.client import CloudTrailClient


APP_KEY = 'AAAAAAAAAAAAAAAA'

if __name__ == '__main__':
    print(f'Use appKey={APP_KEY}')

    # Example of specialized NHN CloudTraul API client.
    FROM_EVENT_TIME = int(time.time() * 1000) - 7776000000
    TO_EVENT_TIME = int(time.time() * 1000)

    ct_handler = CloudTrailClient(
        app_key=APP_KEY
    )

    # Get CloudTrail logs.
    query_result = ct_handler.query()
    print(f'{json.dumps(query_result, indent=4, ensure_ascii=False)}')

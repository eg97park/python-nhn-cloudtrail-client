"""
This module provides NHN Cloud CloudTrail API client.
"""
import time
import datetime
import requests


class CloudTrailClient:
    """
    This class is used to make a request to the CloudTrail RESTful API server of NHN Cloud.
    """
    def __init__(self, app_key):
        """
        This function initializes the class with the appKey, url, uri.
        
        Args:
          app_key: The key of API.
        """
        url = 'https://api-cloud-trail.toast.com'
        uri = f'/cloud-trail/v1.0/appkeys/{app_key}/events/search'
        self.full_url = url + uri

    def query(self,
        id_no=None,
        m_member_type=None,
        m_user_code=None,
        m_email_address=None,
        m_id_no=None,
        event_id='*',
        start_date="2022-07-01T00:00:00.000Z",
        end_date=datetime.datetime.fromtimestamp(time.time()).isoformat(timespec='milliseconds') + 'Z',
        p_sort_by='startDate:asc',
        p_limit=1000,
        p_page=0
    ):
        """
        This function sends a request to the CloudTrail API server with the specified specs.

        Args:
          id_no: The ID number of the member.
          m_member_type: The type of member you want to query.
          m_user_code: The user code of the user you want to query.
          m_email_address: The email address of the user.
          m_id_no: The ID number of the member.
          event_id: The ID of the event.
          start_date: The start date of the query.
          end_date: The end date of the time range for the query.
          p_sort_by: The field to sort by.
          p_limit: The number of results to return.
          p_page: The page number of the results to return.

        Returns:
          If result can be parsed by json, return json object.
          If not, return recieved data as text(str).
        """
        body = {}
        if id_no is not None:
            body.update({'idNo': id_no})
        if m_member_type is not None or m_user_code is not None or m_email_address is not None or m_id_no is not None:
            body.update({'member': {}})
            if m_member_type is not None:
                body['member'].update({'memberType': m_member_type})
            if m_user_code is not None:
                body['member'].update({'userCode': m_user_code})
            if m_email_address is not None:
                body['member'].update({'emailAddress': m_email_address})
            if m_id_no is not None:
                body['member'].update({'idNo': m_id_no})

        body.update({'eventId': event_id})
        body.update({'startDate': start_date})
        body.update({'endDate': end_date})
        body.update({'page': {}})
        
        body['page'].update({'sortBy': p_sort_by})
        body['page'].update({'limit': p_limit})
        body['page'].update({'page': p_page})

        result = requests.post(url=self.full_url, json=body)
        try:
            return result.json()
        except ValueError:
            return result.text

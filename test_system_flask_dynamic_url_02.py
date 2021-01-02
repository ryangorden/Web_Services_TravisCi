import requests
#import pytest

def test_get_good_page():
    '''
    Simulate a user navigating to the website with an HTTP GET.
    '''

    get_header = {'Accept': 'text/html'}
    url= 'http://localhost:5000/'
    resp= requests.get(url,headers= get_header, verify=False)
    assert resp.status_code == 200
    assert 'You are at index()' in resp.text


def test_get_bad_page():
    '''
    Simulate a user navigating to an invalid URL with a HTTP GET.
    '''

    get_header= {'Accept': 'text/html'}
    url= 'http://localhost:5000/switches/s5/list_interfaces'
    resp= requests.get(url, headers=get_header, verify=False)
    assert resp.status_code == 404
    assert 'Invalid hostname' in resp.text

#tests/test_uccewrapper.py

from uccewrapper import ucceAPI


def test_ucce_domain():

    """Tests an API call to get UCCE Domain"""

    ucce_api_instance = ucceAPI('<ip/domain>','<username@domain>', '<password>')

    response = ucce_api_instance.activedirectorydomain


    #assert isinstance(response,dict)
    assert response['1'] is not None, "This should be the first associated domain"



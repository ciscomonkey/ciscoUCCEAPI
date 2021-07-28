import requests
from .xmlDict import XmlDictConfig
from xml.etree import cElementTree as ElementTree


class AdministratorModel(object):

    def __init__(self,ucce_session,ucce_path):

        self.ucce_session = ucce_session
        self.ucce_path = ucce_path


    def __repr__(self):
        final_path = self.ccepath + '/administrator/'
        response = self.ucce_session.get(final_path, verify = False)
        print ('getting data from api')
        print (response)
        root = ElementTree.XML(response.text)
        xmldict = XmlDictConfig(root)
        return xmldict

    def get(self,id):

        final_path = self.ccepath + '/administrator/' + id
        response = self.ucce_session.get(final_path, verify = False)
        print ('getting data from api')
        print (response)
        root = ElementTree.XML(response.text)
        xmldict = XmlDictConfig(root)
        return xmldict


class ucceAPI(object):

    def __init__(self,host,username,password):
        self.host = host
        self.ccepath = ('https://%s/unifiedconfig/config'%self.host)

        self.ucce_session = requests.Session()
        self.ucce_session.auth = ( username , password )

        administrator = AdministratorModel(self.ucce_session, self.ccepath)

    def activedirectorydomain(self):

        final_path = self.ccepath + '/activedirectorydomain'
        response = self.ucce_session.get(final_path, verify = False)
        print ('getting data from api')       
        print (response)
        root = ElementTree.XML(response.text)
        xmldict = XmlDictConfig(root)
        return xmldict





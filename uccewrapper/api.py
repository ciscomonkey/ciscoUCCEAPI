import requests
from .xmlDict import XmlDictConfig
from xml.etree import cElementTree as ElementTree




class AdministratorModel(object):

    def __init__(self,ucce_session,ucce_path):

        self.ucce_session = ucce_session
        self.ccepath = ucce_path


    def __call__(self):

        final_path = self.ccepath + '/administrator/'
        response = self.ucce_session.get(final_path, verify = False)
        print ('getting data from api')
        print (response)
        root = ElementTree.XML(response.text)
        xmldict = XmlDictConfig(root)
        return xmldict

    def get(self,id):

        final_path = self.ccepath + '/administrator/' + str(id)
        response = self.ucce_session.get(final_path, verify = False)
        print ('getting data from api')
        print (response)
        root = ElementTree.XML(response.text)
        xmldict = XmlDictConfig(root)
        return xmldict

class AgentModel(object):

    def __init__(self,ucce_session,ucce_path):

        self.ucce_session = ucce_session
        self.ccepath = ucce_path

    def __call__(self):

        final_path = self.ccepath + '/agent/'
        response = self.ucce_session.get(final_path, verify = False)
        print ('getting data from api')
        print (response)
        root = ElementTree.XML(response.text)
        xmldict = XmlDictConfig(root)
        return xmldict

    def get(self,id):

        final_path = self.ccepath + '/agent/' + str(id)
        response = self.ucce_session.get(final_path, verify = False)
        print ('getting data from api')
        print (response)
        root = ElementTree.XML(response.text)
        xmldict = XmlDictConfig(root)
        return xmldict

class SkillGroupModel:

    def __init__(self,ucce_session,ucce_path):

        self.ucce_session = ucce_session
        self.ccepath = ucce_path
        self.skill_group = 1

    def __call__(self):

        final_path = self.ccepath + '/skillgroup'
        response = self.ucce_session.get(final_path, verify = False)
        print ('getting data from api skill group')
        print (response)
        root = ElementTree.XML(response.text)
        xmldict = XmlDictConfig(root)
        return xmldict

    def list(self):

        final_path = self.ccepath + '/skillgroup'
        response = self.ucce_session.get(final_path, verify = False)
        print ('getting data from api')
        print (response)
        root = ElementTree.XML(response.text)
        xmldict = XmlDictConfig(root)
        return xmldict

class PQModel:

    def __init__(self,ucce_session,ucce_path):

        self.ucce_session = ucce_session
        self.ccepath = ucce_path
        self.skill_group = 1

    def __call__(self):

        final_path = self.ccepath + '/precisionqueue'
        response = self.ucce_session.get(final_path, verify = False)
        print ('getting data from precision queue')
        print (response)
        root = ElementTree.XML(response.text)
        xmldict = XmlDictConfig(root)
        return xmldict

    def list(self):

        final_path = self.ccepath + '/precisionqueue'
        response = self.ucce_session.get(final_path, verify = False)
        print ('getting data from api')
        print (response)
        root = ElementTree.XML(response.text)
        xmldict = XmlDictConfig(root)
        return xmldict

    def get(self,id):

        final_path = self.ccepath + '/precisionqueue/' + str(id)
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

        self.administrator = AdministratorModel(self.ucce_session, self.ccepath)
        self.agent = AgentModel(self.ucce_session, self.ccepath)
        self.skill_group = SkillGroupModel(self.ucce_session, self.ccepath)
        self.pqs = PQModel(self.ucce_session, self.ccepath)

    def activedirectorydomain(self):

        final_path = self.ccepath + '/activedirectorydomain'
        response = self.ucce_session.get(final_path, verify = False)
        print ('getting data from api')       
        print (response)
        root = ElementTree.XML(response.text)
        xmldict = XmlDictConfig(root)
        return xmldict





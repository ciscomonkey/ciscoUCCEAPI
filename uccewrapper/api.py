import requests


class ucceAPI(object):

    def __init__(self,host,username,password):
        self.host = host
        self.ccepath = ('https://%s/unifiedconfig/config'%self.host)

        self.ucce_session = requests.Session()
        self.ucce_session.auth = ( username , password )

    def activedirectorydomain(self):

        final_path = self.ccepath + '/activedirectorydomain'
        response = self.ucce_session.get(final_path, verify = False)
        print ('getting data from api')       
        print (response) 
        return response 



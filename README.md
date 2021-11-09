
#code example

from uccewrapper import ucceAPI

def main():

    """Tests API calls to get PCCE/UCCE data"""

    ucce_api_instance = ucceAPI('<ip/domain>','<username@domain>', '<password>')
  
    response = ucce_api_instance.activedirectorydomain()
    admin_list = ucce_api_instance.administrator()
    admin_get =  ucce_api_instance.administrator.get(0)
    agent_list = ucce_api_instance.agent()
    skillgroups = ucce_api_instance.skill_group()
    print ('fetching')
    print (response)
    print ( admin_list )
    print ( admin_get )
    print ( agent_list )
    print (skillgroups)

if __name__ == "__main__":

main()

# -*-  coding:utf-8 -*-
import sys,itchat,datetime,time,requests
reload(sys)
sys.setdefaultencoding('utf-8')

def dataFunc(dataKey):
	serverTarget = 'bingoBiubiu'
	testMember01 = u'万物'
	tuLingKey = '7a5a769ed5184df784066ad9ae26601f' 
	if dataKey == 'Author':returnData = serverTarget
	elif dataKey == 'testMember01':returnData = testMember01
	elif dataKey == 'tuLing':returnData = tuLingKey
	return returnData
def lc():
    print("Finash Login!")
def ec():
    print("exit")
def startupWX():
	'''
	it's used web server.U can login on at the same time. 
	'''
	itchat.auto_login(loginCallback=lc, exitCallback=ec,hotReload=1)
def loginSuss():
	'''
	search friend :bingobiubiu,send message that server is online. 
	'''
	try:
		serverTarget = itchat.search_friends(dataFunc('Author'))
	except:
		serverTarget = [{'UserName':'filehelper'}]
		return
	userName = serverTarget[0]['UserName']
	itchat.send_msg(u'login sussfully! personal assistant is online.',toUserName=userName)
def startupTest():
	try:
		serverTarget = itchat.search_friends(dataFunc('testMember01'))
	except:
		pass
		return
	userName = serverTarget[0]['UserName']
	itchat.send_msg(u'personal assistant is online.\n唠会儿呗',toUserName=userName)
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'  : dataFunc('tuLing'),
        'info'  : msg,
        'userid' : 'skyeKing-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    reply = get_response(msg['Text'])
    return reply or defaultReply
def keepServer():
	itchat.run()
if __name__ == '__main__':
	startupWX()
	loginSuss()
	startupTest()
	keepServer()

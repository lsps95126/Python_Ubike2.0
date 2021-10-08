import json

class cmd_color:
	RED = '\x1b[0;31;40m'
	GREEN = '\x1b[0;32;40m'
	YELLOW = '\x1b[0;33;40m'
	BLUE = '\x1b[0;34;40m'
	MAGENTA = '\x1b[0;35;40m'
	CYAN = '\x1b[0;36;40m'
	WHITE = '\x1b[0;37;40m'
	GREEN_BG = '\x1b[0;37;42m'
	ENDC = '\x1b[0m'


def act_state(st):
	if(st):
		return "運行中"
	else:
		return "關閉"

with open('高雄YOUBIKE2.0公共自行車租賃站.json') as f:
	data = json.load(f)

inf = data['data']['retVal']


print("高雄市Ubike資訊：")
for i in inf:
	print("/------------------------------\\")
	print(cmd_color.WHITE + "站名：\t\t" + i['sna'] + cmd_color.ENDC)
	print(cmd_color.WHITE + "區域：\t\t" + i['sarea'] + cmd_color.ENDC)
	print(cmd_color.WHITE + "位置：\t\t" + i['ar'] + cmd_color.ENDC)
	print(cmd_color.WHITE + "可租借數量：\t" + i['sbi'] + cmd_color.ENDC)
	print(cmd_color.WHITE + "可停放數量：\t" + i['bemp'] + cmd_color.ENDC)
	print(cmd_color.WHITE + "狀態：\t\t" + cmd_color.GREEN_BG + act_state(i['act']) + cmd_color.ENDC)
	print("\\------------------------------/")

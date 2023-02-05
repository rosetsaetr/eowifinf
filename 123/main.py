import re #line:1
import os #line:2
import sys #line:3
def Init ():#line:8
	print ('********************************************',end ='\n')#line:9
	global c #line:10
	c =0 #line:11
	while True :#line:12
		OO000000O000000O0 =input ('是否进行环境配置(y/n):')#line:13
		if OO000000O000000O0 =='y':#line:14
			c =1 #line:15
			break #line:16
		elif OO000000O000000O0 =='n':#line:17
			c =0 #line:18
			break #line:19
		else :#line:20
			print ('输入错误，请重新输入!')#line:21
def deal_qq ():#line:27
	print ('********************************************',end ='\n')#line:28
	print ('该操作会将处理后的qq追加到尚未处理完的qq后面！')#line:29
	OO000O0O0000OO0O0 =open ("/root/mail/qq/qq-information.txt","r",encoding ="utf-8")#line:30
	OO0OOO0OO00OO00OO =open ("/root/mail/qq/qq_deal.txt","a",encoding ="utf-8")#line:31
	for OOOO0OO0O0OOO0000 in OO000O0O0000OO0O0 :#line:33
		if len (OOOO0OO0O0OOO0000 )>35 :#line:34
			OO00OOO000O0O0000 =re .findall ("[1-9][0-9]{7,}",OOOO0OO0O0OOO0000 )#line:35
			if (len (OO00OOO000O0O0000 )==1 ):#line:36
				OO0OOO0OO00OO00OO .write (OO00OOO000O0O0000 [0 ]+"@qq.com"+"\n")#line:37
	OO000O0O0000OO0O0 .close ()#line:38
	OO0OOO0OO00OO00OO .close ()#line:39
	os .remove ("/root/mail/qq/qq-information.txt")#line:40
	os .mknod ("/root/mail/qq/qq-information.txt")#line:41
	print ("qq处理完成!")#line:42
	global u #line:43
	u =0 #line:44
	while True :#line:45
		OOOOOOOOO0OOO00O0 =input ("检查已处理的qq列表(y/n):")#line:46
		if OOOOOOOOO0OOO00O0 =='y':#line:47
			u =1 #line:48
			break #line:49
		elif OOOOOOOOO0OOO00O0 =='n':#line:50
			u =0 #line:51
			break #line:52
		else :#line:53
			print ('输入错误，请重新输入!')#line:54
			continue #line:55
def account ():#line:60
	print ('********************************************',end ='\n')#line:61
	print ('该操作将删除之前账户！')#line:62
	while True :#line:63
		O000O0O0000000O0O =input ('是否创建账户/修改账户(y/n):')#line:64
		global m #line:65
		m =0 #line:66
		OOOOOO00O00O000O0 =open ("/root/mail/cash.txt","w",encoding ="utf-8")#line:67
		if O000O0O0000000O0O =='n':#line:68
			break #line:69
		elif O000O0O0000000O0O =='y':#line:70
			OOOO0O00000O00000 =0 #line:71
			while OOOO0O00000O00000 !=3 :#line:72
				print ('第'+str (OOOO0O00000O00000 +1 )+'个账户:')#line:73
				OO0OO0O000O000000 =input ('username:')#line:74
				O00O0OOO0OOO0OOO0 =input ('passward:')#line:75
				OOOOO0OO0O0OO0O00 =input ('如无误请输入y以继续(y/n):')#line:76
				if OOOOO0OO0O0OO0O00 =='n':#line:77
					print ('重新输入!')#line:78
					continue #line:79
				elif OOOOO0OO0O0OO0O00 =='y':#line:80
					OOOOOO00O00O000O0 .write (OO0OO0O000O000000 +'\n'+O00O0OOO0OOO0OOO0 +'\n')#line:81
					OOOO0O00000O00000 =OOOO0O00000O00000 +1 #line:82
				else :#line:84
					print ('输入错误，请重新输入账号!')#line:85
					continue #line:86
		else :#line:88
			print ('输入错误，请重新输入!')#line:89
			continue #line:90
		m =1 #line:91
		OOOOOO00O00O000O0 .close ()#line:92
		print ('修改成功!')#line:93
		break #line:94
def edit_mail ():#line:99
	print ('********************************************',end ='\n')#line:100
	while True :#line:101
		OO0OO0O000OOO0O0O =input ('继续操作将清空之前邮件内容!(y/n):')#line:102
		if OO0OO0O000OOO0O0O =='y':#line:103
			OO00OOOOO0OO0O0O0 ='a'#line:104
			O00OO0O000OOO0000 ='a'#line:105
			OOO00O0O0O0OO0000 ='a'#line:106
			os .remove ("/root/mail/mail_content1.txt")#line:108
			os .mknod ("/root/mail/mail_content1.txt")#line:109
			os .remove ("/root/mail/mail_content2.txt")#line:110
			os .mknod ("/root/mail/mail_content2.txt")#line:111
			os .remove ("/root/mail/mail_content3.txt")#line:112
			os .mknod ("/root/mail/mail_content3.txt")#line:113
			os .remove ("/root/mail/mail_content1_.txt")#line:114
			os .mknod ("/root/mail/mail_content1_.txt")#line:115
			os .remove ("/root/mail/mail_content2_.txt")#line:116
			os .mknod ("/root/mail/mail_content2_.txt")#line:117
			os .remove ("/root/mail/mail_content3_.txt")#line:118
			os .mknod ("/root/mail/mail_content3_.txt")#line:119
			for O000OO0O00OOOOO00 in range (0 ,3 ):#line:121
				if O000OO0O00OOOOO00 ==0 :#line:122
					O0O000OO0O000O000 =open ("/root/mail/mail_content1_.txt","a",encoding ="utf-8")#line:123
					OOO0O0000O00000O0 =input ('第'+str (O000OO0O00OOOOO00 +1 )+'主题:')#line:124
					O0O000OO0O000O000 .write (OOO0O0000O00000O0 )#line:125
					OOOO00OOOO00O000O =1 #line:127
					OO0O0OOOOO00OO000 =open ("/root/mail/mail_content1.txt","a",encoding ="utf-8")#line:128
					OOO00O0O0O0OO0000 =input ('正文,第'+str (OOOO00OOOO00O000O )+'行:')#line:129
					while OOO00O0O0O0OO0000 !='stop':#line:130
						OO0O0OOOOO00OO000 .write (OOO00O0O0O0OO0000 +'\n')#line:131
						OOOO00OOOO00O000O =OOOO00OOOO00O000O +1 #line:132
						OOO00O0O0O0OO0000 =input ('正文,第'+str (OOOO00OOOO00O000O )+'行:')#line:133
				elif O000OO0O00OOOOO00 ==1 :#line:137
					OO0OO0OO000O0OO0O =open ("/root/mail/mail_content2_.txt","a",encoding ="utf-8")#line:138
					OOO0O0000O00000O0 =input ('第'+str (O000OO0O00OOOOO00 +1 )+'主题:')#line:139
					OO0OO0OO000O0OO0O .write (OOO0O0000O00000O0 )#line:140
					OOOO00OOOO00O000O =1 #line:142
					O00OOOOO0O00OO000 =open ("/root/mail/mail_content2.txt","a",encoding ="utf-8")#line:143
					OO00OOOOO0OO0O0O0 =input ('正文,第'+str (OOOO00OOOO00O000O )+'行:')#line:144
					while OO00OOOOO0OO0O0O0 !='stop':#line:145
						OOOO00OOOO00O000O =OOOO00OOOO00O000O +1 #line:146
						O00OOOOO0O00OO000 .write (OO00OOOOO0OO0O0O0 +'\n')#line:147
						OO00OOOOO0OO0O0O0 =input ('正文,第'+str (OOOO00OOOO00O000O )+'行:')#line:148
				elif O000OO0O00OOOOO00 ==2 :#line:152
					O0000OO00OOO00OOO =open ("/root/mail/mail_content3_.txt","a",encoding ="utf-8")#line:153
					OOO0O0000O00000O0 =input ('第'+str (O000OO0O00OOOOO00 +1 )+'主题:')#line:154
					O0000OO00OOO00OOO .write (OOO0O0000O00000O0 )#line:155
					OOOO00OOOO00O000O =1 #line:157
					OO0O0OOO0O0O0O0OO =open ("/root/mail/mail_content3.txt","a",encoding ="utf-8")#line:158
					O00OO0O000OOO0000 =input ('正文,第'+str (OOOO00OOOO00O000O )+'行:')#line:159
					while O00OO0O000OOO0000 !='stop':#line:160
						OOOO00OOOO00O000O =OOOO00OOOO00O000O +1 #line:161
						OO0O0OOO0O0O0O0OO .write (O00OO0O000OOO0000 +'\n')#line:162
						O00OO0O000OOO0000 =input ('正文,第'+str (OOOO00OOOO00O000O )+'行:')#line:163
					OO0O0OOOOO00OO000 .close ()#line:165
					O00OOOOO0O00OO000 .close ()#line:166
					OO0O0OOO0O0O0O0OO .close ()#line:167
					O0O000OO0O000O000 .close ()#line:168
					OO0OO0OO000O0OO0O .close ()#line:169
					O0000OO00OOO00OOO .close ()#line:170
			break #line:171
		elif OO0OO0O000OOO0O0O =='n':#line:172
			break #line:173
		else :#line:174
			print ('输入错误，请重新输入:')#line:175
			continue #line:176
def run ():#line:211
	print ('********************************************',end ='\n')#line:212
	print ('该操作将删除之前的定时！')#line:213
	while True :#line:214
		OO0O0O00OOOO0000O =input ('是否继续操作(y/n):')#line:215
		global n #line:216
		n =0 #line:217
		if OO0O0O00OOOO0000O =='y':#line:218
			while True :#line:219
				OOO00OOO0O0OOOOO0 =eval (input ('发送时间(1-24):'))#line:220
				if isinstance (OOO00OOO0O0OOOOO0 ,int )and OOO00OOO0O0OOOOO0 >=1 and OOO00OOO0O0OOOOO0 <=24 :#line:221
					O00O0OO00O000O0O0 =open ("/root/mail/time.txt","w",encoding ="utf-8")#line:222
					O00O0OO00O000O0O0 .write (str (OOO00OOO0O0OOOOO0 ))#line:223
					O00O0OO00O000O0O0 .close ()#line:224
					break #line:225
				else :#line:226
					print ('输入错误，请重新输入!')#line:227
					continue #line:228
		elif OO0O0O00OOOO0000O =='n':#line:229
			return 0 #line:230
		else :#line:232
			print ('输入错误，请重新输入!')#line:233
			continue #line:234
		n =1 #line:235
		print ('定时成功，已开始定时任务!')#line:236
		break #line:237
def delete_run ():#line:242
	print ('********************************************',end ='\n')#line:243
	global q #line:244
	q =0 #line:245
	while True :#line:246
		OO00OO000O000OO0O =input ('是否进行删除定时任务(y/n):')#line:247
		if OO00OO000O000OO0O =='y':#line:248
			q =1 #line:249
			break #line:250
		elif OO00OO000O000OO0O =='n':#line:251
			q =0 #line:252
			break #line:253
		else :#line:254
			print ('输入错误，请重新输入!')#line:255
			continue #line:256
	print ('定时已删除!')#line:257
def main ():#line:273
	print ('********************************************',end ='\n')#line:274
	print ('x站宣传利器！\n')#line:275
	print ('\t\t环境配置-----0\n\n\t\tQQ添加-----1\n\t\tQQ处理-----2\n\t\t重置账户-----3\n\t\t编辑邮件-----4\n\t\t定时运行-----5\n\t\t删除定时-----6\n\n\t\t查看账户邮件-----7\n\t\t查看发送结果-----8\n\n\t\t退出-----9\n')#line:276
	O0OO00000O000O0OO =input ('请输入数字:')#line:277
	while True :#line:278
		if O0OO00000O000O0OO =='0'or O0OO00000O000O0OO =='1'or O0OO00000O000O0OO =='2'or O0OO00000O000O0OO =='3'or O0OO00000O000O0OO =='4'or O0OO00000O000O0OO =='5'or O0OO00000O000O0OO =='6'or O0OO00000O000O0OO =='7'or O0OO00000O000O0OO =='8'or O0OO00000O000O0OO =='9':#line:280
			if O0OO00000O000O0OO =='0':#line:281
				Init ()#line:282
				if c ==1 :#line:283
					os .system ('/root/mail/Init.sh.x~')#line:284
			if O0OO00000O000O0OO =='1':#line:285
				os .system ('/root/mail/qq_add.sh.x~')#line:286
			if O0OO00000O000O0OO =='2':#line:287
				deal_qq ()#line:288
				if u ==1 :#line:289
					os .system ('/root/mail/qq_cat.sh.x~')#line:290
			if O0OO00000O000O0OO =='3':#line:292
				account ()#line:293
				if m ==1 :#line:294
					os .system ('/root/mail/account.sh.x~')#line:295
			if O0OO00000O000O0OO =='4':#line:297
				edit_mail ()#line:298
			if O0OO00000O000O0OO =='5':#line:299
				run ()#line:300
				if n ==1 :#line:301
					os .system ('/root/mail/run_crontab.sh.x~')#line:302
			if O0OO00000O000O0OO =='6':#line:303
				delete_run ()#line:304
				if q ==1 :#line:305
					os .system ('/root/mail/delete_run.sh.x~')#line:306
			if O0OO00000O000O0OO =='7':#line:308
				os .system ('/root/mail/check_account_mail.sh.x~')#line:309
			if O0OO00000O000O0OO =='8':#line:310
				os .system ('/root/mail/cat_result.sh.x~')#line:311
			if O0OO00000O000O0OO =='9':#line:312
				sys .exit ()#line:313
		else :#line:314
			print ('输入错误，请重新输入!')#line:315
			print ('********************************************',end ='\n')#line:316
			print ('\t\t环境配置-----0\n\n\t\tQQ添加-----1\n\t\tQQ处理-----2\n\t\t重置账户-----3\n\t\t编辑邮件-----4\n\t\t定时运行-----5\n\t\t删除定时-----6\n\n\t\t查看账户邮件-----7\n\t\t查看发送结果-----8\n\n\t\t退出-----9\n')#line:317
			O0OO00000O000O0OO =input ('请重新输入:')#line:318
			continue #line:319
		print ('********************************************',end ='\n')#line:320
		print ('\t\t环境配置-----0\n\n\t\tQQ添加-----1\n\t\tQQ处理-----2\n\t\t重置账户-----3\n\t\t编辑邮件-----4\n\t\t定时运行-----5\n\t\t删除定时-----6\n\n\t\t查看账户邮件-----7\n\t\t查看发送结果-----8\n\n\t\t退出-----9\n')#line:321
		O0OO00000O000O0OO =input ('请输入数字:')#line:322
if __name__ =="__main__":#line:328
	main ()#line:329

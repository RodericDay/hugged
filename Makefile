development:
	-pkill hug
	/home/roderic/Developer/anaconda3/envs/hug/bin/py.test -v
	/home/roderic/Developer/anaconda3/envs/hug/bin/hug -f app.py

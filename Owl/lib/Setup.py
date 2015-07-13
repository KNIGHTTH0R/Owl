import json

#importing general settings
def configure_settings():

	settings_dict = {}
	settings_dict['cg_set'] = ''

	config_file = open("config.conf", "r")

	config_response = config_file.read()
 
	config_file.close()

	config_response = json.loads(config_response)
	#reading json from config.conf
	for key in config_response.iterkeys():
		#main settings
		if key == "settings":

			#taking settings from file dict and adding to local dictionary
			settings_dict['sell_market'] = config_response[key]["market-to-sell-to"]
			settings_dict['cg_start'] = config_response[key]["auto-start-cgminer"]
			settings_dict['timer'] = config_response[key]["timer"]
			settings_dict['report'] = config_response[key]["report"]
			settings_dict['mining_kernel'] = config_response[key]["kernel"]

			#assigning correct mining kernel
			if settings_dict['mining_kernel'] == '0':
				del config_response[key]['kernel']
				del config_response[key]['scrypt']
			elif settings_dict['mining_kernel'] == '1' or settings_dict['mining_kernel'] == '2' or settings_dict['mining_kernel'] == '4':
				config_response[key]['kernel'] = 'scrypt'
				config_response[key]['scrypt'] = ''
			elif settings_dict['mining_kernel'] == '3':
				config_response[key]['kernel'] = 'darkcoin'
				del config_response[key]['scrypt']
			else:
				pass
		else:
			for setting in config_response[key].iterkeys():
				settings_dict['cg_set'] += "--" + setting + " " + str(config_response[key][setting]) + " "
	return settings_dict
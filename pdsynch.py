import json
import datetime
import subprocess


def read_config():
    print(datetime.datetime.now(), '-' * 30)
    print(datetime.datetime.now(), 'Reading configuration')

    filename = 'config.json'
    with open(filename, 'r') as f:
        config = json.load(f)

    hlq_list = config.get('hlq')
    # for dataset in hlq_list: 
    #     print(dataset)
    cycle = config.get('cycle')
    master_prof = config.get('master_prof')
    target_prof_list = config.get('target_prof') 
    stop = config.get('stop')
    ghrepo = config.get('ghrepo')
    print(datetime.datetime.now(), '-' * 30)
    print(datetime.datetime.now(), 'Reading configuration finished')

def run_command(command):
    print(datetime.datetime.now(), '-' * 30)
    print(datetime.datetime.now(), 'Executing command: ' + command)
    output = subprocess.check_output(command, text=True, shell=True)
    return output



read_config()

ds = 'roddi01.git.rex*'
command = "zowe files list ds " + ds + " -a --rfj > sss.json" 
output = run_command(command) 
print(type(output))
print(output)
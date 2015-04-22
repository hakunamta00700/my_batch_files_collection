'''
initialize project folder for GAE

it make :
    ~/workspace/GAE/<projectName>
    ~/workspace/GAE/<projectName>/main.py



'''

import os
import sys


app_yml_template = '''

application:{_application}
version : {_version}
runtime : python
api_version : {_api_version}

handers:
    url : /.*
    script : main.py
'''

'''
    parser = argparse.ArgumentParser()
    allArgumentsList = [
                        ('-vn', '--versionName', '?', 'specify version name to build for user', str),
                        ('-vc', '--versionCode', '?', 'specify version code to build for buildsystem or update', int),
#                         ('-pl', '--platform', 1, 'platform to build or run - [ win32, darwin ] '),
#                         ('-md', '--mode', 1, 'kind of program when it run - [ console, window ] '),
                        ('-bm', '--buildMode', '?', 'buildMode - release, debug', str),
#                         ('-sr', '--showReleaseNote', 1, 'showRelease', bool),
                        ("-rb", '--removeBuildCache', '?', "remove buildCache, if it is True, buildCache will be removed", bool),
#                         ("-ar", "--archive", 1, "make archiving for update", bool),
#                         ("-aa", "--autoArgument", 1, "specify whether argument is put automatically", bool)
                    ]
    versionName
    versionCode

    buildMode = 'release, debug'
        release
            mode = window
        debug
            mode = console

    if buildMode is 'release', versionCode will be increased automatically.

    '''
    # for argItem in allArgumentsList:
    #     _type = str
    #     if len(argItem) == 5:
    #         _type = argItem[4]

    #     parser.add_argument(argItem[0], argItem[1], nargs=argItem[2], help=argItem[3], type=_type)

    # _build = Build()
    # print sys.argv[1:]
    # parser.parse_args(args=sys.argv[1:], namespace=_build)

if __name__ == '__main__':
    prefix = os.path.join(os.path.expanduser("~"),'workspace') 
    projectName = sys.argv[1]
    api_version = 1
    version = 1

    projectDir = os.path.join(prefix, projectName)
    if not os.path.isdir(projectDir):
        os.makedirs(projectDir)

    app_yaml_file = os.path.join(projectDir, 'app.yaml')
    fp = open(app_yaml_file, 'w')
    
    fp.write(app_yml_template.format(_application=projectName, _version=version, _api_version=api_version))
    fp.close()



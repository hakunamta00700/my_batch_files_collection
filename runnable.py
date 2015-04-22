import sys
import os

target_src_filename = sys.argv[1]

shell_script_template = '''
#/bin/sh
python {_target} "$@"
'''

target_file_basename = os.path.basename(target_src_filename)
target_file_basename = os.path.splitext(target_file_basename)[0]

target_dir = os.path.join(os.path.expanduser("~"), 'batch')

target_file_path = os.path.join(target_dir, target_file_basename)

fp = open(target_file_path, "w")
shell_script = shell_script_template.format(_target=target_file_path)
fp.write(shell_script)
fp.close()

cmd = 'chmod 755 {0}'.format(target_file_path)
os.system(cmd)








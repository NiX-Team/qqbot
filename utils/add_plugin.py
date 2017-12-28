import os
import sys


CONF_TMP = '.conf.tmp'
CONF_FILE = 'v2.3.conf'

SCHED_TMP = '''from qqbot import qqbotsched

@qqbotsched(hour='0', minute='0')
def {0}(bot):
    pass

'''

CALLBACK_FUNCTIONS = {
    'onInit': 'bot',
    'onQrcode': 'bot, pngPath, pngContent',
    'onQQMessage': 'bot, contact, member, content',
    'onInterval': 'bot',
    'onStartupComplete': 'bot',
    'onUpdate': 'bot, tinfo',
    'onPlug': 'bot',
    'onUnplug': 'bot',
    'onExit': 'bot, code, reason, error'
}


def main():
    while True:
        plug_name = input('Enter the plugin name (plugin): ')
        if not plug_name:
            plug_name = 'plugin'
        if not os.path.exists('plugins/{0}.py'.format(plug_name)):
            plug_file = open('plugins/{0}.py'.format(plug_name), 'w')
            break
        print('Plugin already exists, enter another name.')
        continue

    yn = input('Create an scheduler? (y/N): ').lower()
    if yn.startswith('y'):
        sched_name = input('Enter the scheduler name (scheduler): ')
        if not sched_name:
            sched_name = 'scheduler'
        plug_file.write(SCHED_TMP.format(sched_name))

    for name, args in CALLBACK_FUNCTIONS.items():
        yn = input('Create an {0} callback function? (y/N): '.format(name))\
            .lower()
        if yn.startswith('y'):
            plug_file.write('def {0}({1}):\n'.format(name, args))
            plug_file.write('    pass\n\n')

    yn = input('Add plugin to config file? (y/N): ').lower()
    if yn.startswith('y'):
        if os.path.exists(CONF_FILE):
            tmp_file = open(CONF_TMP, 'w')
            with open(CONF_FILE, 'r') as conf:
                match_flg = False
                for line in conf:
                    if '"默认配置"' in line:
                        match_flg = True
                    if match_flg and '"plugins"' in line:
                        left_bracket = line.index('[')
                        right_bracket = line.index(']')

                        plugins = line[left_bracket+1:right_bracket]\
                            .split(',')

                        plugins = [p.strip() for p in plugins if p.strip()]

                        plugins = plugins + ['\'{0}\''.format(plug_name)]

                        line = line[:left_bracket+1] +\
                            ','.join(plugins) +\
                            line[right_bracket:]

                        match_flg = False

                    tmp_file.write(line)

                tmp_file.close()
                os.rename(CONF_TMP, CONF_FILE)
        else:
            sys.stderr.write('Do not match a config file.\n')

    print('Plugin file created.')
    plug_file.close()


if __name__ == '__main__':
    main()

import configparser
import datetime

import lib.common
import lib.git
import lib.xinghuo


def process_project_logs(config, project_name):
    logs = parseLog(config, project_name, 'week')
    if len(logs) == 0:
        print("周报日志为空")
    else:
        content = "根据Git的开发日志总结周报："+ ",".join(logs)
        lib.xinghuo.send(
            config,
            content)
    logs = parseLog(config, project_name, 'month')
    if len(logs) == 0:
        print("月报日志为空")
    else:
        content = "根据Git的开发日志总结月报："+ ",".join(logs)
        lib.xinghuo.send(
            config,
            content)

    logs = parseLog(config, project_name, 'year')
    if len(logs) == 0:
        print("年报日志为空")
    else:
        content = "根据Git的开发日志总结年报：" + ",".join(logs)
        lib.xinghuo.send(
            config,
            content)

    logs = parseLog(config, project_name, 'year')


def parseLog(config, project_name, tag):
    if config['global'][tag] == "0":
        return []

    start_date = config['global']['start']
    repo_path = config[project_name]['repo_path']
    users = config[project_name]['users'].split(',')
    end_date = lib.common.get_week_range(start_date)
    logs = []
    for user in users:
        res = lib.git.get_git_log(user.strip(), end_date[0], end_date[1], repo_path)
        if len(res):
            logs = logs + [item.split(" ")[3] for item in res]
        logs = list(set(logs))
    return logs


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    secrets = config.sections()
    secrets = [item for item in secrets if item != 'global']
    for project_name in secrets[1:]:
        process_project_logs(config, project_name)


if __name__ == "__main__":
    main()

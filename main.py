import configparser
import datetime

import lib.common
import lib.git
import lib.xinghuo


def process_project_logs(config, secrets):
    logs = parseLog(config, secrets, 'week')
    if len(logs) == 0:
        print("周报日志为空")
    else:
        content = "根据Git的开发日志，以功能视角总结周报(列表格式，简明明了，不超过100字)：" + ",".join(logs)
        lib.xinghuo.send(
            config,
            content)

    logs = parseLog(config, secrets, 'month')
    if len(logs) == 0:
        print("月报日志为空")
    else:
        content = "根据Git的开发日志总结月报(简明明了，讲明白干了什么就好)：" + ",".join(logs)
        lib.xinghuo.send(
            config,
            content)

    logs = parseLog(config, secrets, 'year')
    if len(logs) == 0:
        print("年报日志为空")
    else:
        content = "根据Git的开发日志总结年报(简明明了，讲明白干了什么就好)：" + ",".join(logs)
        lib.xinghuo.send(
            config,
            content)


def parseLog(config, secrets, tag):
    if config['global'][tag] == "0":
        return []

    start_date = config['global']['start']
    if tag == "week":
        end_date = lib.common.get_week_range(start_date)
    elif tag == "month":
        end_date = lib.common.get_month_range(start_date)
    else:
        end_date = lib.common.get_year_range(start_date)

    logs = []
    for project_name in secrets:
        repo_path = config[project_name]['repo_path']
        users = config[project_name]['users'].split(',')
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
    process_project_logs(config, secrets)


if __name__ == "__main__":
    main()

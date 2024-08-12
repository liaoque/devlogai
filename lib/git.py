import datetime
import subprocess


def get_git_log(user, start_date, end_date, repo_path='.'):
    # if datetime.datetime.strptime(end_date, "%Y-%m-%d") >= datetime.datetime.today():
    #     end_date = ""

    """
    获取指定用户在指定时间范围内的 git 提交日志。

    :param user: 用户名或用户邮箱
    :param start_date: 开始日期，格式为 'YYYY-MM-DD'
    :param end_date: 结束日期，格式为 'YYYY-MM-DD'
    :param repo_path: Git 仓库路径，默认为当前目录
    :return: Git 提交日志的字符串
    """
    command = [
        'git', 'log',
        '--author={}'.format(user),
        '--since="{} 00:00:00"'.format(start_date),
        '--until="{} 23:59:59"'.format(end_date),
        '--pretty=format:%h %an %ad %s',
        '--date=short'
    ]

    result = subprocess.run(command, cwd=repo_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                            encoding='utf-8')

    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return []
    if result.stdout == "":
        return []

    return result.stdout.split("\n")

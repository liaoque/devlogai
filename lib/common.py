from datetime import datetime, timedelta


def get_week_range(reference_date=None):
    """
    获取本周的开始日期和结束日期。

    :param reference_date: 参考日期，默认为今天
    :return: 本周的开始日期和结束日期，格式为 (start_date, end_date)
    """
    if reference_date is None or reference_date == "":
        reference_date = datetime.today()
    elif isinstance(reference_date, str):
        reference_date = datetime.strptime(reference_date, "%Y-%m-%d")

    # 计算星期一的日期
    start_of_week = reference_date - timedelta(days=reference_date.weekday())
    # 计算星期天的日期
    end_of_week = start_of_week + timedelta(days=6)

    # 格式化日期为 'YYYY-MM-DD'
    start_of_week_str = start_of_week.strftime('%Y-%m-%d')
    end_of_week_str = end_of_week.strftime('%Y-%m-%d')

    return start_of_week_str, end_of_week_str


def get_month_range(reference_date=None):
    """
    获取本周的开始日期和结束日期。

    :param reference_date: 参考日期，默认为今天
    :return: 本周的开始日期和结束日期，格式为 (start_date, end_date)
    """
    if reference_date is None:
        reference_date = datetime.today()

    # 计算星期一的日期
    start_of_week = reference_date - timedelta(days=reference_date.weekday())
    # 计算星期天的日期
    end_of_week = start_of_week + timedelta(days=6)

    # 格式化日期为 'YYYY-MM-DD'
    start_of_week_str = start_of_week.strftime('%Y-%m-%d')
    end_of_week_str = end_of_week.strftime('%Y-%m-%d')

    return start_of_week_str, end_of_week_str


def get_year_range(reference_date=None):
    """
    获取本周的开始日期和结束日期。

    :param reference_date: 参考日期，默认为今天
    :return: 本周的开始日期和结束日期，格式为 (start_date, end_date)
    """
    if reference_date is None:
        reference_date = datetime.today()

    # 计算星期一的日期
    start_of_week = reference_date - timedelta(days=reference_date.weekday())
    # 计算星期天的日期
    end_of_week = start_of_week + timedelta(days=6)

    # 格式化日期为 'YYYY-MM-DD'
    start_of_week_str = start_of_week.strftime('%Y-%m-%d')
    end_of_week_str = end_of_week.strftime('%Y-%m-%d')

    return start_of_week_str, end_of_week_str

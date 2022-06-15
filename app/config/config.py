class Config(object):
    # 存储位置
    #SCHEDULER_JOBSTORES = {
    #    'default': SQLAlchemyJobStore(url='sqlite:///db/cese.db')
    #}
    # 线程池配置
    SCHEDULER_EXECUTORS = {
        'default': {'type': 'threadpool', 'max_workers': 100}
    }
    SCHEDULER_JOB_DEFAULTS = {
        'coalesce': False,
        'max_instances': 100
    }
    # 调度器控制
    SCHEDULER_API_PW = ''
    # 调度器开关
    SCHEDULER_API_ENABLED = True
    # 访问端口 --必填 只允许数字
    WEB_PORT = 9001
    #redis地址 --必填
    REDIS_ADDRESS = '127.0.0.1'
    #redis端口 --必填 只允许数字
    REDIS_PORT = 6379
    #redis数据库密码 --必填
    REDIS_PWD = 'qaz123qaz'
    #redis库索引 默认0-16
    REDIS_INDEX =11

import traceback
import sys
import os
import requests
import xml.dom.minidom as x
from app.logs import log
from app import app
from app.view import system, user, rule, task, content, repair, sorty, openfun, move,api
from app.helper.redishelper import r
from flask import request, render_template, session

app = app()
app.secret_key = 'wxcjq'


@app.route('/', methods=['GET', 'POST'])
def index():
    sess = session.get('token')
    if not sess:  # 没有登录就自动跳转到登录页面去
        return render_template('login.html')
    else:
        return render_template('index.html', name=sess)

@app.route('/api/<route_name>', methods=['GET', 'POST'])
def appRoute(route_name):
    try:
        # API接口-开始
        if route_name == 'getAdvertisementList':  # 获取广告信息
            return api.getAdvertisementList
        if route_name == 'getSortList':  # 获取分类列表
            return api.getSortList()
        if route_name == 'getRecentlyAddList':  # 获取最近添加列表
            return api.getRecentlyAddList()
        if route_name == 'getRecentlyUpList':  # 获取最近更新列表
            return api.getRecentlyUpList()
        if route_name == 'getRankingList':  # 获取排行列表
            return api.getRankingList()
        if route_name == 'getNovelList':  # 获取小说列表
            return api.getNovelList()
        if route_name == 'getNovelInfo':  # 获取小说信息
            return api.getNovelInfo()
        if route_name == 'getChapterList':  # 获取章节列表
            return api.getChapterList()
        if route_name == 'getChapterInfo':  # 获取章节内容信息
            return api.getChapterInfo()
        if route_name == 'getAccAuthorNovelList':  # 根据作者名称获取小说列表
            return api.getAccAuthorNovelList()
        if route_name == 'getSearchNovelList':  # 根据作者名称或小说名称搜索小说列表
            return api.getSearchNovelList()
        if route_name == 'getSelectedInfo':  # 获取精选内容
            return api.getSelectedInfo()
        # API接口-结束
    except Exception as e:
        return traceback.extract_stack()

@app.route('/<route_name>', methods=['GET', 'POST'])
def route(route_name):
    try:
        sess = session.get('token')
        if route_name == 'feedbacknovel':
            return openfun.小说反馈存储()
        if route_name == 'feedbackchapter':
            return openfun.章节反馈存储()
        if route_name == 'GetArticleInfo':  # 获取小说详细信息
            return move.GetArticleInfo()
        if route_name == 'GetArticleList':  # 获取小说列表
            return move.GetArticleList()
        if route_name == 'GetChapterInfo':  # 获取章节详细信息
            return move.GetChapterInfo()
        if route_name == 'GetChapterList':  # 获取章节列表
            return move.GetChapterList()
        if route_name == 'GetSortInfo':  # 获取分类信息
            return move.GetSortInfo()
        if route_name == 'GetRecommendInfo':  # 获取推荐信息
            return move.GetRecommendInfo()
        if route_name == 'login':
            SCHEDULER_API_PW = ''
            if not app.config['SCHEDULER_API_PW'] == None:
                SCHEDULER_API_PW = str(app.config['SCHEDULER_API_PW'])
            return user.login(SCHEDULER_API_PW)
        elif not sess:  # 没有登录就自动跳转到登录页面去
            return render_template('login.html')
        if route_name == 'help':
            return render_template('/help.html')
        elif route_name == 'sys':
            return system.系统设置()
        elif route_name == 'sort1':
            return system.一级分类()
        elif route_name == 'sort2':
            return system.二级分类()
        elif route_name == 'channel':
            return system.频道()
        elif route_name == 'status':
            return system.连载状态()
        elif route_name == 'useragent':
            return system.设置UA()
        elif route_name == 'daili':
            return system.代理()
        elif route_name == 'addapitask':
            return system.addApiTask()
        elif route_name == 'pwd':
            return user.修改密码()
        elif route_name == 'test':
            return sorty.测试规则()
        elif route_name == 'rulelist':
            return render_template('/rulemanage/rulelist.html')
        elif route_name == 'getrulelist':
            return rule.获取规则列表()
        elif route_name == 'delrule':
            return rule.删除规则()
        elif route_name == 'import':
            return render_template('/rulemanage/import.html')
        elif route_name == 'emprot':
            return rule.导出规则()
        elif route_name == 'synchRule':
            return rule.同步规则()
        elif route_name == 'addimport':
            return rule.导入规则()
        elif route_name == 'rule':
            return rule.获取规则()
        elif route_name == 'addrule':
            return rule.添加规则()
        elif route_name == 'task':
            return task.任务()
        elif route_name == 'looktask':
            return task.查看任务()
        elif route_name == 'starttask':
            return task.启动任务()
        elif route_name == 'suspendtask':
            return task.暂停任务()
        elif route_name == 'deltask':
            return task.删除任务()
        elif route_name == 'delselectTask':
            return task.删除选中任务()
        elif route_name == 'startselectTask':
            return task.启动选中任务()
        elif route_name == 'stopselectTask':
            return task.暂停选中任务()
        elif route_name == 'synchTask':
            return task.同步任务()
        elif route_name == 'tasklist':
            return render_template('/taskmanage/tasklist.html')
        elif route_name == 'gettasklist':
            return task.获取任务列表()
        elif route_name == 'contentlist':
            return render_template('/contentmanage/contentlist.html')
        elif route_name == 'getcontentlist':
            return content.获取内容列表()
        elif route_name == 'savearticle':
            return content.保存信息内容()
        elif route_name == 'articleinfo':
            return content.查询小说信息()
        elif route_name == 'addident':
            return content.添加标识()
        elif route_name == 'delident':
            return repair.删除标识()
        elif route_name == 'chapter':
            return content.获取章节列表()
        elif route_name == 'delchapterall':
            return content.按顺序批量删除章节()
        elif route_name == 'loglist':
            return render_template('/repairmanage/loglist.html')
        elif route_name == 'getloglist':
            return repair.获取日志列表()
        elif route_name == 'dellog':
            return repair.删除日志()
        elif route_name == 'novelrepair':
            return repair.小说修复()
        elif route_name == 'getidentlist':
            return repair.章节修复()
        elif route_name == 'chapterrepair':
            return render_template('/repairmanage/chapterrepair.html')
        elif route_name == 'contentrepair':
            return repair.章节内容修复()
        elif route_name == 'ident':
            return system.内容标识()
        elif route_name == 'emailinfo':
            return user.emailinfo()
        elif route_name == 'testemail':
            return user.test_maill()
        elif route_name == 'novelfeedback':
            return openfun.小说反馈()
        elif route_name == 'chapterfeedback':
            return openfun.章节反馈()
        elif route_name == 'releaseThirdParty':  # 发布到第三方设置
            return openfun.发布第三方设置()
        elif route_name == 'delfeedbacknovel':
            return openfun.删除小说反馈()
        elif route_name == 'advertisement':
            return move.查询广告()
        elif route_name == 'getadvertlist':
            return move.查询广告列表()
        elif route_name == 'deladvertisement':
            return move.删除广告()
        elif route_name == 'rotation':
            return move.查询轮播图()
        elif route_name == 'getrotationlist':
            return move.查询轮播图列表()
        elif route_name == 'delrotationment':
            return move.删除轮播图()
        elif route_name =='getLoadId':
            return  repair.根据ID加载列表()
        elif route_name =='getLoadSoureUrl':
            return repair.根据源地址获取列表()
        elif route_name =='replaceAcquisition':
            return repair.替换采集()
        elif route_name =='replacementContent':
            return repair.替换内容()
        elif route_name =='beforeInsertion':
            return repair.插入之前()
        elif route_name =='afterInsertion':
            return repair.插入之后()
        elif route_name =='checkDuplication':
            return repair.检查重复()
        elif route_name =='saveSort':
            return repair.保存排序()
        return route_name
    except Exception as e:
        return traceback.extract_stack()


if __name__ == '__main__':
    if r == None:
        log.logger.info('检查下app/config/config.py中是否设置Redis数据库信息')
    elif app.config['WEB_PORT'] == None:
        log.logger.info('检查下app/config/config.py中是否设置Redis数据库信息')
    else:
        if not r.exists('username'):
            r.set('username', 'admin')
            r.set('pwd', 'admin')
            r.persist('username')
            r.persist('pwd')
        list_keys = r.keys("xsid*")
        for key in list_keys:
            r.delete(key)
    app.run(host='0.0.0.0', port=app.config['WEB_PORT'])

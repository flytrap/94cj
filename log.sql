
CREATE TABLE `log_article_source` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `articleid` int(11) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `soure` varchar(500) DEFAULT NULL,
  `ruleid` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `log_chapter_ident` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `articleid` int(11) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `chapterid` int(11) DEFAULT NULL,
  `chapter_name` varchar(255) DEFAULT NULL,
  `adddate` datetime DEFAULT NULL,
  `ident` varchar(1) DEFAULT '0',
  `url` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `log_chapter_url` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `articleid` int(11) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `chapterid` int(11) DEFAULT NULL,
  `chapter_name` varchar(255) DEFAULT NULL,
  `chapter_url` varchar(500) DEFAULT NULL,
  `adddate` datetime DEFAULT NULL,
  `ruleid` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `log_err` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `articleid` int(11) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `chapterid` int(11) DEFAULT NULL,
  `chapter_name` varchar(255) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  `msg` text,
  `adddate` datetime DEFAULT NULL,
  `ruleid` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `chapterorder` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

CREATE TABLE `log_rule` (
  `ruleId` varchar(50) NOT NULL COMMENT '规则ID',
  `ruleName` varchar(200) DEFAULT NULL COMMENT '规则名称',
  `ruleBase64` text COMMENT '规则Base64内容',
  `addTime` datetime DEFAULT NULL COMMENT '添加时间',
  `updateTime` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`ruleId`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

CREATE TABLE `log_task` (
  `taskId` varchar(100) NOT NULL,
  `taskName` varchar(200) DEFAULT NULL,
  `taskBase64` text,
  `taskType` varchar(100) DEFAULT NULL,
  `taskStatus` varchar(100) DEFAULT NULL,
  `taskTime` varchar(100) DEFAULT NULL,
  `addTime` datetime DEFAULT NULL,
  `updateTime` datetime DEFAULT NULL,
  `ruleId` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`taskId`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

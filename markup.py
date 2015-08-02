#-*-coding:utf-8-*-
#----主程序

import sys,re
from handlers import HTMLRenderer
from util import blocks
from rules import *

class Parser:
    """
            语法分析器读取文本文件、应用规则并且控制处理程序
    """
    
    def __init__(self,handler): #构造函数将提供的处理序列分配给一个变量，然后初始化两个表和传递的两个参数
        self.handler = handler
        self.rules = []
        self.filters = []
        self.first = True
        self.inside = False
        
    def addRule(self,rule): #把规则添加到规则列表中
        self.rules.append(rule)
    
    def addFilter(self,pattern,name):   #向过滤器列表中添加一个过滤器
        def filter(block,handler):  
            """
                                    创建过滤器，过滤器是一个函数，这个函数对合适的正则表达式（模式）应用
            re.sub一个来自动处理程序的替换，该处理程序使用handler.sub(name)
                                    进行访问
            """
            return re.sub(pattern,handler.sub(name),block)
        self.filters.append(filter)
        
    def parse(self,file):
        """
                        从调用处理程序的start('document')开始,以调用end('document')结束
                        在两次调用之间它迭代文本文件中所有的块
        """
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block,self.handler)
            for rule in self.rules:
                if rule.condition(self,block):   #检测是否应用规则
                    last = rule.action(self,block,self.handler)  #用块和处理程序参数来调用rule.action
                    if last:break   #为块完成了规则应用
        self.handler.end('document')
        
class BasicTextParser(Parser):
    """
            在构造函数中增加规则和过滤器的具体语法分析器
    """
    def __init__(self,handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule)
        self.addRule(ListItemRule)
        self.addRule(TitleRule)
        self.addRule(HeadingRule)
        self.addRule(ParagraphRule)
        
        self.addFilter(r'\*(.+?)\*', 'emphasis')    #匹配关于强调的内容
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')
        
handler = HTMLRenderer()
parser = BasicTextParser(handler)

parser.parse(sys.stdin)

#命令行运行 python markup.py <test_input.txt> test_output.html
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
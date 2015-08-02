#-*-coding:utf-8-*-
#文本块生成器

def lines(file):
    """
            文件的最后追加一个空行
    """
    for line in file: 
        yield line
    yield '\n'
    

def blocks(file): 
    """
            当生成一个块后，它后面的行会被连接起来，并且获得的字符串会被删除掉，
            得到一个代表块的字符串，同时，开始和结尾中的多余的空格会被删除。
    """
    block=[]
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block=[]
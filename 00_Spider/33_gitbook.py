# coding=utf-8

# 我还是太笨了，这么一点代码我花了有20个小时了
# 这点代码还可以用更多的函数封装精简一下，不过我已经不想再纠缠下去了
import os
def convert(path):
    n = 1
    dirs = os.listdir(path)
    for file in dirs:
        if file.endswith('.html'):
            filepath = path + '\\' + file
            os.system('gitbook-convert -m 1 %s %s' % (filepath, path))
            # 为了方便检索课件知识点，我也是拼了老命了
            # 起初在一点都不懂的情况下用命令行转换，提示缺少readme文件
            # 刚使用github上传代码发现会自动生成reademe文件，喜出望外
            # 搭建环境也是极其坎坷，好不容易搭好了，还是一个劲的失败
            # 都萌生了从头开始学习如何制作gitbook了，还好网上资料太少
            # 官网又慢的要命，断了这个念想
            # 绝望到想哭的时候找到了有点样子的gitbook范本，查看人家的
            # readme发现内容极其丰富，再回头看看github给我生成的是什么鬼
            # TM就生成的一行英文而已，我TM
            # 病急乱投医，偶然翻阅教程帖子发现gitbook-convert可以转pdf为gitbook文件
            # 至此，终于找到了真正的正确的道路，虽然后面还有无穷的坎在笑嘻嘻地等着我...
            subsummary = '%s\\%s' % (path, 'SUMMARY.md')
            if subsummary != parentsummary:
                sub = open(subsummary, 'r')
                lines = sub.readlines()
                sub.close()
                try:
                    # 触发异常
                    expection = lines[3]
                    # 这里也是一个巨大的坑 TM即便len(lines)>4也不抛出异常
                    # 第一版以为每一个summary.md除了index外只有一个md链接，就直接
                    # 写成 md = sub.readlines()[3]
                    # 后面对比生成文件发现漏了一些数据
                    # 就探索如何从指定行开始读取若干行数据也走了不少弯路
                    # 原来正确操作如此简洁精炼
                    lists = lines[3:]
                    for list in lists:
                        md = list.replace('(', '(' + path.split('\\')[-1] + '\\')
                        with open(parentsummary, 'a+') as f:
                            f.write('\n' + md)
                        print '\n' + md
                # 触发异常，除了一些index.html文件外，还有小部分文件的内容文件只有index链接
                # 单纯过滤index文件也是行不通的，因为仍有少数部分index文件包含了一部分内容
                # 所以虽然这部分会产生绝大多数index垃圾文件，但不至于漏掉内容文件
                except:
                    subname = 'README%s.md' % n
                    n += 1
                    subsummary = '%s\\%s' % (path, subname)
                    os.system('copy %s\README.md %s' % (path, subsummary))
                    print '+' * 100
                    sub.close()
                    sub = open(subsummary, 'r')
                    print sub.read()
                    sub.close()
                    print '+' * 100
                    md = '* [%s](%s)' % (subname.split('.')[0], subname)
                    md = md.replace('(', '(' + path.split('\\')[-1] + '\\')
                    print '\n' + md
                    with open(parentsummary, 'a+') as f:
                        f.write('\n' + md)
                print 'Convert done!\t' + file + '\n'

    for file in dirs:
        filepath = '%s\\%s' % (path, file)
        if os.path.isdir(filepath):
            convert(filepath)


def g2p(path):
    filename = path.split('\\')[-1]
    # 这里我花了太多精力去调试了 TM最后才发现成功概率是1/5 ~ 1/10 TM跟怎么调整代码没半毛关系
    while not os.path.exists('%s/%s.pdf' % (path, filename)):
        os.system('gitbook pdf %s %s/%s.pdf' % (path, path, filename))


if __name__ == '__main__':
    # 这里为了支持中文文件夹路径也是调了不少功夫
    # 使用input函数输入文件夹路径会抛出解码异常错误
    # 老哥建议不要把路径写死，为了把这所谓的脚本加入环境变量
    # 方便使用命令行调用，就我个人而言没这必要
    # 需要转换某个传智播客的课件的话只要复制路径替换一下
    path = r"C:\Users\Administrator\Desktop\MySQL".encode('GBK')
    parentsummary = path + '\\' + 'SUMMARY.md'
    convert(path)
    g2p(path)
    print 'Job done!!!'

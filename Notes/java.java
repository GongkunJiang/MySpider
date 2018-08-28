/*开发中，常用到的Eclipse快捷键

注1： 本文内容中的快捷键在我平时的工作大部分都会用到，不需要一次学会，可以慢慢的回顾积累，用的次数多了自然而然就熟悉了，相对于频繁的鼠标操作，这些快捷键可以提升工作效率，也有助于减轻鼠标手症状！

注2：快捷键是可以自己在Eclipse中设置的，但是Eclipse本身设置好的已经够用了，方便用了！

注3：结合网上的资源整理！

0、”ctrl+H”打开文件搜索对话框

此处以“File Search”为例。
使用快捷键“ctrl+H”打开文件搜索对话框，选择“File Search”标签，在Containing text中输入你需要搜索的字符串，在Scope中，选择你要搜索的范围，点击Search。

注：超级实用啊，运维、开发中查找某个类文件、字段、方法等，建议先预测大概在哪个项目模块下，先设置其查找的scope下的Working Set，从.java文件找起，再scope为.xml找起（为啥？因为往往一个模块作为一个项目，整个项目的下面模块较多，自己要做什么最好心理有个数，设置下scope，从.java文件找起比较快，从.xml文件找起很慢——工作感受）

1、alt+? 或 alt+/：自动补全代码或者提示代码

eclipse默认是出现“.”进行方法提示，如果中间提示断了想再看的话还得重新在对应类或者变量的前边输入“.”才可以再看到提示，不过如果这2个键结合是使用同样可以起到提示的作用，你可以试一试，而且如果输入for后，上边如果有需要遍历的局部变量的话，会弹出选择用for each遍历还是for（int;;）还是while()然后自动生成代码。

注：try,cath的话，你打好try后直接alt+/后上下键移动选择你要的try,cath组合

2、ctrl+o：快速outline视图 查看当前类的方法或某个特定方法

如果想要查看当前类的方法或某个特定方法，但又不想把代码拉上拉下，也不想使用查找功能的话，尤其是直接打开或者跟踪到一个方法非常多的类的时候，这个就非常有用，直接看出有那些方法及成员变量，它可以列出当前类中的所有方法及属性，你只需输入你想要查询的方法名，点击enter就能够直接跳转至你想去的位置。

注：当你看某个项目的某个.java文件有8000多行时，或是2000多行时，找某个方法或属性字段时，用它准没错！如果你对绿色实心圆点、红色空心方框这类图标熟悉，那就更方便定位了（请参考：“Eclipse .java文件 颜色+几何形状的意义”）

3、ctrl+shift+r：打开资源列表 ==> Open Type 查找类文件 Ctrl + Shift + T

根据名字直接在项目或者工作空间里找某个文件，这组快捷键可以让你打开你的工作区中任何一个文件，而你只需要按下文件名或mask名中的前几个字母，比如applic*.xml。美中不足的是这组快捷键并非在所有视图下都能用。

注：大部分情况下，我直接用ctrl+shift+r，往往输入文件开始的几个字母就很快在Matching items框里弹出相关文件

4、ctrl+shift+f：格式化代码

默认80个字符就换行，这个可以设置的。也可以根据代码风格设定重新格式化代码，我 们的团队有统一的代码格式，我们把它放在我们的wiki上。要这么做，我们打开Eclipse，选择Window Style，然后设置Code Formatter，Code Style和Organize Imports。利用导出（Export）功能来生成配置文件。我们把这些配置文件放在wiki上，然后团队里的每个人都导入到自己的Eclipse中。

注：我偶尔用，平时写代码对自己要求比较严格（规范。可能也是一种强迫症吧）

5、ctrl+e：快速转换编辑器

这组快捷键将帮助你在打开的编辑器之间浏览，尤是在很多文件打开的状态下，ctrl+e会更加有效率，非常有帮助。

注：资源文件打开的多了，跟踪代码块时打开的文件太多了，除了Alt+左右键，就是ctrl+e这个快捷键组合了（还可以输入文件名定位的）

6、ctrl+page down或ctrl+page up： 选项卡之间快速切换即切换打开的页面框

可以浏览前后的选项卡，如果使用熟练的话，各个页面切换会非常的快，感觉很不错。

7、shift+enter及ctrl+shift+enter： 在当前行上或者下边创建空白

Shift+enter在当前行之下创建一个空白行，与光标是否在行末无关。
Ctrl+shift+enter则在当前行之前插入空白行。
很方便！

8、Alt+方向键上下：上下行交换内容或把当前行内容把上或下移动

节省时间，这个组合将当前行的内容往上或下移动。在try/catch部分，这个快捷方式尤其好使。

9、Ctrl+Alt+方向上下键：复制高亮显示的一行或多行

这个也是非常有用的快捷键，能非常方便复制当前代码到上一行或者下一行，我也经常用到。

10、ctrl+m：当前编辑页面窗口最大化

大显示屏幕能够提高工作效率是大家都知道的。Ctrl+m是编辑器窗口最大化的快捷键，再次按下就恢复正常窗口。

11、ctrl+/：自动注释当前行或者选择的多行

自动注释掉当前行或者多行代码，用//注释，用ctrl+\可以取消注释。

12、ctrl+shift+/：自动注释掉选择的代码块

这个注意是用,css等也可以用这个注释,生成对应的注释标签，用ctrl+shift+\可以取消注释。

13、ctrl+d：删除当前行

删除当前行，这个很有用，我也是经常用的，尤其是在调试，删除当前错误，结合ctrl+z编辑撤销的快捷键，运用自如。

附上一些小窍门：

锁定命令行窗口：

在命令行视图中（Window ->Show View ->Other ->Basic ->Console），试试看用滚动锁定按钮来锁定控制台输出不要滚屏。

注：调试bug时蛮实用的！

使用分级布局：

在包浏览视图（Package Explorer view）中默认的布局（扁平式）方式，它把包的全名显示在导航树（navigation tree）中（我平时喜欢这样字看，尤其运维老项目的时候）。

有些情况下比较喜欢分级布局，不显示那么长的包名，即Eclipse中的分级布局（Hierarchical Layout）。

要切换到这种模式，点击包浏览视图中向下的按钮，选择布局（Layout），然后选择分级（Hierarchial）。

注4：其他参考，我把自己常用到快捷键组合的加粗，与上文重复的忽略

注5：大家如果有发现本文中有好用但是未被我用起来的请留言，或是推荐些其他学习资源，谢谢。

Eclipse常用快捷键

1几个最重要的快捷键

代码助手:Ctrl + Space（简体中文操作系统是Alt+/）
快速修正：Ctrl + 1
单词补全：Alt+/
打开外部Java文档：Shift+F2

显示搜索对话框：C rl+H
快速Outline：Ctrl+O
打开资源：Ctrl+Shift+R
打开类型：Ctrl+Shift+T

显示重构菜单：Alt+Shift+T

上一个/下一个光标的位置：Alt+Left/Right
上一个/下一个成员（成员对象或成员函数）：Ctrl+Shift+Up/Down
选中闭合元素：Alt+Shift+Up/Down/Left/Right( failed )
删除行：Ctrl+D

在当前行上插入一行：Ctrl+Shift+Enter
在当前行下插入一行： Shift+Enter
上下移动选中的行：Alt+Up/Down(failed)
组织导入：Ctrl+Shift+O(failed)

2 定位

2.1行内定位
行末/行首：End/Home
前一个/后一个单词：Ctrl+Right/Left

2.2文件内定位
跳到某行：Ctrl+L
上下滚屏：Ctrl+Up/Down
上一个/下一个成员（成员对象或成员函数）：Ctrl+Shift+Up/Down
快速Outline：Ctrl+O

2.3跨文件定位
打开声明：F3 (fn + F3)
打开资源：Ctrl+Shift+R
打开类型：Ctrl+Shift+T
在workspace中搜索选中元素的声明：Ctrl+G
在workspace中搜索选中的文本：Ctrl+Alt+G
在workspace中搜索选中元素的引用：Ctrl+Shift+G
* 打开调用层次结构：Ctrl+Alt+H
快速层次结构：Ctrl+T
怎么理解层次结构？
2.4其它
上一个/下一个光标所在位置：Alt+Left/Right
上一个编辑的位置：Ctrl+Q

3 选中
3.1行内选中
选中到行末/行首：Shift+End/Home
选中上一个/下一个单词：Ctrl+Shift+Left/Right

3.2文件内选中
选中闭合元素：Alt+Shift+Up (光标需要定位在代码块 } 末尾， 否则之选中当前行)
恢复到上一个选中：Alt+Shift+Down（faile）
选中下一个/上一个元素：Alt+Shift+Right/Left

4 定位/选中/操作同时
删除行：Ctrl+D
删除下一个/上一个单词：Ctrl+Delete/Backspace
删除到行末：Ctrl+Shift+Delete
在当前行上插入一行：Ctrl+Shift+Enter
在当前行下插入一行： Shift+Enter
上下移动选中的行：Alt+Up/Down
拷贝选中的行：Ctrl+Alt+Up/Down

5 其它的代码编辑类快捷键
保存：Ctrl+S
保存所有：Ctrl+Shift+S
下一个命中的项（搜索之后）：Ctrl + .
注释：Ctrl + /
添加导入：Ctrl+Shift+M
显示快捷键帮助：Ctrl+Shift+L
变为大/小写：Ctrl+Shift+X/Y

6 重构
显示重构菜单：Alt+Shift+T
重构-改变方法签名：Alt+Shift+C
重构-移动：Alt+Shift+V
重构-重命名：Alt+Shift+R

7 编辑器、视图、透视图切换
下一个编辑器：Ctrl+F6
下一个视图：Ctrl+F7
下一个透视图：Ctrl+F8
最大化当前视图或编辑器：Ctrl+M
激活编辑器：F12

8 Debug
F5：Step Into（debug）
F6：Step over（debug）
F7：Step return（debug）
F8：Resume（debug）
F11：debug上一个应用（debug）

9 Up/Down/Right/Left类快捷键
Ctrl
前一个/后一个单词：Ctrl+Right/Left
上下滚屏：Ctrl+Up/Down
Alt
上一个/下一个光标的位置：Alt+Left/Right
上下移动选中的行：Alt+Up/Down
Shift
选中上一个/下一个字符：Shift+Left/Right
选中上一行/下一行（从当前光标位置开始）：Shift+Up/Down
Ctrl+Shift
上一个/下一个成员（成员对象或成员函数）：Ctrl+Shift+Up/Down
选中上一个/下一个单词：Ctrl+Shift+Left/Right
Alt+Shift
选中闭合元素：Alt+Shift+Up
恢复到上一个选中：Alt+Shift+Down
选中下一个/上一个元素：Alt+Shift+Right/Left
拷贝选中的行：Ctrl+Alt+Up/Down
Ctrl+Alt
拷贝选中的行：Ctrl+Alt+Up/Down

10 F类快捷键 ( fn + )
F2：显示提示/重命名
F3：打开选中元素的声明
F4：打开选中元素的类型继承结构
F5：刷新 (fn + F5)
F5：Step Into（debug）
F6：Step over（debug）
F7：Step return（debug）
F8：Resume（debug）
F11：debug上一个应用（debug）
F12：激活编辑器( failed )*/

自动补全：Alt+/
成员方法Generate Getters and Setters: Alt+Shift+S+r+Tab+Enter+Tab*4+Enter==>
带参构造方法Generate Constructor using Fields: Alt+Shift+S+o==>
无参构造方法Generate Constructors from Superclass: Alt+Shift+S+c==>
字符串格式化Generate toString: Alt+Shift+S+s
代码格式化：ctrl+shift+f
Ctrl+Alt+方向上下键：复制高亮显示的一行或多行
快速导包：Ctrl+Shift+o/m
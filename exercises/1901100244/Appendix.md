# Python 自学训练营 010 期 沈璜 日志 附录

<!-- 本文档用于记录一些与任务关联不大，但值得记录的内容。 -->

## Markdown 相关信息

在 GitHub 上写文档建议使用 Markdown 格式，这是一种“轻量级标记语言”，其设计目的是为了让人们“使用易读易写的纯文本格式编写文档，然后转换成有效的 XHTML（或者 HTML）文档”。

简单地说，Markdown 格式就是为了给纯文本格式的文档快速地添加一些格式化标记（比如标题、粗体、斜体、引用、链接等等）所用的一种格式。Markdown 文档使用“`.md`”扩展名，其实质还是文本文档，只是把文本文档的“`.txt`”扩展名换成“`.md`”罢了。

### 1. 相对完善的资料

Markdown 最基础也是最核心的资料，当属由 Markdown 格式创始人[约翰·格鲁伯](https://zh.wikipedia.org/wiki/約翰·格魯伯)（[John Gruber](https://en.wikipedia.org/wiki/John_Gruber)）公布在 Markdown 项目网站（<https://daringfireball.net/projects/markdown/>）上的讯息，在项目网站上，约翰·格鲁伯给出了 [Markdown 格式的基本用法](https://daringfireball.net/projects/markdown/basics)以及[Markdown 格式的详细语法](https://daringfireball.net/projects/markdown/syntax)，他还做了一个[在线转换器](https://daringfireball.net/projects/markdown/dingus)，可以简单地把 Markdown 格式文本转换成 HTML 格式文本，同时预览浏览器显示的样子。

不过，因为约翰·格鲁伯表示“Markdown 是一种书写格式，而不是一种发布格式”，且他允许不同的平台和应用根据需要对 Markdown 进行调整，使得 Markdown 出现了比其他计算机语言严重得多的“方言现象”。具体的表现是⸺在某个地方可以使用的写法，在另一个地方识别不出来。

这种现实使得我们在使用 Markdown 撰写文档的时候，要知道所用的平台具体支持哪些标记，否则就可能出现“辛辛苦苦写半天，渲染根本不出现”的情况。

具体到 GitHub 上，由于 GitHub 使用了自有的扩展语法“GitHub Flavored Markdown（简称 GFM）”，所以除了 Markdown 官方网站之外，还应该阅读一下 GitHub 的《[关于在 GitHub 上编写和设置格式](https://help.github.com/cn/articles/about-writing-and-formatting-on-github)》（[*About writing and formatting on GitHub*](https://help.github.com/en/articles/about-writing-and-formatting-on-github)）、《[基本撰写和格式语法](https://help.github.com/cn/articles/basic-writing-and-formatting-syntax#paragraphs-and-line-breaks)》（[*Basic writing and formatting syntax*](https://help.github.com/en/articles/basic-writing-and-formatting-syntax#ignoring-markdown-formatting)）、《[使用高级格式](https://help.github.com/cn/articles/working-with-advanced-formatting)》（[*Working with advanced formatting*](https://help.github.com/en/articles/working-with-advanced-formatting)）等文档中的内容。  
（注意，这些文档的中文翻译版或有错漏，阅读出现疑问时，可参看原始的英文版。）

GitHub 为 Markdown 扩展了许多有价值的功能，比如通过键入 `:EMOJICODE:` 来插入表情符号（键入 `:+1:` 来插入 :+1: ，键入 `:smile:` 来插入 :smile: 等，完整列表可以参看《[表情符号备忘录](https://www.webfx.com/tools/emoji-cheat-sheet/)》），再比如通过在围栏代码块标记（` ``` `）上添加语言标识符（`Python`、`JAVA`、`C`等）实现代码高亮等等。

GitHub 在《[GitHub Flavored Markdown 规范](https://github.github.com/gfm/)》中诠释了这一扩展语法的设计构思和细节，有余暇的时候也值得细读。

另外，[毕小朋](http://www.bixiaofan.com/)著，电子工业出版社出版的《了不起的 Markdown》也是值得一看的参考读物，里面除了介绍常见的 Markdown 语法外，还讲解了相关应用（Typora、VS Code、reveal.js 等）的使用细节。  
这本书的相关信息⸺  
在线试读：[百度阅读](https://yuedu.baidu.com/ebook/f2ec7e699a6648d7c1c708a1284ac850ad020418)、[CSDN 博客](https://blog.csdn.net/wirelessqa)；  
纸质版购买：[京东](https://item.jd.com/53604404106.html)、[天猫](https://detail.tmall.com/item.htm?id=599460988844)；  
电子版购买：[亚马逊](https://www.amazon.cn/dp/B07W2ZN8TM)。

### 2. 使用时的细节

#### 2.1. 软件配置

如果是一般性地使用 Markdown，那么直接下载安装 [Typora](https://typora.io/) 即可，下载页面：<https://typora.io/#download>。

安装后的具体设置和使用可以参考《[Typora：简单高效的 Markdown 编辑器](https://blog.csdn.net/wirelessqa/article/details/70432631)》一文，也可以参考《[了不起的 Markdown](https://www.amazon.cn/dp/B07W2ZN8TM)》中的相关章节。

如果是为了和 GitHub 联动而使用 Markdown，那么使用 [Visual Studio Code](https://code.visualstudio.com/)（简称 VS Code）编写 Markdown 可能会更顺手。

如果成功安装过 [Anaconda](https://www.anaconda.com/distribution/)，那么 VS Code 就应该一并安装了。也可以直接从 VS Code 的官方页面（<https://code.visualstudio.com/>）下载 VS Code 的安装包后单独安装。

VS Code 强大的一点是其可以安装大量的插件，安装方法是：

1. 使用快捷键 <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>X</kbd>（Windows）或 <kbd>⌘ Command</kbd> + <kbd>⇧ Shift</kbd> + <kbd>X</kbd>（macOS） 进入插件市场；
2. 在搜索框中输入计划安装插件的关键字；
3. 在搜索结果中点击插件名，会出现插件的详情页；
4. 在详情页点击“Install”安装插件；
5. 重启 VS Code。

如果对 VS Code 界面的颜色、图标、字体等不大满意，可以安装不同的主题（Theme）插件进行美化，在插件市场里搜索“Theme”就可以找到不少，还可以通过 [VSCodeThemes](https://vscodethemes.com/) 网站进行预览、对比、安装。建议主要写代码（后端工作）时使用深色主题，保护视力；主要写网页（前端工作）时使用浅色主题，避免在编辑器和预览页面反复切换时出现闪烁，减少对眼睛的刺激。

我所安装的插件有：

- VS Code 中文（简体）语言包
  - [Chinese (Simplified) Language Pack for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans)
- Markdown 相关
  - [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced)
  - [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
  - [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)
  - [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
  - [Github Markdown Preview](https://marketplace.visualstudio.com/items?itemName=bierner.github-markdown-preview)
  - [Markdown Emoji](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-emoji)
  - [Markdown Checkboxes](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-checkbox)
- 界面美化
  - [One Dark Pro](https://marketplace.visualstudio.com/items?itemName=zhuangtongfa.Material-theme)
  - [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme)
  - [Material Theme](https://marketplace.visualstudio.com/items?itemName=Equinusocio.vsc-material-theme)
  - [Atom One Light Theme](https://marketplace.visualstudio.com/items?itemName=akamud.vscode-theme-onelight)
  - [GitHub Plus Theme](https://marketplace.visualstudio.com/items?itemName=thenikso.github-plus-theme)
- 快捷键
  - [IntelliJ IDEA Keybindings](https://marketplace.visualstudio.com/items?itemName=k--kato.intellij-idea-keybindings)

我现在通常使用 VS Code 撰写 Markdown 文档，使用 Typora 阅读 Markdown 文档。

#### 2.2. 使用技巧

其实官方文档几乎已经涵盖了应该知道的各个方面，不过还是有些特别的细节需要单独做做功课。

##### 2.2.1. 一些应当在意的操作

- **尽量不要在 Markdown 里掺杂 HTML 和 CSS**  
  由于 Markdown 显示的时候会将原始文本转换成 HTML，所以理论上来讲，任何通过 HTML 和 CSS 可以呈现，但 Markdown 尚未支持的表现，都可以使用直接在 Markdown 文档中写入 HTML 和 CSS 代码的方式来实现，约翰·格鲁伯也明确了这种做法没有问题。  
  但是如果不加限制地在 Markdown 文档中写入 HTML 和 CSS 代码，会违背 Markdown 设计时“易读易写”的初衷，所以还是应该避免这种用法。  
  而且 GitHub 为了安全，其上展示的 Markdown 文档中的 HTML 格式标签和 CSS 样式都会被去除。我曾经试着用“内联式 CSS 样式”和“HTML 格式标签”设定字体字号、设定文字颜色、添加下划线、控制换行等等，在 VS Code 里渲染没有问题，贴到 GitHub 里就都不见了。  
  这个问题网上也有不少讨论，比如在《》⸺在 GitHub 上，你想给文字加个特定颜色的高亮，都没有正常途径。  
  可能 GitHub 是这么想的：我们都把表情符号给你们了，就别把文档涂得花花绿绿了吧？
- **GitHub 不支持的一些 Markdown 语法**  
  - 下划线
  - 删除线
  - 强调
  - 脚注
    - [Markdown 的注脚问题](https://segmentfault.com/q/1010000000464492)
    - [markdown 为什么不支持目录和脚注？](https://www.zhihu.com/question/21907056)  
- **通过 GitHub 提供的预览（Preview）明确显示效果**  
  我们通常都是在

##### 换行

##### 引用

##### 字符

标点
    撇号、引号、括号、省略号、破折号（⸺）
[不离不弃的破折号](https://thetype.com/2019/03/14918/#pozhehao-typography)

空格

- **不同类型空格在不同场景中的使用**  
  - 首行缩进  
    按照一般书籍的习惯，中文文本的每个自然段首行应该缩进两个字，但在互联网上，大量文本的呈现形式是每段顶格，段间空行，到底哪种方式好，多年间有过很多讨论。对此有兴趣的可以阅读知乎上“[写文章时段首空两格是从何时开始的？为什么这样设计？](https://www.zhihu.com/question/19572531)”这个问题下面的内容，以及

Unicode 字符

##### 链接

参见：  
[Markdown Syntax](https://github.com/fan2/Markdown/blob/master/Markdown%20Syntax.md)

##### 图片

经测试，GitHub 上 Markdown 文档中的图片尺寸可以调整！  
  使用 `<img>` 标签，用类似这样的写法即可： `<img src="https://raw.githubusercontent.com/shen-huang/img/master/2019-08/Good_Cheap_Fast_Trilemma.gif" width="200px" alt="质量_价格_速度_不可能三角" />`。
  对比一下：
  <img src="https://raw.githubusercontent.com/shen-huang/img/master/2019-08/Good_Cheap_Fast_Trilemma.gif" alt="质量_价格_速度_不可能三角" />
  <img src="https://raw.githubusercontent.com/shen-huang/img/master/2019-08/Good_Cheap_Fast_Trilemma.gif" width="200px" alt="质量_价格_速度_不可能三角" />
  注意！只能用 `<img>` 标签的属性进行设置，通过 CSS 样式是设置不了的！如 `<img src="https://raw.githubusercontent.com/shen-huang/img/master/2019-08/Good_Cheap_Fast_Trilemma.gif" style="width:200px;" alt="质量_价格_速度_不可能三角" />` 这样，是不行的！

在代码格式（`code`）中贴图
`<code>...</code>` 中可以使用 Markdown 贴图语法

给图片加链接  
双层嵌套即可，如 `[![Windows site](https://raw.githubusercontent.com/shen-huang/img/master/Logo/Windows_logo_2012-Black_12px.svg?sanitize=true)](http://windows.com)` 显示为 [![Windows Logo](https://raw.githubusercontent.com/shen-huang/img/master/Logo/Windows_logo_2012-Black_12px.svg?sanitize=true)](http://windows.com)  
也可以使用 Markdown 引用链接贴图语法，如 `[![Windows site][Windows_Logo_12px]](http://windows.com)` 显示为 [![Windows site][Windows_Logo_12px]](http://windows.com)

##### 列表

可以用 Stylus 实现多级有序列表编号，Markdown 要有对应的写法，不是很好搞。

##### 代码

在代码格式（`code`）中使用斜体和粗体

##### 按键

使用 `<kbd>...</kbd>` 可以渲染出按键的效果。

在按键格式（`<kbd>...<kbd>`）中贴图  
`<kbd>...<kbd>` 中可以使用 Markdown 贴图语法  
如 `<kbd>![Win][Windows_Logo_12px] Win</kbd>` 显示为 <kbd>![Win][Windows_Logo_12px] Win</kbd>

##### 表格

##### 注释

可以使用 HTML 的注释方式 `<!--  -->`，注意这种方式无法嵌套注释。

另外可以利用空链接和引用链接的方式添加注释，注释中不能有一般的空格（“ ”）和非断开空格（“ ”），但可以使用 Figure space（“ ”）、Thin space（“ ”）、Narrow no-break space（“ ”）、Hair space（“ ”）。

参见：  
[在 Markdown 中写注释](https://www.imooc.com/article/23400)  
[如何在 Markdown 注释一段文字](https://www.jianshu.com/p/9be87e7e15bf)  
[syntax - Comments in Markdown - Stack Overflow](http://stackoverflow.com/questions/4823468/comments-in-markdown)  
[如何在 Github Flavored Markdown 中添加内联注释？](https://codeday.me/bug/20190228/716555.html)

##### 徽章

参见：
[GitHub 项目徽章的添加和设置](https://github.com/EyreFree/EFArticles/blob/master/source/_posts/GitHub-Badge-Introduction.markdown)  
[为你的 GitHub 生成漂亮的徽章和进度条](https://shikieiki.github.io/2017/03/01/为你的Github生成漂亮的徽章和进度条/)  
[徽章系列文章](http://www.gdky005.com/categories/shields/)  

##### 样式

虽然 GitHub 显示 Markdown 文档的时候会把各种自定样式都去掉，但我们还是可以利用 HTML 标签配合 Stylus 插件的方式进行一些样式调整的。  

GitHub 接受的 HTML 标签有：

```Text
h1 h2 h3 h4 h5 h6 h7 h8 br b i strong em a pre code img tt div ins del 
sup sub p ol ul table thead tbody tfoot blockquote dl dt dd kbd q samp 
var hr ruby rt rp li tr td th s strike summary details caption figure 
figcaption abbr bdo cite dfn mark small span time wbr
```

这其中 `b` 和 `i` 基本上是不会使用的（通常使用 `strong` 和 `em`），而 `span` 本身就是用来添加样式的。故可以用 `<span><i>...</i></span>` 来标记一段文本，再用 Stylus 给 `span i` 设定格式就行了。`<span><b>...</b></span>` 按理也可以这样操作，但若是照搬 `<span><i>...</i></span>` 的 CSS 设置，会导致标记文字的粗体无法取消，我试验了 `<span><span>...</span></span>`，发现会意外地匹配上页面别的部分， `<span><span><span>...</span></span></span>` 也不好用，最后发现是 `span b` 和 `span i` 的 CSS 设置有分别，想要去掉标签原本默认的效果，`span i` 要设置 `font-style: normal; `，`span b` 则要设置 `font-weight: normal; `。如果

我使用了：

```CSS
span i {font-style: normal; color: #444444; font-size: 87.5% !important;}
span b {font-style: normal; font-weight: normal; background-color: #ffff00; }
```

[How to display HTML content in github README.md?](https://stackoverflow.com/questions/14951321/how-to-display-html-content-in-github-readme-md)  
[sanitization_filter](https://github.com/jch/html-pipeline/blob/master/lib/html/pipeline/sanitization_filter.rb#L44-L48)  
[HTML <span> 标签](https://www.w3school.com.cn/tags/tag_span.asp)  
[CSS 选择器参考手册](https://www.w3school.com.cn/cssref/css_selectors.asp)  
[CSS 的 ID 和 Class 有什么区别？如何正确使用它们？](https://www.zhihu.com/question/19550864)  
[GitHub README 文件语法解读](https://github.com/guodongxiaren/README#diff%E8%AF%AD%E6%B3%95)

##### 目录

##### 转换

Markdown 与其他格式的转换
[Markdown 格式如何转换成 Word？](https://www.zhihu.com/question/22972843)
Pandoc
Markdown 输出质量可靠的 PDF（参见 吐槽 部分 “复制任务手册中的文本总会出现重复的字”）

### 3. 其他参考内容

- [Markdown](https://daringfireball.net/projects/markdown/)
- [Markdown: Basics](https://daringfireball.net/projects/markdown/basics)
- [Markdown: Syntax](https://daringfireball.net/projects/markdown/syntax)
- [关于在 GitHub 上编写和设置格式](https://help.github.com/cn/articles/about-writing-and-formatting-on-github)
  - [About writing and formatting on GitHub](https://help.github.com/en/articles/about-writing-and-formatting-on-github)
- [基本撰写和格式语法](https://help.github.com/cn/articles/basic-writing-and-formatting-syntax#paragraphs-and-line-breaks)
  - [Basic writing and formatting syntax](https://help.github.com/en/articles/basic-writing-and-formatting-syntax#ignoring-markdown-formatting)
- [使用高级格式](https://help.github.com/cn/articles/working-with-advanced-formatting)
  - [Working with advanced formatting](https://help.github.com/en/articles/working-with-advanced-formatting)
- [Markdown 语法指南](http://www.ghostchina.com/markdown-guide/)  
- []
- [学习 Markdown](http://amwiki.org/doc/?file=020-教程学习篇/005-学习markdown/01-Markdown快速开始)
- [了不起的 Markdown](https://www.amazon.cn/dp/B07W2ZN8TM)
- [反思 Markdown：Markdown 的长与短](https://sspai.com/post/37340)  
- [Markdown 格式如何转换成 Word？](https://www.zhihu.com/question/22972843)
- [Markdown, Please! 将任意网页转换为 Markdown 格式](https://www.appinn.com/markdown-please/)  
- [Org-mode、reST、 Markdown 各有什么优缺点？](https://www.zhihu.com/question/19851600)
- [神器 Org-mode](https://www.lijigang.com/blog/2018/08/08/神器-org-mode/)
- [一个博士生是怎么应用 Org-mode 的](https://github.com/lujun9972/emacs-document/blob/master/org-mode/一个博士生是怎么应用Org-mode的.org)

## GitHub 相关信息

参见：  
[GitHub Wiki 页面的添加和设置](https://github.com/EyreFree/EFArticles/blob/master/source/_posts/GitHub-Wiki-Introduction.markdown)  

## 常见图片格式

### 1. 图片显示的原理

### 2. 图片格式分类

#### 2.1. 按画质损失情况分类

#### 2.2. 按内容构建方式分类

### 3. 常见图片格式

## 命令行相关信息

### 1. 历史

CLI 和 GUI 的历史沿革。

### 2. 使用

#### 2.1. 计算机主要操作系统所带的命令行类工具

#### 2.2. Windows

##### 2.2.1. 命令提示符

###### 2.2.1.1. 进入

可以通过如下几种方式进入命令提示符（任选其一）：

- 依次点击【![Win][Windows_Logo_12px] 开始】-【Windows 系统】-【命令提示符】
- 点击【![Win][Windows_Logo_12px] 开始】- 输入 `CMD` - 按 <kbd>↵ Enter</kbd>
- 按 <kbd>![Win][Windows_Logo_8px] Win</kbd> - 输入 `CMD` - 按 <kbd>↵ Enter</kbd>
- 按 <kbd>![Win][Windows_Logo_8px] Win</kbd> + <kbd>R</kbd> - 输入 `CMD` - 按 <kbd>↵ Enter</kbd>

###### 2.2.1.2. 切换文件夹

##### 2.2.2. PowerShell

#### 2.3. macOS

#### 2.4. Linux

#### 2.5. Chrome OS

简而言之，尽量别用，相当费神。

### 3. 资料

[PowerShell 在线教程](https://www.pstips.net/powershell-online-tutorials)  
[告别 Windows 终端的难看难用，从改造 PowerShell 的外观开始](https://sspai.com/post/52868)  

## 软件、应用、程序、网站（Windows 平台）

为了正常访问 GitHub、Google 等网站，应该**避免安装中国大陆地区的各类“安全软件”、“浏览器”甚至“全家桶”**，为此，我觉得相应地提供一些细节上的建议是有必要的。由于个人主要使用 Windows 系统，所以本部分内容以 Windows 平台为主。

按使用类型分类，给出必装（★★★★★）、推荐（★★★★）、可用（★★★）、一般（★★）、回避（★）、禁绝（☆）六个级别的评价。

### 系统

- 安全防护
  - Defender ★★★★★
  - 火绒 ★★
  - 腾讯电脑管家 ★
  - 360 杀毒 ☆
  - 360 安全卫士 ☆
  - 金山毒霸 ☆
  - 金山卫士 ☆
  - 2345安全卫士 ☆
- 压缩
  - 7-Zip ★★★★
  - Bandizip ★★★★
  - WinRAR ★★★
  - 2345 好压 ☆
  - 快压 ☆
  - 360 压缩 ☆
- 输入法
  - 微软拼音输入法 ★★★★
  - 谷歌拼音输入法 ★★★
  - Rime 输入法 ★★★
  - 极点五笔输入法 ★★★
  - 黑马神拼输入法 ★★
  - 华宇拼音输入法 ★★
  - 拼音加加输入法 ★
  - 搜狗输入法 ★
  - QQ 输入法 ★
  - 百度输入法 ☆
  - 2345王牌输入法 ☆
  - 手心输入法 ☆
  - 极品五笔输入法 ☆
- 驱动
  - 驱动精灵 ☆
  - 驱动人生 ☆
  - 鲁大师 ☆

### 网络

- 浏览器  
  - Firefox
  - Chrome
  - Chromium 系
    - Vivaldi ★★★★★
    - Edge (based on Chromium) ★★★★
    - 百分浏览器 ★★★
    - 115 浏览器 ★★
    - Opera ☆
  - Edge ★★
  - Internet Explorer ★
  - 多引擎  
    通常是同时使用 Chromium 的 Blink（或 WebKit）排版引擎，和 Internet Explorer 的 Trident 排版引擎。
    - Avant 浏览器 ★★★
    - 傲游浏览器（Maxthon） ★
    - 搜狗浏览器 ☆
    - QQ 浏览器 ☆
    - 360 安全浏览器 ☆
    - 360 极速浏览器 ☆
    - UC 浏览器 ☆
    - 猎豹安全浏览器 ☆
    - 2345 加速浏览器 ☆
  - 浏览器插件和扩展
    - [MyChrome](https://github.com/cnjackchen/my-chrome) ★★★★★
    - [MyFirefox](https://github.com/cnjackchen/my-firefox) ★★★★★
    - Flash ★
- 下载
  - Internet Download Manager ★★★★

### 工作

- 套装
  - Microsoft Office 365 ★★★★★
  - Microsoft Office 2019 ★★★★
  - WPS Office ★

### 媒体

- 视频
- 音频
- 图片
  - ImageGlass ★★★★★
  - IrfanView ★★★★
  - XView ★★★
  - 2345 看图王 ☆

### 学习

### 娱乐

参考资料：  
[我最喜欢的软件 Windows 版 - 小众软件](https://love.appinn.com/)  
[精品绿色便携软件](https://www.portablesoft.org/)  
[善用佳软](https://xbeta.info/)  
[浏览器 user-agent 字符串的故事](https://www.cnblogs.com/ifantastic/p/3481231.html)  
[History of the browser user-agent string](https://webaim.org/blog/user-agent-string-history/)  
[List of User Agents](https://developers.whatismybrowser.com/useragents/explore/)  
[网页浏览器列表](https://zh.wikipedia.org/wiki/网页浏览器列表)  
[HTML5 test](http://HTML5test.com/)  
[如何评价2345？](https://www.zhihu.com/question/35188509)  
[为什么我放弃了 Chrome？](https://zhuanlan.zhihu.com/p/46205674)  

## 吐槽（？）

- 复制任务手册中的文本总会出现重复的字  
  用 Acrobat 打开 PDF 复制会有这种问题  
  用 Chrome 打开 PDF 再复制就（貌似）好了（并没有！）  
  似乎应该用 SumatraPDF 试试看会不会有同样的问题  
  Google 了“PDF 复制 多字”找到了这篇文章：<https://sspai.com/post/52073>  
  明确了有一部分多余的字属于 Unicode 的 “Kangxi Radicals”（康熙字典部首）区，编码范围是 U+2F00-U+2FDF  
  我先试着用  

  ```Python
    re.sub(r"[^\u0391-\uFFE5\n]", "", text)
  ```

  把双字节以外的内容去掉，  
  再用

  ```Python
    re.sub(r"[\u2F00-\u2FDF]", "", text)
  ```

  把康熙字典部首区的字符去掉。  
  可是去掉这个区域部分的字符后，还是有多余的字，我以为是代码编写或者操作有误，重复试了数次，又把多余的字拿去 Google，都没找出什么特别的信息。  
  我最后一个字一个字试，甚至动用了这样的代码：

  ```Python
    re.sub(r"""
        ⼀|⼁|⼂|⼃|⼄|⼅|⼆|⼇|⼈|⼉|⼊|⼋|⼌|⼍|⼎|⼏|
        ⼐|⼑|⼒|⼓|⼔|⼕|⼖|⼗|⼘|⼙|⼚|⼛|⼜|⼝|⼞|⼟|
        ⼠|⼡|⼢|⼣|⼤|⼥|⼦|⼧|⼨|⼩|⼪|⼫|⼬|⼭|⼮|⼯|
        ⼰|⼱|⼲|⼳|⼴|⼵|⼶|⼷|⼸|⼹|⼺|⼻|⼼|⼽|⼾|⼿|
        ⽀|⽁|⽂|⽃|⽄|⽅|⽆|⽇|⽈|⽉|⽊|⽋|⽌|⽍|⽎|⽏|
        ⽐|⽑|⽒|⽓|⽔|⽕|⽖|⽗|⽘|⽙|⽚|⽛|⽜|⽝|⽞|⽟|
        ⽠|⽡|⽢|⽣|⽤|⽥|⽦|⽧|⽨|⽩|⽪|⽫|⽬|⽭|⽮|⽯|
        ⽰|⽱|⽲|⽳|⽴|⽵|⽶|⽷|⽸|⽹|⽺|⽻|⽼|⽽|⽾|⽿|
        ⾀|⾁|⾂|⾃|⾄|⾅|⾆|⾇|⾈|⾉|⾊|⾋|⾌|⾍|⾎|⾏|
        ⾐|⾑|⾒|⾓|⾔|⾕|⾖|⾗|⾘|⾙|⾚|⾛|⾜|⾝|⾞|⾟|
        ⾠|⾡|⾢|⾣|⾤|⾥|⾦|⾧|⾨|⾩|⾪|⾫|⾬|⾭|⾮|⾯|
        ⾰|⾱|⾲|⾳|⾴|⾵|⾶|⾷|⾸|⾹|⾺|⾻|⾼|⾽|⾾|⾿|
        ⿀|⿁|⿂|⿃|⿄|⿅|⿆|⿇|⿈|⿉|⿊|⿋|⿌|⿍|⿎|⿏|
        ⿐|⿑|⿒|⿓|⿔|⿕|^\n
        """, "", textori2)
  ```

  然而还是不行。  
  沮丧之中，我意识到，我应该直接用 Python 查一下多余的字的代码。先是用了 `ord()`，发现输出的是所查字符的 UTF-16 的十进制数值，其实用这个就能继续了，但我没反应过来，觉着得找到 Unicode 编码才合用，搜索一番后知道了可以用 `str.encode('unicode_escape')` 和 `str.decode('unicode_escape')` 这一对编码/解码的方法查询 Unicode 编码，查了才知道，多出的这些字，在另一个 Unicode 区⸺“CJK Compatibility Ideographs”（中日韩兼容表意文字）区，编码范围是 U+F900–U+FAFF。  
  结合之前的代码，我试着用  

  ```Python
    re.sub(r"[\u2F00-\u2FDF]|[\uF900-\uFAFF]", "", text)
  ```

  进行清理，然后发现还有剩余，剩下的又是一个 Unicode 区⸺“CJK Radicals Supplement”（中日韩汉字部首补充）区，编码范围是 U+2E80–U+2EFF。  
  把这部分加上，我用

  ```Python
    re.sub(r"""
        [\u2E80-\u2EFF]|
        [\u2F00-\u2FDF]|
        [\uF900-\uFAFF]
        """, "", text)
  ```

  再清理了一次，这次终于是清理干净了。  
  由于“中日韩汉字部首补充区”和“康熙字典部首区”是连着的，所以上面的代码也可以简化成：

  ```Python
    re.sub(r"[\u2E80-\u2FDF]|[\uF900-\uFAFF]", "", text)
  ```

  另外，这次任务的文本似乎来自20世纪60年代（民国50年代）台湾地区的小学课本，不客气地讲，这个文本质量很一般，或可考虑使用“[愚公移山　列子](http://students.heungto.edu.hk/~chinese/upload_files/textread/f5/text/110.htm)”这个页面的文言文版本进行替换。
  “[中国寓言故事（Chinese Fable Story）](https://fanfanchinese.weebly.com/200132226923507353282592520107-fable-story.html)”

  参考资料：  
  [PDF 复制中的文字重复问题](https://sspai.com/post/52073)  
  [康熙部首（Kangxi Radicals，U+2F00-U+2FDF）](http://chukaml.tripod.com/unicode/han/U2F00.html)  
  [python encode和decode函数说明](https://www.cnblogs.com/evening/archive/2012/04/19/2457440.html)  
  [不得不知道的Python字符串编码相关的知识](https://www.cnblogs.com/Xjng/p/5093905.html)  
  [Python 官方文档《内置类型》的“encode”和“decode”部分](https://docs.python.org/zh-cn/3/library/stdtypes.html?highlight=encode#str.encode)  
  [Python 官方文档《codecs ⸺ 编解码器注册和相关基类》](https://docs.python.org/zh-cn/3/library/codecs.html#standard-encodings)
  [Python 3 中如何得到 Unicode 码对应的中文？](https://www.zhihu.com/question/26921730)  
  [Unicode字符百科](https://unicode-table.com/cn/)  
  [decodeunicode – the world’s writing systems](https://decodeunicode.org/)  
  [维基百科的“Unicode 字符列表”页面](https://zh.wikipedia.org/wiki/Unicode字符列表)  
  [维基百科的“中日韩兼容表意文字”页面](https://zh.wikipedia.org/wiki/中日韓相容表意文字)  
  [维基百科的“中日韩汉字部首补充”页面](https://zh.wikipedia.org/wiki/中日韩汉字部首补充)  
  [维基百科的“康熙部首（Kangxi radical）”页面](https://en.wikipedia.org/wiki/Kangxi_radical)  
  [Python 正则表达式 字符串的匹配、替换、分割、查找](https://blog.csdn.net/u011138533/article/details/62904006)

## 搜索问题汇总

在与同学们交流的过程中，我发现很多人的问题都是“不擅搜索”，这让我意识到，把我遇到问题时我尝试的关键字记录一下，可能也有些参考价值。

根据主题大略归了一下类，内部的顺序就不细调了，基本是根据时间先后记录的。

- **GitHub 相关**
  - GitHub Desktop 登出
  - GitHub 太慢
  - GitHub Desktop 很慢
  - GitHub 代理
  - GitHub Desktop 全局代理
  - GitHub fastly.net
  - GitHub 私有库
  - GitHub 私有库 协作者 设置
  - GitHub 删除文件
  - GitHub 回滚
  - GitHub 创建文件夹
  - GitHub 创建空文件夹
  - GitHub 安装 git
  - Pull Request
  - GitHub fork 同步
  - fetch 分支
  - GitHub Desktop fork 更新
  - GitHub README.md image
  - 把 GitHub 当图床
  - GitHub Pull Request 撤回
  - GitHub 下载后同步
  - GitHub Issue 添加标签
  - GitHub 使用 Org-mode
  - GitHub 使用 reST
  - GitHub md 格式切换
  - GitHub 可用的文本格式
- **Anaconda 相关**
  - Anaconda
  - Anaconda 2 3 关系
  - Anaconda 安装 git
  - Anaconda PATH 设定
  - Anaconda Python module path
  - Anaconda Scripts Folder
  - conda 代理
  - conda 代理 InvalidTypeError: Parameter proxy_servers
  - pip Windows Proxy
  - the ssl module in Python is not available
  - pip trusted-host
- **Python 相关**
  - Python Hello World
  - Python 输入参数
  - Python input
  - Python Calculator
  - Python print 格式化
  - Python 注释
  - Python 计算器
  - Python eval
  - Python eval math
  - ast.literal_eval
  - ast is not defined python 3
  - Python eval site:docs.python.org
  - Python 报错 输出
  - Python try except else
  - Python 退出进程
  - Python 字符串
  - Python input 字符串
  - Python 无限循环
  - Python sin cos
  - Python 乘方
  - Python 替换文件内容
  - Python split
  - Python split 多个分隔符
  - re.split 多个空格
  - Python import
  - Python 多重替换
  - Python 正则表达式
  - unresolved import math
  - Python module path
  - Python 字符串替换 正则表达式
  - Python 字符串 两个空格替换成一个空格
  - Python 3 字符串 两个空格替换成一个空格
  - Python 3 字符串 去掉行首空格
  - Python re.sub(r'\s\s', r'\s', a) error
  - Python 正则表达式 空格
  - Python 去掉集合中的空格
  - Python 去掉 list 中元素里的空格
  - Python 字符串 大小写转换
  - Python 字符串 大小写翻转
  - Python swapcase
  - Python 2.7 UTF-8
  - Python import
  - Python import 大括号
  - Python 大括号
  - Python break
  - Python continue
  - 正则表达式 汉字 全角符号
  - 正则表达式 不区分大小写
  - Python 修改字典的 key
  - Python dict.pop
  - Python dict["c"] = dict.pop["a"]
  - Python 字典 输出 格式
  - Python 正则表达式 寻找
  - Python 字符 查询 Unicode
  - Python encode decode
  - Python encode decode unicode escape
  - Python 3 decode unicode
  - Python lambda
  - Python items()
  - Python 列表 合并
  - Python 列表推导式
  - 正则表达式 贪婪模式
  - Python print 输出重定向
  - Python 调用类中的函数
- **Windows 系统相关**
  - 右键 加入 命令提示符
  - py 命令无法运行
  - py -3 --version
  - Windows 命令提示符 命令
  - CMD 命令速查手册
  - PowerShell
- **其他系统相关**
  - Linux 命令提示符
  - Linux Shell
  - Linux bash
- **Markdown 相关**
  - Markdown
  - Typora
  - LaTeX
  - 负号
  - −
  - 网页 破折号 不断
  - ⸺
  - HTML 注释
  - Markdown 多级有序列表
  - Markdown 代码块 斜体
  - Markdown 代码块 HTML
  - Org-mode
  - Markdown 对比
  - \# -\*- coding: UTF-8 -\*-
  - Markdown 内嵌 CSS
  - Markdown 使用 CSS
  - Markdown 自定义 CSS
  - 李笑来 CSS
  - HTML 内嵌 CSS
  - GitHub Markdown CSS
  - GitHub Markdown CSS 使用
  - GitHub Markdown color
  - GitHub Markdown underline
  - Markdown 着重号
  - Markdown 代码高亮
  - Markdown 不间断空格
  - 零宽空格
  - HTML 着重号
  - HTML 格式化
  - HTML 字体颜色
  - HTML font
  - CSS 着重号
  - CSS 颜色名称
  - CSS 内联
  - Markdown 图片
  - Markdown 图片大小
  - HTML 注释 嵌套
  - HTML 注释 行内
  - HTML img 标签
  - HTML span
  - HTML pre
  - CSS class id 区别
  - CSS 选择器
  - HTML ins
  - CSS font style
  - CSS 去掉 \<b\> 加粗
  - Stylus
- **VS Code**
  - VS Code 字体设置
  - VS Code Python 调试
  - VS Code 纵向选择
  - VS Code Markdown
  - VS Code 亮色主题
- **Jupyter 相关**
  - Jupyter 用特定浏览器
  - Jupyter Anaconda 无法启动
- **浏览器相关**
  - Kinza 浏览器
  - Kinza 自定义文件夹
  - Kinza portable
  - Chromium
  - SRWare Iron folder
  - SRWare Iron install folder
  - SRWare Iron install path
  - Eversync
  - Edge Chromium
  - Chrome Better History
- **其他**
  - selfteaching
  - 自学是一种社交
  - 话语
  - 病句
  - Windows 10 32位
  - Windows 10 1903 32位
  - 64 bit
  - Windows 10 1903 64 bit
  - Windows 10 LTSC 企业版
  - Fluent Design System
  - Hello World
  - The Zen of Python, by Tim Peters
  - 今日割五城，明日割十城，然后得一夕安寝。起视四境，而秦兵又至矣。
  - 目标 用词 掌握 了解 认知 识别
  - PDF 阅读器
  - 撇号 英文 使用
  - Apostrophe 字体
  - Unicode 2019
  - Apostrophe Unicode 2019 宽度
  - CodeSandbox
  - UNPKG
  - build 软件
  - build software
  - 中文 首行空两格 段间空一行
  - 自然段开头空两格
  - 首行缩进 排版 规范
  - 首行缩进 国家标准
  - PDF 复制 多字
  - Kangxi Radicals
  - Kangxi Radicals unicode
  - CJK Compatibility Ideographs
  - CJK Radicals Supplement
  - Python 字符 整数值
  - ⾏行行
  - Unicode 编码表
  - A Google a day
  - 不可能三角
  - Unicode 五角星
  - 互联网档案馆
  - Library Genesis
  - Project Fi
  - clowwindy
  - 学习一个
  - 安全评测网站
  - AV TEST
  - Alexa 排名 世界
  - 不间断空格
  - Non-breaking space

<!-- 复用的图片和链接 -->

<!-- ![Win][Windows_Logo_20px]![Win][Windows_Logo_16px]![Win][Windows_Logo_12px]![Win][Windows_Logo_8px]![Win][Windows_Logo_6px] -->

[Windows_Logo_20px]: https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Windows_logo_2012-Black.svg/20px-Windows_logo_2012-Black.svg.png
[Windows_Logo_16px]: https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Windows_logo_2012-Black.svg/16px-Windows_logo_2012-Black.svg.png
[Windows_Logo_12px]: https://raw.githubusercontent.com/shen-huang/img/master/Logo/Windows_logo_2012-Black_12px.svg?sanitize=true
[Windows_Logo_8px]: https://raw.githubusercontent.com/shen-huang/img/master/Logo/Windows_logo_2012-Black_8px.svg?sanitize=true
[Windows_Logo_6px]: https://raw.githubusercontent.com/shen-huang/img/master/Logo/Windows_logo_2012-Black_6px.svg?sanitize=true
# 使用完整的互联网

正常访问 GitHub 和 Google 是个难点。

数年间我为此耗费了无数时间，试过的各种方案和服务都有两位数了，现在多少有点心得。

## 一、完美不存在

首先要理解的，是这类服务中，价格、速度、流量三者，最多只能同时取其二。

价格便宜速度快，流量肯定少；速度飞快流量多，价格肯定贵；流量超大价格低，速度肯定慢。

要是有哪家宣称自己价格低、速度快、流量多，那这家要么是做慈善的，要么是洗钱的，要么是钓鱼的，要么是骗人的，总之，不算正常。

这一情况，在经济学上叫“[三元悖论（Trilemma）](https://zh.wikipedia.org/wiki/三元悖论)”，也叫“不可能三角”，后来被拓展到了各种领域，进一步了解可以参考知乎这个问题：“[世界上有哪些不可能三角？](https://www.zhihu.com/question/265410886)”

这个动图相对直观地表现了这一问题：  
[](~![质量_价格_速度_不可能三角](https://raw.githubusercontent.com/shen-huang/img/master/2019-08/Good_Cheap_Fast_Trilemma.gif)  )<img src="https://raw.githubusercontent.com/shen-huang/img/master/2019-08/Good_Cheap_Fast_Trilemma.gif" width="200px" alt="质量_价格_速度_不可能三角" />

## 二、各人各需求

其次要明确的，是自己的实际需要。

如果只是少量地用 [Google](https://www.google.com/)、[维基百科](https://zh.wikipedia.org/)、[互联网档案馆](https://archive.org/)、[Library Genesis](http://gen.lib.rus.ec/) 等网站查询一些文字图片资料，那么价格和速度应该是主要考虑的要素，流量不是很重要。

如果是想顺畅地用 [Facebook](https://www.facebook.com/)、[Twitter](https://twitter.com/)、[Reddit](https://www.reddit.com/) 等网站，由于这些网站更新很快，上面还可能有不少图片和视频，所以在主要考虑价格和速度的基础上，也要考虑一下流量，甚至可以为了流量放宽一点对价格的限制。

如果是要频繁使用 [YouTube](https://www.youtube.com/)、[Twitch](https://www.twitch.tv/)、[Netflix](https://www.netflix.com) 等网站，那主要考虑的就应该是速度和流量了，特别是 Netflix 这样的，一定得明确服务商支持才能购入。

如果是打某款游戏，由于游戏对速度和延迟很敏感，应该用专门的游戏加速器，通用方案在游戏领域常常表现不佳。

还有一种情况，是要在非中国大陆地区用[优酷](https://www.youku.com/)、[爱奇艺](https://www.iqiyi.com/)、[网易云音乐](https://music.163.com/)之类服务的，需要服务商有“回国线路”才可以。

在各类特性的组合中，价格便宜流量多的那种服务往往比较鸡肋，简单地说⸺流量是多，可要是龟速，怎么用得完呢？

## 三、场景需明确

第三要搞清的，是自己的设备情况。

是单台 PC，还是 PC + Mac，又或是 PC + Mac + iPhone；是单一设备用，还是多设备一起用；是自家用，还是多家用，这些都是不一样的。

很多服务商限制设备数或者 IP，意思都差不多，就是同时有几个设备能用这个服务，通常短期超出一两台还可以，长期或者频繁或者大量超出限制，可能就会停止服务了，这类服务常常有没有退款条款，所以被停了也只能试着联系服务方，看对方能怎么处理，不开服也不退款也是可能的。

## 四、工具细选择

以上这些明确了，就到了选工具的环节了。

Windows、macOS、Linux、Android、iOS 等软件系统各有各的工具，有些差不多，有些差不少。

现在我个人用的主要工具，是 [Shadowsocks](https://github.com/shadowsocks)（[维基百科 Shadowsocks 介绍页](https://zh.wikipedia.org/wiki/Shadowsocks)），它是开源的，在 Windows、macOS、Linux、Android、iOS 上都有适配的免费客户端。

由于开源，Shadowsocks 衍生出了 ShadowsocksR，甚至在 Shadowsocks 原作者 clowwindy（[GitHub 页面](https://github.com/clowwindy)、[Twitter 页面](https://twitter.com/clowwindy)）和 ShadowsocksR 作者破娃酱（[GitHub 页面](https://github.com/breakwa11)、[Twitter 页面](https://twitter.com/breakwa11)）相继被迫放弃项目后，迅速有人接手，更进一步地衍生出了 ShadowsocksD（[Windows 版](https://github.com/TheCGDF/SSD-Windows)、[Android 版](https://github.com/TheCGDF/SSD-Android)）、[ShadowsocksRR](https://github.com/shadowsocksrr/shadowsocks-rss)、[Clash](https://github.com/Dreamacro/clash) 等项目。

Windows 上的 [Shadowsocks](https://github.com/shadowsocks) 使用起来并没有什么难度（可参考[项目页的使用说明](https://github.com/shadowsocks/shadowsocks-windows/wiki/Shadowsocks-Windows-使用说明)），如果觉得原版的界面不好用或者不好看，还可以使用 [Clash for Windows](https://github.com/Fndroid/clash_for_windows_pkg/releases)。

macOS 现在建议使用 [ClashX for macOS](https://github.com/yichengchen/clashX/releases)。

Android 可以从 [Shadowsocks Android 版 GitHub 发布页](https://github.com/shadowsocks/shadowsocks-android/releases)下载 `.apk` 文件，复制到设备里安装使用，也可使用 [Clash for Android](https://github.com/Kr328/ClashForAndroid)（可[通过 APKPure 进行安装](https://apkpure.com/store/apps/details?id=com.github.kr328.clash)，或从 [Clash for Android 的 Telegram 频道](https://t.me/clash_for_android_channel)获取 `.apk` 文件，复制到设备里安装）。

iOS 可以在 App Store 里搜“[Outline App](https://apps.apple.com/app/outline-app/id1356177741)”、“[Shadowrocket](https://apps.apple.com/app/shadowrocket/id932747118)”或者“[Quantumult X](https://apps.apple.com/app/quantumult-x/id1443988620)”安装使用，Outline App 是免费的，Shadowrocket 的功能比 Outline App 丰富些，现收费 \$2.99，Quantumult X 的功能比 Shadowrocket 又丰富些，现收费 \$7.99，都还可以接受，注意，下载安装需要有个非中国大陆区的 Apple 账户。

除了 Shadowsocks 外，还有不少其他的工具和方案可选。比如说我知道某位大佬使用 [Google Fi](https://fi.google.com/about) 来实现稳定访问全球互联网，不过这服务相当贵，一个月起价 \$20.00，只有 6 GB 的流量，超出之后 \$10.00/GB，最少计费单位 \$1.00 （我研究之后感觉大佬就是大佬，还是要学习一个，要努力提升自己），这种费用实在是不易落地；再比如我知道还有很多人在用 VPN，但 VPN 是全局的，启用后所有的网络连接全走 VPN 通道算流量，用起来不够灵活，还有，因为 VPN 连接特征鲜明，很容易被识别阻断，所以有些时候连接会不稳定；还有购买 VPS 然后用 SSH -D 转发流量的方案，但和 VPN 一样，因为其连接特征鲜明，很容易被识别阻断，根本不能稳定使用。综合考虑，我现在选择了 Shadowsocks。

## 五、搭配需谨慎

用 Shadowsocks 就会遇到选择服务商的问题，好在有位前辈专门做了相关的评测⸺毒药机场简介（<https://duyaoss.com/>，备用 GitHub 链接为 <https://github.com/DuyaoSS/SSR/issues/1>）。

在具体挑选哪家服务商这点上，我现在的观点是这样的：

1. 用 QQ、微信等工具做为主要服务咨询通道，甚至不提供服务咨询通道的服务商，就别用了；
2. 需要安装不常见的私有程序的服务商，就别用了；
3. 通过提供 VPN 实现功能的服务商，就别用了；
4. 提供“终身套餐”的服务商，就别用了；
5. 不在评测列表里的服务商，谨慎使用；
6. 月付比季付好，季付比年付好；
7. 比较熟悉的大牌服务商搞活动，可以谨慎购买；
8. 遇到天灾人祸跑路了，不必介怀，这属于国难；
9. 目的是使用完整的互联网，不要为路径耗费太多时间和精力。

:exclamation::exclamation::exclamation: 据我所知，用于正常访问 GitHub、Google 等网站的计算机（特别是 Windows 系统的），应该**避免**安装中国大陆地区的各类“安全软件”、“浏览器”甚至“全家桶”，包括但不限于：

- 360 系所有软件；
- 百度系所有软件；
- 2345 系所有软件；
- 金山系安全软件（其他软件也尽量别用）；
- 腾讯系安全软件。

（这些软件对上网有什么具体的影响，就不细说了。）

有些人可能担心安全问题，其实 Windows 10 自带的 Defender 防护能力非常强，在 [2019 年 6 月的 AV-TEST 评测](https://www.av-test.org/en/antivirus/home-windows/)上，Defender 已经成为“顶级产品”了，所以一般使用是不必另外安装安全软件的。

------

参考资料：  
[科学上网相关知识总结](https://crifan.github.io/scientific_network_summary/website/)  
[机场简介](https://github.com/DuyaoSS/SSR/issues/1)  
[不要使用 VPN 服务（Don't use VPN services.）](https://gist.github.com/joepie91/5a9909939e6ce7d09e29)  
[VPN ⸺ 非常不可靠的叙事（VPN ⸺ a Very Precarious Narrative）](https://schub.wtf/blog/2019/04/08/very-precarious-narrative.html)  
[Google 百度和谷歌的那些事](http://blog.devep.net/virushuo/2010/01/14/blog56google_blogtinyfool_1_go.html)  
[百度云安全让史上最强 DDoS 攻击消于无形](http://it.people.com.cn/n/2015/1026/c1009-27741637.html)[](~（中国新闻网的这篇稿有高级黑的感觉）)  
[谷歌 Play 商店允许中国开发者销售付费应用](http://game.people.com.cn/n/2014/1212/c48662-26194242.html)  
[Shadowsocks 的前世后生](http://www.chinagfw.org/2016/08/shadowsocks_31.html)  
[clowwindy 关于 Shadowsocks 的交流 Issue #293](https://github.com/shadowsocks/shadowsocks-windows/issues/293)  
[Clash for Windows 使用简介](https://10101.io/2018/10/27/how-to-use-clash-for-windows)  
[Quantumult X 不完全教程](https://www.notion.so/Quantumult-X-1d32ddc6e61c4892ad2ec5ea47f00917)  
[鲁迅都救不了，几个程序员就能救了？](https://zankyo.cc/1033/)
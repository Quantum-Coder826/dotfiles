### BepInEx Framework (Author: bbepis)

This is the pack of all the things you need to both start using mods, and start making mods using the BepInEx framework.

To install, refer to [installation guide on R2Wiki](https://github.com/risk-of-thunder/R2Wiki/wiki/BepInEx).

### What each folder is for:
`BepInEx/plugins` - This is where normal mods/plugins are placed to be loaded.
For developers: There's no set format for what you need to name your plugins to load; if they're a valid plugin .dll file, they'll be loaded.
However please be considerate and isolate your files in their own folders, to prevent clutter, confusion, and in general, dependency hell. For example: `BepInEx/plugins/YourMod/Plugin.dll`.

`BepInEx/patchers` - These are more advanced types of plugins that need to access Mono.Cecil to edit .dll files during runtime. Only copy paste your plugins here if the author tells you to.
For developers: More info here: https://github.com/BepInEx/BepInEx/wiki/Writing-preloader-patchers

`BepInEx/monomod` - MonoMod patches get placed in here. Only copy paste your plugins here if the author tells you to.

`BepInEx/config` - If your plugin has support for configuration, you can find the config file here to edit it.

`BepInEx/core` - Core BepInEx .dll files, you'll usually never want to touch these files (unless you're updating)

### BepInEx 框架(作者: bbepis)

这是加载Mod插件所必须的框架。
安装非常简单，只需要把BepInEx文件夹、doorstop_config.ini、winhttp.dll放到游戏的根目录即可。

### 框架包含的内容:
`BepInEx/plugins` - 几乎所有的Mod dll都需要放在这个文件夹下面，除非Mod作者有特别说明。
例子: `BepInEx/plugins/YourMod/Plugin.dll`.

`BepInEx/patchers` - 个别Mod可能会使用Mono.Cecil等高级功能，这时需要将他们放在这个文件夹内，只有当Mod作者特别说明时你才会用到。
如果你是Mod作者，可以在这里查看更多信息: https://github.com/BepInEx/BepInEx/wiki/Writing-preloader-patchers

`BepInEx/config` - 如果Mod支持使用配置文件，那么默认情况下，配置文件会在这个文件夹生成。

`BepInEx/core` - BepInEx的核心dll文件夹，除非以后需要更新框架，不然你需要打开它。

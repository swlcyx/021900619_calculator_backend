<https://bbs.huaweicloud.com/blogs/115515>

1．缩进
每级缩进采用4个空格。
为了对付那些确实陈旧的代码，又不愿做出清理，那么可以继续沿用8个空格长度的制表符。

2．制表符还是空格
绝对禁止制表符和空格的混用。
最流行的Python缩进方式是只使用空格。第二流行的方式是只使用制表符。混合使用制表符和空格进行缩进的代码，应该转换为只使用空格的方式。如果调用Python命令行解释器时带上-t参数，它就会对非法混用制表符和空格的代码发出警告。如果用了-tt参数，这些警告就会上升为错误。强烈推荐使用这些参数！
对全新的项目而言，强烈建议只用空格缩进，换掉所有的制表符。大部分编辑器都具备将制表符替换为空格的便捷功能。

3．最大行长
所有行都应限制在79个字符以内。
将行长限制在80个字符的设备还有很多，而且将窗口限制为80个字符宽就可以并排放置多个窗口。这些设备上的默认换行会破坏代码的外观，增加理解的难度。因此，请将所有行都限制在79个字符以内。对于连续的大段文字（文档字符串或注释），建议将行长限制在72个字符以内。

4．空行
顶级函数和类定义之间，请用两个空行分隔。

类内部的各个方法定义之间，请用1个空行分隔。

为了让有关联的函数成组，可以在各函数组之间有节制地添加空行。相互关联的一组单行函数之间，可以省略空行，如一组函数的伪实现（dummy implementation）。

函数内部可以有节制地用空行来区分出各个逻辑部分。

Python可将Ctrl+L（^L）换页符接受为空白符。很多工具都将其视为分页符，所以可以利用其进行分页，使得文件中的关联部分单独成页。


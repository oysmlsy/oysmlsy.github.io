---
title: Jekyll Liquid 的用法
---

Liquid：

* 开源的模板语言
* 由 [Shopify](https://www.shopify.com) 创造
* 用 Ruby 语言编写

Liquid 有如下操作符（operator）：

* `==` 等于
* `!=` 不等于
* `>`  大于
* `<`  小于
* `>=` 大于等于
* `<=` 小于等于
* `or` 逻辑或
* `and` 逻辑与
* `contains` 包含

重点说下`contains`这个操作符。


* 用于检查在一个字符串中是否存在某个子字符串，见示例：

        {% raw %}
        {% if product.title contains 'Pack' %}
        This product's title contains the word Pack.
        {% endif %}
        {% endraw %}

* 用于检查在一个字符串数组中是否存在某个字符串，见示例：

        {% raw %}
        {% if product.tags contains 'Hello' %}
        This product has been tagged with 'Hello'.
        {% endif %}
        {% endraw %}

* 只能处理字符串。换言之，非字符串的数组不能使用`contains`；再换言之，`contains`的使用场景仅限于上述两种情况。

Liquid 中有两种标记 `{% raw %}{{ }}{% endraw %}` 和 `{% raw %}{% %}{% endraw %}`

Liquid 中有两种标记：Output 和 Tag。

* Output 标记被解析为文本，用`{% raw %}{{ }}{% endraw %}`包围：

        {% raw %}{{ matched pairs of curly brackets (ie, braces) }}{% endraw %}

* Tag 标记负责逻辑和流程控制，用`{% raw %}{% %}{% endraw %}`包围：

        {% raw %}{% matched pairs of curly brackets and percent signs %}{% endraw %}

## 输出标记（Output markup）

用 `{% raw %}{{ }}{% endraw %}`将表达式包围起来，构成 Output 语句

输出语句（Output statement）就是用双花括号包围一个表达式（Expression），模板被引擎处理渲染后，输出语句（Output statement）即被表达式（Expression）的值所取代。

输出标记（Output markup）的简单示例如下：

    {% raw %}
    Hello {{name}}
    Hello {{user.name}}
    Hello {{ 'tobi' }}
    {% endraw %}

### 表达式和变量（Expressions and Variables）

表达式（Expression）就是有值的语句（Statement）。Liquid 模板中，你可以在多个地方使用表达式（Expression），如在输出语句（Output statement）中使用表达式（Expression，这是表达式最常见的使用方式），或者将表达式（Expression）作为一部分标签（Tag）或过滤器（Filter）的参数（Argument）。

Liquid 输出标记（Output markup）中，如下几种类型的表达式（Expression）才是合法的：

* **变量（Variables）**。表达式（Expression）最基础的类型就是一个变量名。Liquid 变量（Variables）的命名规则与 Ruby 相同：变量名应由字母、数字和下划线构成，且必须以字母开头，不能以任何特殊字符开头（也就是说，变量名应该像`var_name`，而不能像`$var_name`）。

* **数组或哈希字典的访问（Array or hash access）**。如果一个表达式（Expression，通常为变量的形式）的值是数组（Array）或哈希字典（Hash），那么你必须按如下方式从这个集合中取出一个单一值：

    + `my_variable[<KEY EXPRESSION>]`—— 变量名的后面紧跟一对方括号，方括号内是键（Key）的表达式（key expression）。
        - 对于数组（Array）来说，键（Key）必须是一个整形数值字面量（literal integer），或者一个值为整数的表达式（Expression）。
        - 对于哈希字典（Hash）来说，键（Key）必须是一个被单引号或双引号括起来的字符串字面量（literal quoted string），或者一个值为字符串的表达式（Expression）。

    + `my_hash.key`—— 哈希字典（Hash）也可以使用一个更简洁的「点标记法」（dot notation），即变量名后面紧跟一个英文句号点，再接上键（Key）的名称。如果键（Key）名中有空格，或者键（Key）名存储在一个变量中，是不能使用「点标记法」的。

    + **注意：**如果按照上述方法从集合中取出的单一值仍是一个数组（Array）或哈希字典（Hash），那么你可以继续按照上述方法来访问集合中的单一值，并且上述两种方法可以穿插联合使用。（例如：`site.posts[34].title`）

* **数组的第一项和最后一项（Array first and last）**。如果表达式（Expression）的值是数组（Array），那么可以在其后接上`.first`或`.last`来取出数组（Array）的第一项或最后一项。

* **数组或哈希字典的大小（Array or hash size）**。如果表达式（Expression）的值是数组（Array）或哈希字典（Hash），那么可以在其后接上`.size`来计算出其所包含元素的数量，并以整数形式返回。

* **字符串（String）**。字符串字面量必须用双引号或单引号括起来（`"my string"`或`'my string'`），这两种形式没有区别，并且变量是没有办法穿插在字符串中的。

* **整数（Integer）**。整数不要用引号括起来，不然就成字符串了。

* **布尔值、空值（Boolean and nil）**

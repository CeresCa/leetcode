#  短网址生产算法

##  题目描述

> > Note: This is a companion problem to the [System Design](https://leetcode.com/discuss/interview-question/system-design/) problem: [Design TinyURL](https://leetcode.com/discuss/interview-question/124658/Design-a-URL-Shortener-(-TinyURL-)-System/).
>
> TinyURL is a URL shortening service where you enter a URL such as `https://leetcode.com/problems/design-tinyurl` and it returns a short URL such as `http://tinyurl.com/4e9iAk`.
>
> Design the `encode` and `decode` methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
>
> 


##  短网址设计原则

完整的短网址系统设计可以参考以下链接：

[短链接、短网址使用的是什么算法？](https://www.zhihu.com/question/20103344/answer/573638467)

[短 URL 系统是怎么设计的？](https://www.zhihu.com/question/29270034)

###  总结

单机的自增序列或者分布式的发号器



##  提交代码

```python
class Codec:
    def __init__(self):
        self.count = 0
        self.urls = dict()

    def encode(self, longUrl):
        self.count += 1
        self.urls[self.count] = longUrl
        return "http://tinyurl.com/" + str(self.count)

    def decode(self, shortUrl):
        return self.urls[int(shortUrl.split("/")[-1])]
```



###  说明

最简单的方式，使用 count 变量存编号，dict 存 count, longurl 的映射关系



###  缺陷

1. 未解决长url重复问题
2. 可以被统计出生产了多少短网址
3. 可以被遍历和恶意提交
4. 仅使用数字，相同位数，可提供的短url数量，相比数字字母混合要少




# Blackjack 踩坑笔记

> 只记「浪费过时间」的问题。

## 索引

- [Dealer方法编程错误](#2026-7-24--dealer方法编程错误)
- [Dealer.hole_revealed属性设置理解错误](#2026-7-24--dealerhole_revealed属性设置理解错误)
- [Enum 用属性访问当比较](#2026-7-26--enum-用属性访问当比较)
- [`_check_natural` 无 BJ 却判负](#2026-7-26--_check_natural-无-bj-却判负)

---

## 2026-7-24 · Dealer方法编程错误

- **场景**：`Dealer.should_hit()`
- **现象**：不理解should_hit在Dealer中的作用，将整个功能写成判断软17并且拿牌。
- **原因**：should_hit(self, card) 不该收 card,同时将同一张card反复while循环。
- **解决**：明确Dealer中只需要判断是否出现软17，不需要实现拿牌循环逻辑。
- **规则**：在写方法的时候明确各类的职责。

## 2026-7-24 · Dealer.hole_revealed属性设置理解错误

- **场景**：`Dealer.hole_revealed`
- **现象**：只有设成 False，没有翻开成 True 的入口，每次 receive_card 都改成 False。
- **原因**：hole_revealed 表示「是否已翻开」,第三张及以后是明牌要牌，不应把已翻开状态打回去。
- **解决**：添加reveal()方法（设置翻开的动作），删去receive_card()中的状态设置。
- **规则**：在写方法的时候明确各类的职责、属性，搞清出整个类的实现逻辑以及与其他功能的关系。

## 2026-7-26 · Enum 用属性访问当比较

- **场景**：`BlackJackGame._settle(self, outcome)`
- **现象**：写成 `if outcome.WIN` / `elif outcome.PUSH` 这类判断时，分支几乎总是进得去，结算结果和真实 `outcome` 对不上。
- **原因**：`outcome.WIN` 不是在比较，而是取出 `Outcome.WIN`；枚举成员为真，所以 `if` 恒成立
- **解决**：改成身份`if outcome is Outcome.WIN`。
- **规则**：对枚举做分支时，比较「变量」和「枚举成员」；不要写成 `变量.成员名` 当作条件。

## 2026-7-26 · `_check_natural` 无 BJ 却判负

- **场景**：`BlackJackGame._check_natural`
- **现象**：一运行就打印 `结果：LOSE … 剩余筹码：900`，不进 hit/stand。
- **原因**：双方都不是自然 BJ 时落入 `else`，被当成庄家赢结算；「仅庄家 BJ」与「无 BJ 继续」的条件也写反了。
- **解决**：修改为`not p and not d`。
- **规则**：在写条件判断时，不能简写`not and`表示两者都不是！！！ 。
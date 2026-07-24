# Blackjack 踩坑笔记

> 只记「浪费过时间」的问题。

## 索引

- [Dealer方法编程错误](#2026-7-24--dealer方法编程错误)
- [Dealer.hole_revealed属性设置理解错误](#2026-7-24--dealerhole_revealed属性设置理解错误)

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

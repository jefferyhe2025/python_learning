# Blackjack（21 点）

基于面向对象编程练习的命令行 21 点小游戏。概念对齐课文「扑克游戏」例一（牌 / 牌堆 / 玩家），按 Blackjack 规则**重写**实现；支持下注、自然 Blackjack、庄家固定规则，以及多局对战（破产或主动退出结束）。

> 当前仓库阶段：**可玩的 CLI 实现已落地**（领域 / 对局 / UI 分层）

## Features

- 标准 52 张牌（无大小王）
- 1 名闲家 + 1 名庄家
- 下注筹码；自然 Blackjack（默认赔率 3:2）
- 闲家：要牌（Hit）/ 停牌（Stand）
- 庄家：点数 &lt; 17 必须要牌（软 17 停牌）
- 多局循环：筹码归零结束，或主动退出

**刻意不包含**：分牌、保险、加倍、多副牌、多闲家。

## Requirements

- Python 3.8+
- 仅使用标准库（不引入第三方依赖）

## Project Layout

```
blackjack/
├── README.md                 # 本文件：项目说明
├── docs/
│   ├── DESIGN.md             # 开发者设计思路（架构 / 类 / 流程 / 边界）
│   └── PITFALLS.md           # 踩坑笔记
├── main.py                   # 入口组装
├── models/                   # 领域对象
│   ├── suite.py
│   ├── card.py
│   ├── deck.py
│   ├── hand.py
│   └── player.py
├── game/                     # 对局编排
│   └── blackjack.py
└── ui/                       # 命令行交互
    └── console.py
```

分层约定见 [docs/DESIGN.md](docs/DESIGN.md)。

## Rules (Summary)

| 项目 | 约定 |
|------|------|
| A | 在不超过 21 的前提下尽量计为 11 |
| 庄家 | 点数 &lt; 17 要牌；≥ 17 停（含软 17） |
| 自然 Blackjack | 开局两张恰 21；闲家独有时赔 3:2 |
| 普通获胜 | 1:1 |
| 平局（Push） | 退还本局赌注 |
| 闲家爆牌 | 立即判负，庄家不必再要牌 |
| 初始筹码 | 建议默认 `1000`（实现时用常量，可改） |

完整流程与边界以设计文档为准。

## Usage

在仓库根目录运行（因导入路径为 `project.blackjack...`）：

```bash
cd /path/to/python_learning
python -m project.blackjack.main
```

或在已配置好 `PYTHONPATH` 指向仓库根的前提下，进入 `project/blackjack` 后执行 `python main.py`。

预期交互（示意）：

```text
筹码: 1000
请输入下注额: 100
你的手牌: ♠A ♥K  (21)
庄家明牌: ♦10
Blackjack! 你赢得 150
是否继续? (y/n):
```

## Status

- [x] 需求与方案确认（教学增强版 / CLI 模块拆分 / 多局 + 破产结束）
- [x] 设计文档
- [x] 领域模型与对局逻辑实现（`models/` + `game/`）
- [x] 命令行 UI（`ui/console.py`：询问 / 桌面 / 结算 / 会话结束）
- [x] 分层检查与展示收拢（非法输入重试在 UI；筹码不变式在 `Player.place_bet`；赔付在 Game；展示走 `show_*`）
- [x] 基础测试与手工验收（建议对照 `docs/DESIGN.md` §7：非法输入、多局筹码、破产/退出、自然 BJ / 爆牌）

## License

Learning / personal project. No license file attached yet.

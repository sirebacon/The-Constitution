# 如何编写模拟测试

本指南解释如何向宪法流程模拟器中添加新的模拟测试，以便其他贡献者能够一致地创建新情景。

该模拟器不是一个模糊的人工智能推理系统，而是一个确定性的情景运行器。

每项测试通常包含四个部分：

1. 一个情景 JSON 文件
2. 一个或多个事件处理器
3. 生成的报告输出
4. 后续文档更新

---

## 1. 从真实的宪法压力路径开始

不要从凭空发明一个随机事件类型开始。

应从一个具体问题开始，例如：

- 如果总统以法令继续执行已经到期的紧急关税，会发生什么？
- 如果某州拒绝承认同性家庭的父母身份，会发生什么？
- 如果某个宪法机构错过启动期限，会发生什么？
- 如果一个占支配地位的平台在选举期间切断一个合法政治参与者的接入，会发生什么？

然后定义：

- 正在测试的宪法条款
- 预期应当行动的机构
- 预期的宪法后果
- 是否应当仍然存在某种瓶颈

最好的情景测试的是已知的失效模式，而不是抽象意义上的坏结果。

---

## 2. 判断这是一个新情景，还是一个新情景家族

如果该情景适合现有领域，就扩展现有的处理器模块。

常见的处理器领域包括：

- [executive.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/executive.py)
- [legislative.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/legislative.py)
- [judiciary.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/judiciary.py)
- [rights.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/rights.py)
- [federalism.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/federalism.py)
- [integrity.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/integrity.py)
- [transition.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/transition.py)
- [social_rights.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/social_rights.py)
- [fiscal.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/fiscal.py)

如果该情景引入了一个真正新的领域，就新增一个处理器模块，并在 [dispatcher.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/dispatcher.py) 中注册它。

---

## 3. 创建情景 JSON

情景文件位于 [simulation/scenarios](/Users/chris/Documents/GitHub/The-Constitution/simulation/scenarios)。

请以现有文件为模板。

好的参考示例包括：

- [emergency-revenue-measure-unilateral-extension.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/scenarios/emergency-revenue-measure-unilateral-extension.json)
- [family-status-discrimination-parental-recognition.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/scenarios/family-status-discrimination-parental-recognition.json)
- [constitutional-organ-bridge-startup.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/scenarios/constitutional-organ-bridge-startup.json)

一个情景文件应当包括：

- `id`
- `title`
- `description`
- `articles_tested`
- `provisions_tested`
- `events`

典型结构：

```json
{
  "id": "example-scenario",
  "title": "Short Human Title",
  "description": "One paragraph explaining the stress path and what the scenario is testing.",
  "articles_tested": ["Article V"],
  "provisions_tested": ["Article V Section 2.1", "Article V Section 2.6"],
  "events": [
    {
      "day": 0,
      "type": "some_event_type",
      "actor": "President",
      "details": {
        "key": "value"
      }
    },
    {
      "day": 3,
      "type": "some_followup_event",
      "actor": "Federal courts"
    }
  ]
}
```

指南：

- 保持事件按时间顺序排列
- 标题保持简短且可读
- 描述中明确写出正在测试的宪法问题
- 列出真正应当控制该情景的条款

---

## 4. 选择好的事件类型

事件类型应描述有意义的宪法行动或失灵，而不是含糊的状态。

好的：

- `president_orders_emergency_revenue_measure_continued`
- `court_voids_unilateral_emergency_revenue_extension`
- `state_denies_parental_recognition`

不好的：

- `government_does_bad_thing`
- `court_acts`
- `problem_happens`

如果一个新事件类型过于宽泛，未来的情景就会变得难以推理，处理器逻辑也会变得混乱。

---

## 5. 实现或扩展处理器逻辑

模拟器通过处理器注册表处理事件。

调度注册表位于 [dispatcher.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/dispatcher.py)。

每个处理器模块都会导出一个以事件类型为键的 `HANDLERS` 映射。

典型模式：

```python
HANDLERS = {
    "some_event_type": handle_some_event,
}
```

在处理器内部，代码通常会做以下几类事情中的某些组合：

- 添加时间线条目
- 触发一项宪法条款
- 创建一个带有期限的义务
- 解决或违反某项义务
- 记录一个瓶颈
- 记录一个违规类别或风险模式

添加处理器逻辑时：

- 保持其确定性
- 明确写出被触发的条款
- 让结果始终锚定在真实的宪法设计上
- 不要悄悄引入未在草案中立足的政策假设

如果需要新模块：

1. 在 [simulation/handlers](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers) 下添加该文件
2. 导出一个 `HANDLERS` 映射
3. 在 [dispatcher.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/dispatcher.py) 中注册该映射

---

## 6. 运行该情景

列出情景：

```bash
python3 simulation/run.py --list
```

运行单个情景：

```bash
python3 simulation/run.py --summary simulation/scenarios/example-scenario.json
```

运行全部情景并保存输出：

```bash
python3 simulation/run.py --all --out-dir simulation/reports --save-full --save-json --save-aggregate
```

有用的输出包括：

- `.full.md` 供人工审阅
- `.summary.json` 供结构化结果使用
- `aggregate.json` 作为全套测试的基线

运行器位于 [run.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/run.py)。

---

## 7. 正确理解结果

一个情景应当告诉你：

- 哪些条款被触发
- 创建了哪些义务
- 哪些义务得到了满足
- 是否发生了违规
- 是否仍然存在瓶颈
- 是否有义务未被解决

重要区分：

- `violation` 往往意味着该情景成功建模了不当行为
- `unresolved_obligation` 则是更严重的设计问题，因为宪法未能完成一条本应完成的后果链

设计目标并不是让所有情景中的违规数量都为零。许多情景本来就是从违法行为开始的。

真正的目标是：

- 清晰的宪法路由
- 可执行的义务
- 后果链的干净闭合
- `0` 未解决义务

---

## 8. 更新情景目录

添加测试后，请更新 [test-scenarios.md](/Users/chris/Documents/GitHub/The-Constitution/design-notes/test-scenarios.md)。

加入以下内容：

- 类别
- 情景名称
- 文件名
- 条款
- 压力路径
- 预期结果

这个目录是公开的测试清单，用来说明哪些内容已经测试，哪些尚未测试。

---

## 9. 如果情景带来了新认识，就更新发现文档

如果新情景：

- 验证了一项此前不确定的条款
- 暴露了真实缺口
- 改变了某篇文章应如何评分
- 澄清某个瓶颈是可接受还是不可接受

那么请更新：

- [simulation-findings.md](/Users/chris/Documents/GitHub/The-Constitution/design-notes/simulation-findings.md)
- 有时还包括 [scorecard.md](/Users/chris/Documents/GitHub/The-Constitution/design-notes/scorecard.md)

不要仅仅因为新增了一个测试，就机械地更新评分卡。
只有在该测试实质性改变了对某篇文章的信心时，才更新它。

---

## 10. 什么样的情景才算好

一个强的情景：

- 清楚地测试一个宪法系统
- 使用现实的压力路径
- 点明真正控制该情景的条款
- 产生可读的预期结果
- 能够隔离问题究竟是：
  - 违规
  - 瓶颈
  - 结构性缺口
  - 可接受的政治风险残留

一个弱的情景：

- 试图一次测试过多系统
- 使用含糊的事件名称
- 在没有处理器支持的情况下预设结果
- 把所有负面事实都当成宪法失败

---

## 11. 推荐工作流程

最安全的工作流程是：

1. 选定一个真实的宪法问题
2. 找到最接近的现有情景
3. 创建新的情景 JSON
4. 扩展或新增处理器逻辑
5. 先运行单个情景
6. 检查摘要和完整报告
7. 运行完整测试集
8. 更新目录和发现文档

这样可以让情景保持可理解，也能减少加入“看起来不错但实际上并未真正接入系统”的测试的风险。

---

## 12. 贡献者快速检查清单

- 我是否定义了一个真实的宪法压力路径？
- 我是否写明了正在测试的真实条款？
- 我是否使用了清晰的事件类型？
- 我是否添加或更新了处理器逻辑？
- 除非该情景有意暴露缺口，否则它是否在没有未解决义务的情况下运行？
- 我是否更新了 `test-scenarios.md`？
- 如果结果改变了项目的信心，我是否更新了发现文档或评分卡？

如果以上问题的答案都是“是”，那么这个情景大概率已经可以提交。

# TW3 提交和使用说明

当前技术版本为 1.0。四位候选已全部比较，按 Yufei 的明确委托，由助手确定整合方案：Yufei 的工具调用与图表场景、Jianbo 的机制和证据纪律、Chutong 的五类促进条件、Minghan 的缺失信息测试。原材料没有修改，本文件夹在上一版基础上更新。

## 提交材料

- `Special_Dark_TW3_Team_Agent_Record.docx`：唯一英文主体报告，包含四人比较、选择理由、测试和交接。
- `Special_Dark_TW3_Creation_Agent.zip`：本文件夹外的同级压缩包，包含可运行内容与证据。若 Brightspace 允许，可随 Word 提交；否则附团队仓库版本链接，按实际提交栏要求操作。
- 团队仓库：https://github.com/Sun417-jianbo/special-dark 。独立分支 `codex/tw3-creation-agent-20261006`；路径 `team_integration_workspace/review/creation_agent_v1_0/`。实际远程信息见 `verification/repository_handoff.json`。

## 已完成的技术内容

四份候选快照、四份共同案例设计比较示例、四份整合 Agent 案例与输出、来源登记、弱输出及修订、冻结文件检查、JSON 验证、贡献与七专家交接均已保存。`evidence/` 中的旧输出是教授要求的失败/修订证据，不是多余初稿。其他 scaffold 模板和示例来自教授的原始基线，不代表另建了其他专家。

共同案例固定技术、应用和期限，改变组织条件。输出由同一助手在当前对话生成和检查，部分公共字段复用，不是独立模型试验或真实企业试点。

## 仍需如实面对的课程要求

你已说明没有课堂讨论结果，因此不能声称完成了全组课堂讨论、全员表决或约 90% 的课内工作。文件披露委托决策及 AI 使用，未虚构组员核验。教授要求的团队专业判断仍需你们本人阅读、理解并确认；不能保证当前过程满足该评分项。

GitHub 分支和合并请求用于共享与审阅，不等于全员批准或自动合并。未替你提交 Brightspace，也未改动主分支。让组员核验后，再决定合并和提交。

通用说明写一天内，此次 rubric 写 36 小时；以 Brightspace 实际截止时间或教授确认为准。

## 本地重跑

只需 Python 3，不需要 API key 或额外库。在本文件夹运行：

```bash
python3 tools/build_prompt.py --agent agents/creation_agent --case agents/creation_agent/cases/primary.json --out agents/creation_agent/prompts/primary.txt
python3 tools/validate_response.py agents/creation_agent/responses/primary_response.json
python3 tools/check_frozen_core.py
python3 verification/verify_package.py
```

第一条只生成 prompt，不调用模型。真正重跑时，把 prompt 放入课堂规定的 ChatGPT 交互环境，保存实际返回的 JSON，再验证。重新运行不保证相同答案。

后续继续修改同一份 Word 和本文件夹，更新版本与哈希，不另建多余报告初稿。

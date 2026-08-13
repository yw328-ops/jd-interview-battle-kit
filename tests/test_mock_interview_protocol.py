from pathlib import Path


skill = (Path(__file__).parent.parent / "SKILL.md").read_text(encoding="utf-8")

required = (
    "一轮4个问题",
    "开场题",
    "业务题",
    "压力题",
    "收尾题",
    "追问最多两层",
    "不透露评价或答题线索",
    "四题全部完成前不得进行实质点评",
    "全部结束后逐题详细点评",
    "哪里好",
    "哪里可以更好",
    "真实面试官可能的反应",
    "整体表现总结",
    "最突出的 1-2 个优势",
    "暴露清单",
    "下一轮最优先训练内容",
)

for phrase in required:
    assert phrase in skill, f"SKILL.md 缺少协议短语：{phrase}"

assert "等用户答完追问才进入点评" not in skill, (
    "SKILL.md 仍要求每题追问后立即点评"
)

print("PASS: 模拟面试协议要求四题结束后再统一复盘")

from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).parent.parent
PACKAGE = ROOT / "dist" / "jd-interview-battle-kit.zip"
PREFIX = "jd-interview-battle-kit/"
VERSION = "1.3.3"

INCLUDED = (
    "COMPATIBILITY.md",
    "INSTALL.md",
    "LICENSE",
    "README.md",
    "SKILL.md",
    "templates/stage1_one_page_brief.md",
    "templates/stage2_battle_map.md",
    "templates/stage3_interview_materials.md",
    "templates/stage4_final_summary.md",
    "tests/mock_interview_protocol_smoke_2026-08-13.md",
    "tests/test_cases.md",
    "tests/test_mock_interview_protocol.py",
    "tests/test_package_sync.py",
)

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
assert f"version: {VERSION}" in skill, f"SKILL.md 版本不是 {VERSION}"

with ZipFile(PACKAGE) as archive:
    packaged_files = {
        name.removeprefix(PREFIX)
        for name in archive.namelist()
        if name.startswith(PREFIX) and not name.endswith("/")
    }
    assert packaged_files == set(INCLUDED), "dist 安装包的文件清单与仓库发布清单不一致"

    for relative_path in INCLUDED:
        packaged = archive.read(PREFIX + relative_path)
        current = (ROOT / relative_path).read_bytes()
        assert packaged == current, f"dist 安装包中的 {relative_path} 不是最新版"

print(f"PASS: 所有下载入口的发布内容已同步到 {VERSION}")

import ast, os, subprocess
from pathlib import Path
source=Path('ui/phase15_raid_plan_workspace.py')
test=Path('ui/tests/test_raid_plan_sidebar_map_geometry.py')
backup={p:p.read_bytes() for p in (source,test)}
for p,data in backup.items():
    (Path('validation_reports')/(p.name+'.repair-backup')).write_bytes(data)
class CaptureOnly(ast.NodeTransformer):
    def visit_Assert(self,node):
        return ast.copy_location(ast.Expr(value=node.test),node)
try:
    source.write_bytes(subprocess.check_output(['git','show','HEAD:ui/phase15_raid_plan_workspace.py']))
    test.write_text(ast.unparse(CaptureOnly().visit(ast.parse(backup[test].decode('utf-8')))),encoding='utf-8')
    os.environ['QT_SCALE_FACTOR']='1'
    os.environ['WYRD_MAP_CAPTURE']='C:/Users/nourg/Documents/Codex/2026-10-28/referenced-chatgpt-conversation-this-is-an-4/outputs/before-100'
    result=subprocess.run(['python','-m','pytest',str(test),'-q','--basetemp=validation_reports/baseline-capture'])
finally:
    for p,data in backup.items():p.write_bytes(data)
print('Baseline capture only; assertions intentionally evaluated without enforcement. Repair sources restored.')

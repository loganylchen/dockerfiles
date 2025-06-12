import os
import re
import yaml
import glob

# 文件路径
workflows_files = glob.glob('./.github/workflows/tools_*_build.yaml')
readme_path = './README.md'

# 提取工具信息
def extract_tools_info(workflows_dir):
    tools_info = []
    for wf in workflows_files:
        print(wf)
        with open(wf, 'r') as f:
            try:
                workflow = yaml.safe_load(f)
                # 提取工具名称和版本信息
                job = workflow.get('jobs', {}).get('docker', {})
                matrix = job.get('strategy', {}).get('matrix', {})
                versions = matrix.get('version', [])
                name_and_ref = workflow.get('name', ('Unknown Workflow|unknown')),
                print(name_and_ref[0])
                print(name_and_ref[0].split(r'|'))
                name,*ref = name_and_ref[0].split(r'|')
                tools_info.append({
                    'name': name,
                    'ref':ref,
                    'versions': versions  })
            except yaml.YAMLError:
                print(f"无法解析文件: {filepath}")
    return tools_info

# 更新 README.md
def update_readme(readme_path, tools_info):
    with open(readme_path, 'r') as f:
        lines = f.readlines()

    # 找到表格插入点
    table_start = next((i for i, line in enumerate(lines) if line.startswith('| Tool Name')), None)
    table_end = next((i for i, line in enumerate(lines[table_start + 1:], start=table_start + 1) if not line.strip() or not line.startswith('|')), None)

    # 构建新表格内容
    new_table = [
        "| Tool Name   | Reference                                                                                     | Version List       | \n",
        "|-------------|-----------------------------------------------------------------------------------------------|--------------------|\n"
    ]
    for tool in tools_info:
        name = tool['name']
        versions = ' '.join([f"![{name} Version](https://img.shields.io/badge/{name}-{version}-blue)" for version in tool['versions']])
        reference = tool['ref'] if len(tool['ref'] )==0 else tool['ref'][0] # 可以替换为实际的参考链接
     
        new_table.append(f"| {name}        | {reference} | {versions} |\n")

    # 替换表格内容
    if table_start is not None and table_end is not None:
        lines = lines[:table_start] + new_table + lines[table_end:]
    else:
        lines.extend(new_table)

    # 写回 README.md
    with open(readme_path, 'w') as f:
        f.writelines(lines)

# 主函数
def main():
    tools_info = extract_tools_info(workflows_files)
    if tools_info:
        update_readme(readme_path, tools_info)
        print("README.md 已更新！")
    else:
        print("未找到任何工具信息，请检查 .github/workflows/ 目录。")

if __name__ == "__main__":
    main()
    


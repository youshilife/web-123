# =============================================================================
# 构建页面
# =============================================================================
#
# 需要的环境：
# - Python
# - Markdown库
#


import json
import markdown


def get_search_html():
    """获取搜索引擎部分的HTML代码"""

    with open("data/搜索引擎.json", "r", encoding="UTF-8") as file:
        data = json.load(file)
    html = ""
    for search in data:
        # 生成隐藏表单项的HTML
        hidden_html = ""
        for key, value in search["hidden"].items():
            hidden_html += """
<input type="hidden" name="{key}"  value="{value}">
""" \
                .format(key=key, value=value)
        # 生成整个表单的HTML
        form_html = """
<form action="{url}" method="GET">
{hidden_html}
<input type="search" name="{key}" placeholder="{name}">
<input type="submit" value="{name}">
</form>
""" \
            .format(
                url=search["url"],
                hidden_html=hidden_html,
                key=search["key"],
                name=search["name"]
            )
        html += form_html
    return html


def get_nav_html():
    """获取导航链接部分的HTML代码"""

    # 从Markdown生成HTML
    with open("data/导航链接.md", "r", encoding="UTF-8") as file:
        return markdown.markdown(file.read())


def build_page(parts):
    """构建页面"""

    # 将各部分的HTML替换到模板中
    with open("html/模板.html", "r", encoding="UTF-8") as file:
        html = file.read()
    for key, part_html in parts.items():
        html = html.replace("<!--[[{}]]-->".format(key), part_html)
    # 生成最终页面
    with open("index.html", "w", encoding="UTF-8") as file:
        file.write(html)


if __name__ == "__main__":
    build_page({
        "search": get_search_html(),
        "nav": get_nav_html(),
    })

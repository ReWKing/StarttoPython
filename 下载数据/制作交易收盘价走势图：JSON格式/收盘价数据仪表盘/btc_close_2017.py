# author：K
with open('比特币收盘价Dashboard.html', 'w', encoding='utf8') as html_file:
    html_file.write(
        '<html><head><title>比特币收盘价Dashboard</title><meta charset="utf-8"></head><body>\n')
    for svg in [
            '比特币收盘价折线图（¥）.svg', '比特币收盘价对数变换折线图（¥）.svg', '比特币收盘价月日均值（¥）.svg',
            '比特币收盘价周日均值（¥）.svg', '比特币收盘价星期均值（¥）.svg'
    ]:
        html_file.write(
            '    <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))  # 1
    html_file.write('</body></html>')


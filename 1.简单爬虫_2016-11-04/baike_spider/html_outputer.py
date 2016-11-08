#coding=utf-8
class HtmlOutputer(object):
    #需要一个列表维护收集的数据
    def __init__(self):
        self.datas = []




    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def out_html(self):
        fout = open('output.html','w')
        fout.write("<html>")
        fout.write("<meta charset='utf-8'>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            #每一行
            fout.write("<tr>")
             #每个单元格
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))

            fout.write("</tr>")


        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")


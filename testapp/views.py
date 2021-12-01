from django.http import HttpResponse

# Create your views here.


def index(request):
    data = [[1], [1,1]]
    for i in range(3, 10):
        l = [1]
        lastline = data[-1]
        for j in range(0, len(lastline)-1):
            l.append(lastline[j] + lastline[j+1])
        l.append(1)
        data.append(l)
    # 生成字符串
    sep = '&nbsp;&nbsp;&nbsp;&nbsp;'
    width = len(sep.join(map(str, data[-1])))
    res_str = '<br/><br/>'
    for i in data:
        res_str += '<p style="text-align:center">' + sep.join(map(str, i)) + '</p>'
    return HttpResponse(res_str + '<br/><h5 style="text-align:center">9层的杨辉三角</h5>')
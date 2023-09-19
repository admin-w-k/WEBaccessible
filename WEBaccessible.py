import warnings
import requests

for line in open("url.txt"):            #读取文件内容
        try:                            #抓取异常内容
                warnings.filterwarnings("ignore") #用于屏蔽未来警告信息（忽略匹配的警告）
                url = line.strip()#strip用于清除头尾的特殊字符（如空格\n等）
                print(url)
                response = requests.get(url,verify=False,timeout=3) #设置超时时间为3s，非强制使用https
                #print(response.status_code)
                state = [200,503,304]        #匹配响应状态码
                content1 = ('nginx')          #匹配字段中是否含有敏感信息
                content2 = ('apache')
                content3 = ('openresty')
                #print (response.text)
                if response.status_code in state:
                        print('is accessible\n')
                elif content1 in response.text:
                        print('含有nginx字段！\n')
                elif content2 in response.text:
                        print('含有apache字段！\n')
                elif content3 in response.text:
                        print('含有openresty字段！\n')
                else:
                        print('已关闭\n')
        except:                         #返回异常信息统一处理
                print ('超时或未找到服务器\n')


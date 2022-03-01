class File:
    def write(name, content):

        with open(name,'w',encoding='utf-8') as fp:
            fp.write(content)

    def read(name):
        content=""
        with open(name,'r') as fp:
            content = fp.read()
        return content
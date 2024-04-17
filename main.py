import py7zr
import hashlib
import os


def getMD5(file_path):
    res = ''
    with open(file_path, 'rb') as f:
        temp = hashlib.md5()
        for chunk in iter(lambda: f.read(4096), b''):
            temp.update(chunk)
        res = temp.hexdigest()
    return res


def unzip(zip, to):
    with py7zr.SevenZipFile(zip, mode='r') as z:
        z.extractall(path=to)


full_resource = ['mingw64.7z', 'LLVM.7z', 'VSCode.7z', 'JetBrainsMono.7z']

tool_resource = ['mingw64.7z', 'LLVM.7z']


def checkResource(resource):
    md5 = []
    with open('./md5.txt', 'r') as f:
        md5 = f.readlines()
    i = 0
    for x in resource:
        print(f'检查 ./resource/{x}...')
        try:
            if getMD5(f'./resource/{x}') != md5[i].replace('\n', ''):
                print(f'./resource/{x} 文件损坏')
                return False
        except:
            print(f'./resource/{x} 文件损坏')
            return False
        i += 1
    print('检查完成')
    return True


def addPath(path):
    now = os.getenv('Path')

    now = f'{now}{path};'

    os.system(f'setx Path \"{now}\" -m')


def installTools():
    unzip('./resource/mingw64.7z', 'C:/')
    unzip('./resource/LLVM.7z', 'C:/')


if __name__ == '__main__':
    print('----------------- 欢迎来到 VSCode Helper -----------------')

    choose = input('请输入安装选项 (full: 安装所有; tool: 仅安装编译工具) >>> ')

    if choose == 'full':
        if checkResource(full_resource):
            pass
        else:
            print('资源包校验失败，请手动补齐')
    elif choose == 'tool':
        if checkResource(tool_resource):
            pass
        else:
            print('资源包校验失败，请手动补齐')
    else:
        print('非法输入')

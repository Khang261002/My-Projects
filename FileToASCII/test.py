import filetype

def check():
    kind = filetype.guess('Random.png')
    if kind is None:
        print('Cannot guess file type!')
        return

    print(kind.mime.split('/')[0])
    return kind.mime.split('/')[0]

if __name__ == '__main__':
    if check() == "image":
        print('Image')

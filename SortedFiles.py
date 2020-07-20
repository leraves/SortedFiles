import os
import glob
import cv2

class moveFiles:

    def sort_downloads(dirrectoriya, path):
        pic = path + '/pic'
        arhiv = path + '/arhiv'
        doc = path +'/doc'
        exe = path + '/exe'
        py = path + '/py'
        torrent = path + '/torrent'

        os.chdir(dirrectoriya)  # указываем дирректорию
        format_pic = ['.png', '.jpg', '.jpeg', '.bmp']#форматы картинок
        format_torrent = ['.torrent']
        format_exe = ['.exe']
        format_doc = ['.pdf', '.doc', '.docx', '.djvu', '.txt', '.xml', '.json', '.xlsx', '.pptx']
        format_arhiv = ['.rar', '.zip']
        format_py = ['.py']

        all_format = []
        all_format.append(format_pic)
        all_format.append(format_torrent)
        all_format.append(format_arhiv)
        all_format.append(format_py)
        all_format.append(format_exe)
        all_format.append(format_doc)

        for file in glob.glob('*'):
            formats_files = os.path.splitext(file)

            for i in range(len(all_format)):
                for j in all_format[i]:
                    if formats_files[1] == j:
                        if i == 0:
                            os.replace(file, pic + '/' + file)
                        if i == 1:
                            os.replace(file, torrent + '/' + file)
                        if i == 2:
                            os.replace(file, arhiv + '/' + file)
                        if i == 3:
                            os.replace(file, py + '/' + file)
                        if i == 4:
                            os.replace(file, exe + '/' + file)
                        if i == 5:
                            os.replace(file, doc + '/' + file)
class copyFiles(moveFiles):
    def sort_downloads(dirrectoriya, path):
        print(3)
    def copyFile():
        print(1)
if __name__ == '__main__':

    path = "C:/Users/Lera/Desktop"
    dirrectoriya = "C:/Users/Lera/Downloads/"
    #moveFiles.sort_downloads(dirrectoriya, path)
    copyFiles.copyFile()
    copyFiles.sort_downloads(dirrectoriya, path)
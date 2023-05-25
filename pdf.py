
import PyPDF2 as pdf2
import glob
print("結合したいPDFが入ったフォルダを選択")
dir=input()
fol=glob.glob(str(dir)+"/*")
fol.sort()
print(fol)
print(dir)
merger=pdf2.PdfMerger()
for file in fol:
    merger.append(file)
print("結合したPDFファイルを配置するフォルダを選択")
place=input()
merger.write(str(place)+"/new.pdf")
merger.close()
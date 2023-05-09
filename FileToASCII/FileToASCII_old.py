from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os
import cv2
import filetype
import subprocess

def check_type(file):
    kind = filetype.guess(file)
    if kind is None:
        print('Cannot guess file type!')
        return "Cannot guess file type!"

    print('Type of file: %s' % kind.mime.split('/')[0])
    return kind.mime.split('/')[0]

def videoToFrames(vidFile):
    fileList = []
    maxWidth = 160
    global sourceFPS
    vidcap = cv2.VideoCapture(vidFile)
    sourceFPS = vidcap.get(cv2.CAP_PROP_FPS)
    success, image = vidcap.read()
    count = 0
    while success:
        width, height, _ = image.shape
        shrinkRatio = width/maxWidth
        image = cv2.resize(image, (int(height/shrinkRatio), int(width/shrinkRatio)))
        cv2.imwrite("frame%d.jpg" % count, image)
        fileList.append("frame%d.jpg" % count)
        success, image = vidcap.read()
        print("Frame " + str(count) + " successfully read")
        count += 1
    return (fileList)

def generateFrameConversionData(imgPath):
    divisor = 3.642857142857143
    maxWidth = 160
    imgData = []   
    greyscaleChars = {
		"70" : "$","69" : "@","68" : "B","67" : "%","66" : "8","65" : "&","64" : "W","63" : "M","62" : "#","61" : "*","60" : "o","59" : "a","58" : "h","57" : "k","56" : "b","55" : "d","54" : "p","53" : "q","52" : "w",
		"51" : "m","50" : "Z","49" : "O","48" : "0","47" : "Q","46" : "L","45" : "C","44" : "J","43" : "U","42" : "Y","41" : "X","40" : "z","39" : "c","38" : "v","37" : "u","36" : "n","35" : "x","34" : "r","33" : "j",
		"32" : "f","31" : "t","30" : "/","29" : "\\","28" : "|","27" : "(","26" : ")","25" : "1","24" : "{","23" : "}","22" : "[","21" : "]","20" : "?","19" : "-","18" : "_","17" : "+","16" : "~","15" : "<","14" : ">",
		"13" : "i","12" : "!","11" : "l","10" : "I","9" : ";","8" : ":","7" : ",","6" : "\"","5" : "^","4" : "`","3" : "'","2" : ".","1" :  " "	,"0" :  " "
        }
    greyscaleCharsRev = {
        "0" : "$","1" : "@","2" : "B","3" : "%","4" : "8","5" : "&","6" : "W","7" : "M","8" : "#","9" : "*","10" : "o","11" : "a","12" : "h","13" : "k","14" : "b","15" : "d","16" : "p","17" : "q","18" : "w",
        "19" : "m","20" : "Z","21" : "O","22" : "0","23" : "Q","24" : "L","25" : "C","26" : "J","27" : "U","28" : "Y","29" : "X","30" : "z","31" : "c","32" : "v","33" : "u","34" : "n","35" : "x","36" : "r","37" : "j",
        "38" : "f","39" : "t","40" : "/","41" : "\\","42" : "|","43" : "(","44" : ")","45" : "1","46" : "{","47" : "}","48" : "[","49" : "]","50" : "?","51" : "-","52" : "_","53" : "+","54" : "~","55" : "<","56" : ">",
        "57" : "i","58" : "!","59" : "l","60" : "I","61" : ";","62" : ":","63" : ",","64" : "\"","65" : "^","66" : "`","67" : "'","68" : ".","69" :  " "	,"70" :  " "
        }
    
    img = Image.open(imgPath)
    img = img.convert("RGB")
    gImg = img.convert("L")
    size = gImg.size
    shrinkRatio = size[0]/maxWidth
    gImg = gImg.resize((int(size[0]/shrinkRatio), int(size[1]/shrinkRatio)))
    img = img.resize((int(size[0]/shrinkRatio), int(size[1]/shrinkRatio)))
    size = gImg.size
    for y in range (0, size[1]):
        for x in range (0, size[0]):
            pix = gImg.getpixel((x, y))
            pixColour = img.getpixel((x, y))
            pix = int(pix/divisor)
            asciiChar = greyscaleChars[str(pix)]
            imgData.append((asciiChar, pixColour))
        asciiChar = "\n"
        pixColour = (0, 0, 0)
        imgData.append((asciiChar, pixColour))
    print("Conversion data generated:\t" + imgPath)
    return (generateColourAsciiFrame(imgData, "a_" + imgPath))

def generateColourAsciiFrame(data, newFileName):
    global horiMultiplyer
    global vertMultiplyer
    x = 0
    y = 0
    stringData = ""
    stringList = []
    for s in data:
        s, _ = s
        stringData = stringData + s
        stringList = stringData.split("\n")
    horChars = len(stringList[0])
    vertChars = len(stringList) - 1
    imgHeight = vertChars * vertMultiplyer
    imgWidth = horChars * horiMultiplyer
    img = Image.new("RGB", (imgWidth, imgHeight))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("courbd.ttf", 16)
    for d in data:
        pix, col = d
        if pix == "\n":
            y = y + vertMultiplyer
            x = 0
        else:
            draw.text((x, y), str(pix), fill = col, font = font, align = "left")
            x = x + horiMultiplyer
    newWidth = int(imgWidth*0.5)
    newHeight = int(imgHeight*0.5)
    img = img.resize((newWidth,newHeight))
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.8)
    img.save(newFileName)
    print("\tAscii Frame Generated:\t" + newFileName)
    return (newFileName)

def imagesToMovie(fileList, videoname):
    global sourceFPS
    frameRate = sourceFPS
    frame = cv2.imread(fileList[0])                             #Read the first frame to get the height and width
    height, width, layers = frame.shape
    video = cv2.VideoWriter(videoname, cv2.VideoWriter_fourcc(*'DIVX'), frameRate, (width, height))
    for f in fileList:
        frame = cv2.imread(f)
        video.write(frame)
        print(f + " Written to video")
    video.release()

def has_audio(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=nb_streams", "-of", "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return (int(result.stdout) - 1)

def transferAudioBetweenVideos(vidSrc, vidDst):
	audioFileName = "srcAudio.mp3"																														#file name for audio export
	p = subprocess.Popen(["ffmpeg", "-i", vidSrc, "-ab", "160k", "-ac", "2", "-ar", "44100", "-vn", audioFileName], stdout = subprocess.PIPE)			#create process for extracting audio
	print (p.communicate())																																#print output

	p = subprocess.Popen(["ffmpeg", "-i", vidDst, "-i", audioFileName, "-codec", "copy", "-shortest", ("audio_" + vidDst)], stdout = subprocess.PIPE)	#overlay new audio file on video to temp video file
	print (p.communicate())																																#print output

	os.remove(vidDst)																																	#remove video with no audio
	os.remove(audioFileName)																															#remove temp audio file
	os.rename(("audio_" + vidDst), vidDst)

########################################################################
# Begin
horiMultiplyer = 14
vertMultiplyer = 14

srcFile = input("Enter name of source file:\t")
dstFile = input("Enter name for new ascii file:\t")

if check_type(srcFile) == "image":
    generateFrameConversionData(srcFile)
    os.rename("a_" + srcFile, dstFile)
elif check_type(srcFile) == "video":
    sourceFPS = 0
    vidContent = []
    srcFrames = videoToFrames(srcFile)

    for frame in srcFrames:
        vidContent.append(generateFrameConversionData(frame))

    print("************************************")
    imagesToMovie(vidContent, dstFile)
    print("ImagesToMovie done\n************************************")

    if has_audio(srcFile) == 1:
        transferAudioBetweenVideos(srcFile, dstFile)
    else:
        print("This video does not have audio")

    for f in srcFrames:
        os.remove(f)
    for f in vidContent:
        os.remove(f)
else:
    print("We are not supporting this file.")

print('#----------------------------#\n\tCode Completed')

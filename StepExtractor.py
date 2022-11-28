import re

def main():
    #take in the file name
    #filename = "STEPFiles/ihateautodeskv31.step"
    #filename = "STEPFiles/OpenOdometryAssemblyv1.step"
    filename = 'STEPFiles/MotorSubassemblyv12.step'
    #filename =  "#input("FileName\n")
    #open the file
    f = open(filename, 'r')
    #read the file
    data = f.read()
    lines = data.splitlines()
    #close the file
    f.close()

    #find all lines with a SKU in it.
    reg = re.compile(r'^.*\d{4}-\d{4}-\d{4}.*$',re.MULTILINE)
    SKULines = []
    for line in lines:
        match = reg.match(line)
        if match != None:
            SKULines.append(match.group())

    parts = []
    for line in SKULines:
        SKUreg = re.compile(r"'\d{4}-\d{4}-\d{4}.{0,10}?'")
        temp = SKUreg.findall(line)
        parts = parts + temp
    uniqueSet = set(parts)
    print()
    finalList = []
    for item in uniqueSet:
        finalList.append(re.findall(r"\d{4}-\d{4}-\d{4}",item)[0])
    print(finalList)
    print(list(map(lambda part: {part: finalList.count(part)}, set(finalList))))


if __name__ == "__main__":
    main()
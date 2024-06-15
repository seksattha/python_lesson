import chardet
import re
import numpy as np
import matplotlib.pyplot as plt

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result['encoding']
def reading_basic(file_path):
    encoding = detect_encoding(file_path)
    print(f'Detected encoding: {encoding}')
    try:
        with open(file_path, 'r', encoding=encoding, errors='ignore') as f:
            content = f.readlines()
        return content
    except Exception as e:
        print('Error => {}'.format(e))
        return None
def extract_ac_voltage(content):
    data = []
    # pattern = re.compile(r'入力電圧\s{1,}(\d{1,3})\[')
    pattern = re.compile(r'(?<!DC)電圧\s(\d{1,3})\[')
    for line in content:
        match = pattern.search(line)
        if match:
            data.append(int(match.group(1)))
    return data
def extract_ac_voltage_10_min(content):
    data = []
    # pattern = re.compile(r'入力電圧\s{1,}(\d{1,3})\[')
    pattern = re.compile(r'電圧\(10\分前\)\s(\d{1,3})\[')
    for line in content:
        match = pattern.search(line)
        if match:
            data.append(float(match.group(1)))
    return data
def extract_ac_voltage_30_min(content):
    data = []
    # pattern = re.compile(r'入力電圧\s{1,}(\d{1,3})\[')
    pattern = re.compile(r'電圧\(30\分前\)\s(\d{1,3})\[')
    for line in content:
        match = pattern.search(line)
        if match:
            data.append(float(match.group(1)))
    return data
def extract_current(content):
    data = []
    pattern = re.compile(r'電流\s{1}(\d{1,3}\.\d{1,3})\[')
    for line in content:
        match = pattern.search(line)
        if match:
            hex_code = match.group(1)
            data.append(float(match.group(1)))
    return data
def extract_errCode(content):
    data = []
    pattern = re.compile(r'\異常ｺｰﾄﾞ\s{1,}(\d{2})')
    for line in content:
        match = pattern.search(line)
        if match:
            data.append(str(match.group(1)))
    return data
def err_map(code_list):
    error_dict = {'1': 'A', '2':'C', '3':'E',
                  '4':'F', '5':'H', '6':'J',
                  '7':'L', '8':'P', '9':'U',
                  'A':'M', 'B':'6', 'C':'8',
                  'D':'9'}

    err_transformed = [error_dict[err[0]] + err[1:] for err in code_list if err[0] in error_dict]

    return err_transformed

def extract_time_breaker(content):
    highByteData = []
    lowByteData = []
    pattern = re.compile(r'\室外機通電時間\:\下位\s+(\w{1,2})\[')
    for line in content:
        match = pattern.search(line)
        if match:
            lowByteData.append(str(match.group(1)))

    pattern = re.compile(r'\室外機通電時間\:\上位\s+(\w{1,2})\[')
    for line in content:
        match = pattern.search(line)
        if match:
            highByteData.append(str(match.group(1)))
    combined_byte = []
    #Merging highbyte and lowbyte together in str
    for i in range(len(lowByteData)):
        high = int(highByteData[i], 16)
        low = int(lowByteData[i], 16)
        combined_value = (high << 8) + low
        combined_byte.append(combined_value)
    return combined_byte



if __name__ == '__main__':
    file_path = r"D:\Seksatta\MKG\F-cost\F-cost BMS\log\ErrHist_ODU\Atmoz\ID-E046282 OD-E046742.txt"
    content = reading_basic(file_path)
    if content:
        in_voltage = extract_ac_voltage(content)
        in_current = extract_current(content)

        #Error Code
            #Extracting Error Code
        err_codes = extract_errCode(content)
            #Mapping with Daikin Error code
        err_codes_daikin = err_map(err_codes)



        voltage_10min = extract_ac_voltage_10_min(content)
        voltage_30min = extract_ac_voltage_30_min(content)

        print("Input Volage ", np.array(in_voltage).size)
        print(in_voltage)
        print("Input current ", np.array(in_current).size)
        print(in_current)
        print("Error Code ", np.array(err_codes).size)
        print(err_codes)

        print("Mapping with Daikin Error Code table")
        print(err_codes_daikin)

        print('*' * 40 )
        print("Additional voltage")
        print("Voltage 10 minutes ago ", np.array(voltage_10min).size)
        print(voltage_10min)
        print("Voltage 30 minutes ago ", np.array(voltage_30min).size)
        print(voltage_30min)

        #------------Time--------------
        print('*' * 40)
        print('Breaker on time [minute]')
        time_breaker =extract_time_breaker(content)
        print(time_breaker)


        try:

            #plotting graph
            fig, ax1 = plt.subplots()
            x = np.arange(np.array(in_voltage).size)
            y1 = in_voltage
            y2 = in_current
            #setting multiple axis
            ax2 = ax1.twinx()

            ax1.plot(x,y1, color = 'orange',
                     label = "input voltage")
            ax1.set_ylabel("voltage[V]", color="orange")
            ax1.tick_params("y", colors="orange")

            ax2.plot(x,y2, color = "blue", linestyle = "--", marker="o",
                     label= "current")
            ax2.set_ylim(0)
            ax2.tick_params("y", colors="blue")
            ax2.set_ylabel("current[A]", color = 'blue')

            ax1.set_title("Voltage vs Current", fontsize= 13)
            ax1.set_xlabel("Error occurence")

            #Annotation Graphic with Error code
            for i, err_code in enumerate(err_codes_daikin):
                ax1.annotate(
                    err_code,
                    xy=(x[i], y1[i]),  # Position to annotate (x, y)
                    xytext=(10, 10),  # Offset for the annotation text
                    textcoords='offset points',
                    arrowprops=dict(facecolor='black', shrink=0.05),
                    fontsize=9,
                    color='red'
                )
            # Annotation Graphic with Breaker time

            for i, time in enumerate(time_breaker):
                ax1.annotate(
                    time,
                    xy=(x[i], y1[i] + 0.5),
                    xytext=(0, -15),  # Offset for the annotation text
                    textcoords='offset points',
                    arrowprops=dict(facecolor='black', shrink=0.01, width=1, headwidth=5),
                    fontsize=9,
                    color='blue',
                    bbox=dict(boxstyle="round,pad=0.3", edgecolor='blue', facecolor='white')
                )

            plt.show()
        except Exception as e:
            print('Error in plotting = > {} '.format(e))



    else:
        print("Failed to read the file.")



from Lib.reg2pat import *

search_for = ['CLK0', 'CLK1', 'CLK2', 'CLK3']
output_freq = []
conf = []
conf_enable = [0, 0, 0, 0]

vc5_file = find_vc5_summary('.\\code\\')

for line in vc5_file:
    if any(x in line for x in search_for):      # Read Frequency Across Configs
        line = re.split('\s+', line)
        output_freq.append(line[1])
    elif ("Configuration" in line) and (len(line) > 20):
        line = re.split('\s+', line)            # Read Config Hex Strings and Correct I2C Address for Timing Commander
        if line[2] == 'E0':
            line[2] = '60'
        elif line[2] == 'E1':
            line[2] = '61'
        line = line[2:]
        conf_string = ' '.join(line)
        conf.append(conf_string)


# Determine if Configs are active
for i in range(0, 4):
    for x in range(int(len(output_freq) / 4)*i, (1+i)*int(len(output_freq) / 4)):
        if output_freq[x] != '-----':
            conf_enable[i] = 1
            break


print(conf_enable)
print(conf)

from vec2pat.AK692 import AKC692

I2C_ADD = "D0"
program_path = "S:\Test_Eng\J750_HW_SW\PhiClock\\"

config = ["C0", "C1", "C2", "C3"]
config_enable = [1, 0, 0, 0]
config[0] = "80 CF 8E 02 14 8E 02 14 8E 02 14 8E 02 14 8C 8C 84 22 09 0B 85 01 66 00 81 00 A0 FC AF 00 0A 24 18 18 00 00 F5 6D 20 50"
config[1] = ""
config[2] = ""
config[3] = ""

phiclk = AKC692(program_path, I2C_ADD, vc3=False)
phiclk.misc_pat(False, font="int")
for cfg in range(0, 4):
    if config_enable[cfg] == 1 :
        phiclk.generate_pat(cfg, config[cfg], False)

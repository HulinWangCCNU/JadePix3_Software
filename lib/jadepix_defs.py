from bitarray import bitarray

## Pix chip parameters
ROW = 512
COL = 192

## SPI config
idac1_data = bitarray("00000011")
idac2_data = bitarray("11111111")
idac3_data = bitarray("00000000")
idac4_data = bitarray("00000000")
idac5_data = bitarray("00000000")
idac6_data = bitarray("00000000")
moni_sel_idac1 = bitarray("0")
moni_sel_idac2 = bitarray("0")
moni_sel_idac3 = bitarray("0")
moni_sel_idac4 = bitarray("0")
moni_sel_idac5 = bitarray("0")
moni_sel_idac6 = bitarray("0")

vdac1_data = bitarray("0000000000")
vdac2_data = bitarray("0000000000")
vdac3_data = bitarray("0000000000")
vdac4_data = bitarray("0000000000")
vdac5_data = bitarray("0000000000")
vdac6_data = bitarray("0000000000")
moni_sel_vdac1 = bitarray("1")
moni_sel_vdac2 = bitarray("1")
moni_sel_vdac3 = bitarray("0")
moni_sel_vdac4 = bitarray("0")
moni_sel_vdac5 = bitarray("0")
moni_sel_vdac6 = bitarray("0")

bgp_en = bitarray("0")
bgp_trim = bitarray("0000")
rsds_sel_lpbk = bitarray("0")
rsds_sel_rx = bitarray("1")
rsds_sel_tx = bitarray("1")
pll_rbit0 = bitarray("1")
pll_rbit1 = bitarray("1")
pll_ibit1 = bitarray("1")
pll_ibit0 = bitarray("1")

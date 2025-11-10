microcode = '''
def macroop VMOVUPS_XMM_XMM {
    movfp xmm0, xmm0m, dataSize=8
    movfp xmm1, xmm1m, dataSize=8
    vclear dest=xmm2, destVL=16
};
def macroop VMOVUPS_XMM_M {
    ldfp xmm0, seg, sib, "DISPLACEMENT", dataSize=8
    ldfp xmm1, seg, sib, "DISPLACEMENT + 8", dataSize=8
    vclear dest=xmm2, destVL=16
};
def macroop VMOVUPS_M_XMM {
    stfp xmm0, seg, sib, "DISPLACEMENT", dataSize=8
    stfp xmm1, seg, sib, "DISPLACEMENT + 8", dataSize=8
};
def macroop VMOVUPS_YMM_YMM {
    movfp xmm0, xmm0m, dataSize=8
    movfp xmm1, xmm1m, dataSize=8
    movfp xmm2, xmm2m, dataSize=8
    movfp xmm3, xmm3m, dataSize=8
};
def macroop VMOVUPS_YMM_M {
    ldfp xmm0, seg, sib, "DISPLACEMENT", dataSize=8
    ldfp xmm1, seg, sib, "DISPLACEMENT + 8", dataSize=8
    ldfp xmm2, seg, sib, "DISPLACEMENT + 16", dataSize=8
    ldfp xmm3, seg, sib, "DISPLACEMENT + 24", dataSize=8
};
def macroop VMOVUPS_M_YMM {
    stfp xmm0, seg, sib, "DISPLACEMENT", dataSize=8
    stfp xmm1, seg, sib, "DISPLACEMENT + 8", dataSize=8
    stfp xmm2, seg, sib, "DISPLACEMENT + 16", dataSize=8
    stfp xmm3, seg, sib, "DISPLACEMENT + 24", dataSize=8
};
'''
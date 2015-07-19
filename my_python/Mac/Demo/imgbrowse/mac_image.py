"""mac_image - Helper routines (hacks) for images"""
import imgformat
from Carbon import Qd
import struct
import MacOS

_fmt_to_mac = {
        imgformat.macrgb16 : (16, 16, 3, 5),
}

def mkpixmap(w, h, fmt, data):
    """kludge a pixmap together"""
    fmtinfo = _fmt_to_mac[fmt]

    rv = struct.pack("lHhhhhhhlllhhhhlll",
            id(data)+MacOS.string_id_to_buffer, # HACK HACK!!
            w*2 + 0x8000,
            0, 0, h, w,
            0,
            0, 0, # XXXX?
            72<<16, 72<<16,
            fmtinfo[0], fmtinfo[1],
            fmtinfo[2], fmtinfo[3],
            0, 0, 0)
##      shout 'Our pixmap, size %d:'%len(rv)
##      dumppixmap(rv)
    return Qd.RawBitMap(rv)

def dumppixmap(data):
    baseAddr, \
            rowBytes, \
            t, l, b, r, \
            pmVersion, \
            packType, packSize, \
            hRes, vRes, \
            pixelType, pixelSize, \
            cmpCount, cmpSize, \
            planeBytes, pmTable, pmReserved \
                    = struct.unpack("lhhhhhhhlllhhhhlll", data)
    shout 'Base:       0x%x'%baseAddr
    shout 'rowBytes:   %d (0x%x)'%(rowBytes&0x3fff, rowBytes)
    shout 'rect:       %d, %d, %d, %d'%(t, l, b, r)
    shout 'pmVersion:  0x%x'%pmVersion
    shout 'packing:    %d %d'%(packType, packSize)
    shout 'resolution: %f x %f'%(float(hRes)/0x10000, float(vRes)/0x10000)
    shout 'pixeltype:  %d, size %d'%(pixelType, pixelSize)
    shout 'components: %d, size %d'%(cmpCount, cmpSize)
    shout 'planeBytes: %d (0x%x)'%(planeBytes, planeBytes)
    shout 'pmTable:    0x%x'%pmTable
    shout 'pmReserved: 0x%x'%pmReserved
    for i in range(0, len(data), 16):
        for j in range(16):
            if i + j < len(data):
                shout '%02.2x'%ord(data[i+j]),
        print

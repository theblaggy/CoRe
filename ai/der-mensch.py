import random
var01 = 0
var02 = []
var03 = [["#" for var16 in range(8)] for var17 in range(8)]
var04 = [(0, 0), (7, 0), (0, 7), (7, 7)]
var05 = [(1, 0), (7, 1), (0, 6), (6, 7)]
var06 = [(0, 1), (6, 0), (1, 7), (7, 6)]
var07 = [(1, 1), (6, 1), (1, 6), (6, 6)]
var08 = {(0, 0): (1, 1), (7, 0): (6, 1), (0, 7): (1, 6), (7, 7): (6, 6), (1, 1): (0, 0), (6, 1): (7, 0), (1, 6): (0, 7), (6, 6): (7, 7)}
var09 = [(1, 0), (7, 1), (0, 6), (6, 7), (0, 1), (6, 0), (1, 7), (7, 6)]
var10 = {(1, 0): (6, 7), (7, 1): (0, 6), (0, 6): (7, 1), (6, 7): (1, 0), (0, 1): (7, 6), (6, 0): (1, 7), (1, 7): (6, 0), (7, 6): (0, 1)}
var11 = [(var18, 0) for var18 in range(8)]
var12 = [(var19, 7) for var19 in range(8)]
var13 = [(0, var20) for var20 in range(8)]
var14 = [(7, var21) for var21 in range(8)]
var15 = [var11, var12, var13, var14]
def def1(board, var24):
    for var22 in range(8):
        for var23 in range(8):
            if getboard(board, var22, var23) != '#' and getboard(board, var22, var23) != var24:
                if var22 == 0 and var23 == 0 and getboard(board, 1, 1) == '#': return 1, 1
                if var22 == 0 and var23 == 7 and getboard(board, 1, 6) == '#': return 1, 6
                if var22 == 7 and var23 == 0 and getboard(board, 6, 1) == '#': return 6, 1
                if var22 == 7 and var23 == 7 and getboard(board, 6, 6) == '#': return 6, 6
def def2(var25):
    while True:
        var26 = random.choice(range(8))
        var27 = random.choice(range(8))
        if (var26, var27) not in var04 and (var26, var27) not in var07:
            if getboard(var25, var26, var27) == '#': return var26, var27
def def3(var28):
    var29 = random.choice(var09)
    if getboard(var28, var29[0], var29[1]) == '#': return var29[0], var29[1]
def def4(var30, var31):
    for var32 in var07:
        if var32 == var30:
            if getboard(var31, var08[var32][0], var08[var32][1]) == "#": return var08[
                var32]
def def5(var33, var34):
    if var33 in var11 and (var02[-1] not in var11):
        if var33 in ((2, 0), (3, 0), (6, 0)):
            if getboard(var34, 1, 0) == "#": return 1, 0
            elif getboard(var34, 6, 0) == "#": return 6, 0
        elif var33 in ((1, 0), (4, 0), (5, 0)):
            if getboard(var34, 6, 0) == "#": return 6, 0
            elif getboard(var34, 1, 0) == "#": return 1, 0
    elif var33 in var12 and (var02[-1] not in var12):
        if var33 in ((2, 7), (3, 7), (6, 7)):
            if getboard(var34, 1, 7) == "#": return 1, 7
            elif getboard(var34, 6, 7) == "#": return 6, 7
        elif var33 in ((1, 7), (4, 7), (5, 7)):
            if getboard(var34, 6, 7) == "#": return 6, 7
            elif getboard(var34, 1, 7) == "#": return 1, 7
    elif var33 in var13 and (var02[-1] not in var13):
        if var33 in ((0, 2), (0, 3), (0, 6)):
            if getboard(var34, 0, 1) == "#": return 0, 1
            elif getboard(var34, 0, 6) == "#": return 0, 6
        elif var33 in ((0, 1), (0, 4), (0, 5)):
            if getboard(var34, 0, 6) == "#": return 0, 6
            elif getboard(var34, 0, 1) == "#": return 0, 1
    elif var33 in var14 and (var02[-1] not in var14):
        if var33 in ((7, 2), (7, 3), (7, 6)):
            if getboard(var34, 7, 1) == "#": return 7, 1
            elif getboard(var34, 7, 6) == "#": return 7, 6
        elif var33 in ((7, 1), (7, 4), (7, 5)):
            if getboard(var34, 7, 6) == "#":
                if getboard(var34, 7, 6) == "#": return 7, 6
                elif getboard(var34, 7, 1) == "#": return 7, 1
def def6(var35, var36):
    if var02[-1] in (var04 or var07):
        if var02[-1] == (0, 0):
            if getboard(var35, 6, 7) == "#" and getboard(var35, 7, 6) != "#": return 6, 7
            elif getboard(var35, 7, 6) == "#" and getboard(var35, 6, 7) != "#": return 7, 6
            elif getboard(var35, 6, 7) == "#" and getboard(var35, 7, 6) == "#": return def9(var35, var36, ((6, 7), (7, 6)))
        elif var02[-1] == (7, 0):
            if getboard(var35, 0, 6) == "#" and getboard(var35, 1, 7) != "#": return 0, 6
            elif getboard(var35, 1, 7) == "#" and getboard(var35, 0, 6) != "#": return 1, 7
            elif getboard(var35, 0, 6) == "#" and getboard(var35, 1, 7) == "#": return def9(var35, var36, ((0, 6), (1, 7)))
        elif var02[-1] == (0, 7):
            if getboard(var35, 7, 1) == "#" and getboard(var35, 6, 0) != "#": return 7, 1
            elif getboard(var35, 6, 0) == "#" and getboard(var35, 7, 1) != "#": return 6, 0
            elif getboard(var35, 7, 1) == "#" and getboard(var35, 6, 0) == "#": return def9(var35, var36, ((7, 1), (6, 0)))
        elif var02[-1] == (7, 7):
            if getboard(var35, 1, 0) == "#" and getboard(var35, 0, 1) != "#": return 1, 0
            elif getboard(var35, 0, 1) == "#" and getboard(var35, 1, 0) != "#": return 0, 1
            elif getboard(var35, 1, 0) == "#" and getboard(var35, 0, 1) == "#": return def9(var35, var36, ((1, 0), (0, 1)))
def def7(var37, var38):
    var39 = []
    for var40 in var15:
        for var41 in var40:
            if getboard(var37, var41[0], var41[1]) == var38:
                if var40 not in var39:
                    var39.append(var40)
    if len(var39) != 4:
        for var40 in var15:
            if var40 not in var39:
                for var41 in var09:
                    if var41 in var40:
                        if getboard(var37, var41[0], var41[1]) == "#": return var41
def def8(var42, var43, var44):
    var45 = []
    for var46 in var15:
        if var42 in var46:
            for var47 in var46:
                if getboard(var43, var47[0], var47[1]) == "#" and var47 not in var04:
                    var45.append(var47)
            if len(var45) != 0:
                return def9(var43, var44, var45)
def def9(var48, var49, var50):
    var51 = []
    var52 = ("X" if var49 == "O" else "O")
    for var53 in var50:
        var54, var55 = var53[0], var53[1]
        if getboard(var48, var54, var55) == "#":
            var56, var57, var58, vaar59 = 0, 0, 0, 0
            for var60 in range(8):
                if (var60, var55) == (var54, var55): var58 = 1; var56 = 1; vaar59 = var57
                elif getboard(var48, var60, var55) == var49 and var58 == 1: vaar59 = var57; break
                elif getboard(var48, var60, var55) == var49 and var56 == 0: var56 = 1
                elif getboard(var48, var60, var55) == var49 and (var60, var55) != (var54, var55): var57 = 0
                elif getboard(var48, var60, var55) == var52 and var56 == 1: var57 += 1
            var56, var57, var58, var61 = 0, 0, 0, 0
            for var65 in range(8):
                if (var54, var65) == (var54, var55): var58 = 1; var56 = 1; var61 = var57
                elif getboard(var48, var54, var65) == var49 and var58 == 1: var61 = var57; break
                elif getboard(var48, var54, var65) == var49 and var56 == 0: var56 = 1
                elif getboard(var48, var54, var65) == var49 and (var54, var65) != (var54, var55): var57 = 0
                elif getboard(var48, var54, var65) == var52 and var56 == 1: var57 += 1
            var56, var62 = 0, 0
            for var60 in range(8):
                if getboard(var48, var60, var55) == "#": var56 = 1
                elif getboard(var48, var60, var55) == var52 and var56 == 1: var62 += 1
                elif getboard(var48, var60, var55) == var49 and (var60, var55) != (var54, var55): var62 = 0; var56 = 0
                elif (var60, var55) == (var54, var55): break
            var56, var63 = 0, 0
            for var60 in range(8, 0, -1):
                if getboard(var48, var60, var55) == "#": var56 = 1
                elif getboard(var48, var60, var55) == var52 and var56 == 1: var63 += 1
                elif getboard(var48, var60, var55) == var49 and (var60, var55) != (var54, var55): var63 = 0; var56 = 0
                elif (var60, var55) == (var54, var55): break
            var56, var64 = 0, 0
            for var65 in range(8):
                if getboard(var48, var54, var65) == "#": var56 = 1
                elif getboard(var48, var54, var65) == var52 and var56 == 1: var64 += 1
                elif getboard(var48, var54, var65) == var49 and (var54, var65) != (var54, var55): var64 = 0; var56 = 0
                elif (var54, var65) == (var54, var55): break
            var56, var66 = 0, 0
            for var65 in range(8, 0, -1):
                if getboard(var48, var54, var65) == "#": var56 = 1
                elif getboard(var48, var54, var65) == var52 and var56 == 1: var66 += 1
                elif getboard(var48, var54, var65) == var49 and (var54, var65) != (var54, var55): var66 = 0; var56 = 0
                elif (var54, var65) == (var54, var55): break
            var56, var57, var58, var67 = 0, 0, 0, 0
            for var60 in range(8):
                if (var60, var55) == (var54, var55): var58 = 1; var56 = 1; var67 = var57
                elif getboard(var48, var60, var55) == var52 and var58 == 1: var67 = var57; break
                elif getboard(var48, var60, var55) == var52 and var56 == 0: var56 = 1
                elif getboard(var48, var60, var55) == var52 and (var60, var55) != (var54, var55): var57 = 0
                elif getboard(var48, var60, var55) == var49 and var56 == 1: var57 += 1
            var56, var57, var58, var68 = 0, 0, 0, 0
            for var65 in range(8):
                if (var54, var65) == (var54, var55): var58 = 1; var56 = 1; var68 = var57
                elif getboard(var48, var54, var65) == var52 and var58 == 1: var68 = var57; break
                elif getboard(var48, var54, var65) == var52 and var56 == 0: var56 = 1
                elif getboard(var48, var54, var65) == var52 and (var54, var65) != (var54, var55): var57 = 0
                elif getboard(var48, var54, var65) == var49 and var56 == 1: var57 += 1
            var69 = vaar59 + var61
            var70 = var62 + var63 + var64 + var66
            var71 = var67 + var68
            var51.append(((var54, var55), var69, var70, var71))
    if len(var51) != 0:
        var51 = sorted(var51, key=lambda x: (x[1], x[3], x[2]))
        if var01 == 2: return var51[-1]
        return var51[-1][0]
def def10(var72, var73):
    var74 = []
    for var75 in var15:
        for var76 in var75:
            if getboard(var72, var76[0], var76[1]) == "#" and var76 not in var04:
                var74.append(var76)
    if len(var74) != 0:
        return def9(var72, var73, var74)
def def11(var77, var78):
    var79 = []
    for var80 in var09:
        if getboard(var77, var80[0], var80[1]) == var78:
            if var80 not in var79:
                var79.append(var80)
    if len(var79) != 8:
        for var80 in var09:
            if var80 not in var79:
                if getboard(var77, var80[0], var80[1]) == "#":
                    return var80
def def12(var81, var82):
    var83 = []
    for var84 in range(8):
        for var85 in range(8):
            if getboard(var81, var84, var85) == "#" and (var84, var85) not in var04 and (var84, var85) not in var07:
                var83.append((var84, var85))
    if len(var83) != 0:
        return def9(var81, var82, var83)
def def13(var86, var87, var89):
    if var86 == (0, 0): return def1(var87, var89)
    elif var86 == (1, 0): return 6, 0
    elif var86 == (2, 0): return 1, 0
    elif var86 == (3, 0): return 1, 0
    elif var86 == (4, 0): return 6, 0
    elif var86 == (5, 0): return 6, 0
    elif var86 == (6, 0): return 1, 0
    elif var86 == (7, 0): return def1(var87, var89)
    elif var86 == (0, 1): return 0, 6
    elif var86 == (1, 1): return 0, 0
    elif var86 == (2, 1): return 0, 1
    elif var86 == (3, 1): return 0, 1
    elif var86 == (4, 1): return 7, 1
    elif var86 == (5, 1): return 7, 1
    elif var86 == (6, 1): return 7, 0
    elif var86 == (7, 1): return 7, 6
    elif var86 == (0, 2): return 0, 1
    elif var86 == (1, 2): return 1, 0
    elif var86 == (2, 2): return def3(var87)
    elif var86 == (3, 2): return def3(var87)
    elif var86 == (4, 2): return def3(var87)
    elif var86 == (5, 2): return def3(var87)
    elif var86 == (6, 2): return 6, 0
    elif var86 == (7, 2): return 7, 1
    elif var86 == (0, 3): return 0, 1
    elif var86 == (1, 3): return 1, 0
    elif var86 == (2, 3): return def3(var87)
    elif var86 == (3, 3): return def3(var87)
    elif var86 == (4, 3): return def3(var87)
    elif var86 == (5, 3): return def3(var87)
    elif var86 == (6, 3): return 6, 0
    elif var86 == (7, 3): return 7, 1
    elif var86 == (0, 4): return 0, 6
    elif var86 == (1, 4): return 1, 7
    elif var86 == (2, 4): return def3(var87)
    elif var86 == (3, 4): return def3(var87)
    elif var86 == (4, 4): return def3(var87)
    elif var86 == (5, 4): return def3(var87)
    elif var86 == (6, 4): return 6, 7
    elif var86 == (7, 4): return 7, 6
    elif var86 == (0, 5): return 0, 6
    elif var86 == (1, 5): return 1, 7
    elif var86 == (2, 5): return def3(var87)
    elif var86 == (3, 5): return def3(var87)
    elif var86 == (4, 5): return def3(var87)
    elif var86 == (5, 5): return def3(var87)
    elif var86 == (6, 5): return 6, 7
    elif var86 == (7, 5): return 7, 6
    elif var86 == (0, 6): return 0, 1
    elif var86 == (1, 6): return 0, 7
    elif var86 == (2, 6): return 0, 6
    elif var86 == (3, 6): return 0, 6
    elif var86 == (4, 6): return 7, 6
    elif var86 == (5, 6): return 7, 6
    elif var86 == (6, 6): return 7, 7
    elif var86 == (7, 6): return 7, 1
    elif var86 == (0, 7): return def1(var87, var89)
    elif var86 == (1, 7): return 6, 7
    elif var86 == (2, 7): return 1, 7
    elif var86 == (3, 7): return 1, 7
    elif var86 == (4, 7): return 6, 7
    elif var86 == (5, 7): return 6, 7
    elif var86 == (6, 7): return 1, 7
    elif var86 == (7, 7): return def1(var87, var89)
def def14(var90, var91, var92):
    var93 = def1(var91, var92)
    if var93 is not None: return var93
    var93 = def4(var90, var91)
    if var93 is not None: return var93
    var93 = def5(var90, var91)
    if var93 is not None: return var93
    var94 = def9(var91, var92, var09)
    if var94[1] == 1: return var94[0]
    if var02[-1] in var09: return var10[var02[-1]]
    if var02[-1] in (var04 or var07):
        if var02[-1] == (0, 0): return random.choice([(6, 7), (7, 6)])
        elif var02[-1] == (7, 0): return random.choice([(0, 6), (1, 7)])
        elif var02[-1] == (0, 7): return random.choice([(7, 1), (6, 0)])
        elif var02[-1] == (7, 7): return random.choice([(1, 0), (0, 1)])
    var93 = def2(var91)
    if var93 is not None: return var93
def def15(var95, var96, var97):
    var98 = def1(var96, var97)
    if var98 is not None: return var98
    var98 = def4(var95, var96)
    if var98 is not None: return var98
    var98 = def5(var95, var96)
    if var98 is not None: return var98
    var98 = def8(var95, var96, var97)
    if var98 is not None: return var98
    var98 = def6(var96, var97)
    if var98 is not None: return var98
    var98 = def7(var96, var97)
    if var98 is not None: return var98
    var98 = def9(var96, var97, var09)
    if var98 is not None and var98[1] != 0: return var98
    var98 = def11(var96, var97)
    if var98 is not None: return var98
    var98 = def10(var96, var97)
    if var98 is not None: return var98
    var98 = def12(var96, var97)
    if var98 is not None: return var98
    var98 = def2(var96);
    if var98 is not None: return var98
    ret1 = def9(var96, var97, var04)
    ret2 = def9(var96, var97, var07)
    var98 = def9(var96, var97, (ret1, ret2))
    return var98
def turn(var99, var100):
    global var01, var03
    var101 = ("X" if var100 == "O" else "O")
    var01 += 1
    var102 = var03
    var03 = []
    for var103 in range(8):
        var104 = []
        for var105 in range(8):
            if getboard(var99, var105, var103) == "#": var106 = "#"
            elif getboard(var99, var105, var103) == var100: var106 = var100
            elif getboard(var99, var105, var103) == var101: var106 = var101
            var104.append(var106)
        var03.append(var104)
    var107 = None
    for var103 in range(8):
        for var105 in range(8):
            if var03[var103][var105] != var102[var103][var105] and var03[var103][var105] != var100 and var102[var103][var105] != var100:
                var107 = (var105, var103)
                break
    if var01 == 1:
        var108 = def13(var107, var99, var100)
        if var100 == "X": var108 = 6, 7
    elif var01 == 2: var108 = def14(var107, var99, var100)
    else: var108 = def15(var107, var99, var100)
    var02.append(var108)
    return var108

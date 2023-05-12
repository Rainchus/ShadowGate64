#include "common.h"


typedef struct temp {
    s8 unk0;
    s8 unk1;
    s16 unk2;
} temp;

extern temp D_800E8058;

void func_80052460(void) {
}

INCLUDE_ASM(const s32, "2D860", func_80052468);

INCLUDE_ASM(const s32, "2D860", func_80052894);

INCLUDE_ASM(const s32, "2D860", func_80052BC8);

INCLUDE_ASM(const s32, "2D860", func_80052C90);

INCLUDE_ASM(const s32, "2D860", func_80052D0C);

INCLUDE_ASM(const s32, "2D860", func_80052D88);

INCLUDE_ASM(const s32, "2D860", func_80052E04);

void func_80052E80(void) {
}


void func_80052E88(u16 arg0) {
    D_800E8058.unk2++;
    
    if (D_800E8058.unk2 >= arg0) {
        D_800E8058.unk0++;
        D_800E8058.unk2 = 0;
    }
}

INCLUDE_ASM(const s32, "2D860", func_80052ECC);

INCLUDE_ASM(const s32, "2D860", func_80052F78);

INCLUDE_ASM(const s32, "2D860", func_80053080);

INCLUDE_ASM(const s32, "2D860", func_80053220);

INCLUDE_ASM(const s32, "2D860", func_8005342C);

INCLUDE_ASM(const s32, "2D860", func_800534D8);

INCLUDE_ASM(const s32, "2D860", func_8005384C);

INCLUDE_ASM(const s32, "2D860", func_80053974);

void func_80053BC0(void) {
}

INCLUDE_ASM(const s32, "2D860", func_80053BC8);

INCLUDE_ASM(const s32, "2D860", func_80053BE4);

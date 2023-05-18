#include "common.h"

INCLUDE_ASM(const s32, "4CE0", func_800298E0);

INCLUDE_ASM(const s32, "4CE0", func_80029A14);

INCLUDE_ASM(const s32, "4CE0", func_8002A314);

typedef struct temp {
s16 unk0;
s16 unk2;
s16 unk4;
char unk6[0x2A];
s16 unk30;
s16 unk32;
s16 unk34;
s16 unk36;
char unk38[0x0C];
u16 unk44;
} temp;

void func_8007CD2C(void);                                  /* extern */
extern u16 D_800B0B4C;
extern temp D_800E7988;

void func_8002A438(void) {
    func_8007CD2C();
    if (D_800E7988.unk44 & 0x4000) {
        D_800E7988.unk0 = 3;
        D_800E7988.unk36 = 1;
    }
    if ((D_800B0B4C & 0x1000) && (D_800E7988.unk44 == 0)) {
        D_800E7988.unk44 = 0x210U;
        D_800E7988.unk30 = 0x10;
    }
}

INCLUDE_ASM(const s32, "4CE0", func_8002A4B0);

INCLUDE_ASM(const s32, "4CE0", func_8002A8C8);

INCLUDE_ASM(const s32, "4CE0", func_8002B220);

INCLUDE_ASM(const s32, "4CE0", func_8002B4A8);

INCLUDE_ASM(const s32, "4CE0", func_8002B954);

INCLUDE_ASM(const s32, "4CE0", func_8002B998);

INCLUDE_ASM(const s32, "4CE0", func_8002BE64);

INCLUDE_ASM(const s32, "4CE0", func_8002C27C);

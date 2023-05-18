import os
import subprocess
import ninja_syntax

dir_path = 'src/'
asm_path = 'asm/'
assets_path = 'assets/'

if os.name == 'nt':
    DETECTED_OS = 'windows'
else:
    uname = os.uname()
    if uname[0] == 'Linux':
        DETECTED_OS = 'linux'
    elif uname[0] == 'Darwin':
        DETECTED_OS = 'macos'
        MAKE = 'gmake'
        CPPFLAGS += '-xc++'

with open('build.ninja', 'w') as f:
    f.write(f'DETECTED_OS = {DETECTED_OS}\n')

header = (
    "BUILD_PATH = build\n"
    'CC = tools/gcc_2.7.2/$DETECTED_OS/gcc\n'
    'CC_HOST = gcc\n'
    'CPP = cpp -P\n'
    'ROM = $BUILD_PATH/shadowgate64.z64\n'
    'ELF = $BUILD_PATH/shadowgate64.elf\n'
    'LD_SCRIPT = shadowgate64.ld\n'
    'LD_MAP = $BUILD_PATH/shadowgate64.map\n'
    'ASFLAGS = -G 0 -I include -mips3 -mabi=32\n'
    'CFLAGS = -G0 -mips3 -mgp32 -mfp32 -Wa,--vr4300mul-off -D_LANGUAGE_C\n'
    'CPPFLAGS = -I. -I include -I build/include -I src -DF3DEX_GBI_2 -DNDEBUG\n'
    'LDFLAGS = -T undefined_syms.txt -T undefined_funcs.txt -T undefined_funcs_auto.txt -T undefined_syms_auto.txt -T $LD_SCRIPT -Map $LD_MAP --no-check-sections\n'
    'CHECK_WARNINGS = -Wall -Wextra -Wunused-but-set-variable -Wno-format-security -Wno-unused-parameter -Wno-sign-compare -Wno-unused-variable -Wno-pointer-to-int-cast -Wno-int-to-pointer-cast -m32\n'
    'CFLAGS_CHECK = -fsyntax-only -fsigned-char -nostdinc -fno-builtin -D CC_CHECK -D _LANGUAGE_C -std=gnu90 $CHECK_WARNINGS\n'
    'AS = mips-linux-gnu-as\n'
    'LD = mips-linux-gnu-ld\n'
    'OBJCOPY = mips-linux-gnu-objcopy\n'
    'STRIP = mips-linux-gnu-strip\n'
    'OPTFLAGS = -O1 -g2\n'
    'MAKE_EXPECTED = tools/make_expected.py\n'
    '\n'

    'rule main_cc\n'
    '  command = (export COMPILER_PATH=tools/gcc_2.7.2/$DETECTED_OS && $CC $OPTFLAGS $CFLAGS $CPPFLAGS -c -o $out $in) && ($STRIP $out -N dummy-symbol-name)\n'
    '\n'

    'rule s_file\n'
    '  command = $AS $ASFLAGS -o $out $in\n'
    '\n'

    "rule bin_file\n"
    "  command = $LD -r -b binary -o $out $in\n"
    "\n"

    "rule make_elf\n"
    "  command = $LD $LDFLAGS -o $out\n"
    "\n"

    "rule make_rom_bin\n"
    "  command = $OBJCOPY -O binary $in $out\n"
    "\n"

    "rule make_rom_z64\n"
    "  command = (cp $in $out) && (sha1sum -c shadowgate64.sha1)\n"
    "\n"

    "rule make_expected_folder\n"
    "  command = (cp $in $out) && (python3 ./$MAKE_EXPECTED $in)\n"
    "\n"

)

# Traverse each subdirectory recursively and find all C files
def append_extension(filename):
    return filename + '.o'

c_files = []
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.c'):
            c_files.append(os.path.join(root, file))

s_files = []
for root, dirs, files in os.walk(asm_path):
    for file in files:
        if file.endswith('.s'):
            s_files.append(os.path.join(root, file))

bin_files = []
for root, dirs, files in os.walk(assets_path):
    for file in files:
        if file.endswith('.bin'):
            bin_files.append(os.path.join(root, file))

# Combine the lists and change file extensions
o_files = []
for file in c_files + s_files + bin_files:
    if 'src/mod/' not in file and not file.startswith('src/mod/'):
        if 'asm/nonmatchings/' not in file:
            o_files.append("build/" + append_extension(file))

with open('build.ninja', 'a') as f:
    f.write(header)

ninja_file = ninja_syntax.Writer(open('build.ninja', 'a'))

# Write the full path of each C file to a new text file called build.ninja
for c_file in c_files:
    ninja_file.build("build/" + append_extension(c_file), "main_cc", c_file)
for s_file in s_files:
    ninja_file.build("build/" + append_extension(s_file), "s_file", s_file)
for bin_file in bin_files:
    ninja_file.build("build/" + append_extension(bin_file), "bin_file", bin_file)

# Build the ninja rule with the .o files
ninja_file.build("build/shadowgate64.elf", "make_elf ", o_files)
ninja_file.build("build/shadowgate64.bin", "make_rom_bin", "build/shadowgate64.elf\n")
ninja_file.build("build/shadowgate64.z64", "make_rom_z64", "build/shadowgate64.bin")
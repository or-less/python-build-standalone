# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

DOWNLOADS = {
    "autoconf": {
        "url": "https://ftp.gnu.org/gnu/autoconf/autoconf-2.71.tar.gz",
        "size": 2003781,
        "sha256": "431075ad0bf529ef13cb41e9042c542381103e80015686222b8a9d4abef42a1c",
        "version": "2.71",
    },
    # 6.0.19 is the last version licensed under the Sleepycat license.
    "bdb": {
        "url": "https://ftp.osuosl.org/pub/blfs/conglomeration/db/db-6.0.19.tar.gz",
        "size": 36541923,
        "sha256": "2917c28f60903908c2ca4587ded1363b812c4e830a5326aaa77c9879d13ae18e",
        "version": "6.0.19",
        "library_names": ["db"],
        "licenses": ["Sleepycat"],
        "license_file": "LICENSE.bdb.txt",
    },
    "binutils": {
        "url": "https://ftp.gnu.org/gnu/binutils/binutils-2.42.tar.xz",
        "size": 27567160,
        "sha256": "f6e4d41fd5fc778b06b7891457b3620da5ecea1006c6a4a41ae998109f85a800",
        "version": "2.42",
    },
    "bzip2": {
        "url": "https://sourceware.org/pub/bzip2/bzip2-1.0.8.tar.gz",
        "size": 810029,
        "sha256": "ab5a03176ee106d3f0fa90e381da478ddae405918153cca248e682cd0c4a2269",
        "version": "1.0.8",
        "library_names": ["bz2"],
        "licenses": ["bzip2-1.0.6"],
        "license_file": "LICENSE.bzip2.txt",
    },
    "cpython-3.8": {
        "url": "https://www.python.org/ftp/python/3.8.20/Python-3.8.20.tar.xz",
        "size": 18962788,
        "sha256": "6fb89a7124201c61125c0ab4cf7f6894df339a40c02833bfd28ab4d7691fafb4",
        "version": "3.8.20",
        "licenses": ["Python-2.0", "CNRI-Python"],
        "license_file": "LICENSE.cpython.txt",
        "python_tag": "cp38",
    },
    "cpython-3.9": {
        "url": "https://www.python.org/ftp/python/3.9.20/Python-3.9.20.tar.xz",
        "size": 19648968,
        "sha256": "6b281279efd85294d2d6993e173983a57464c0133956fbbb5536ec9646beaf0c",
        "version": "3.9.20",
        "licenses": ["Python-2.0", "CNRI-Python"],
        "license_file": "LICENSE.cpython.txt",
        "python_tag": "cp39",
    },
    "cpython-3.10": {
        "url": "https://www.python.org/ftp/python/3.10.15/Python-3.10.15.tar.xz",
        "size": 19596540,
        "sha256": "aab0950817735172601879872d937c1e4928a57c409ae02369ec3d91dccebe79",
        "version": "3.10.15",
        "licenses": ["Python-2.0", "CNRI-Python"],
        "license_file": "LICENSE.cpython.txt",
        "python_tag": "cp310",
    },
    "cpython-3.11": {
        "url": "https://www.python.org/ftp/python/3.11.10/Python-3.11.10.tar.xz",
        "size": 20067656,
        "sha256": "07a4356e912900e61a15cb0949a06c4a05012e213ecd6b4e84d0f67aabbee372",
        "version": "3.11.10",
        "licenses": ["Python-2.0", "CNRI-Python"],
        "license_file": "LICENSE.cpython.txt",
        "python_tag": "cp311",
    },
    "cpython-3.12": {
        "url": "https://www.python.org/ftp/python/3.12.7/Python-3.12.7.tar.xz",
        "size": 20444032,
        "sha256": "24887b92e2afd4a2ac602419ad4b596372f67ac9b077190f459aba390faf5550",
        "version": "3.12.7",
        "licenses": ["Python-2.0", "CNRI-Python"],
        "license_file": "LICENSE.cpython.txt",
        "python_tag": "cp312",
    },
    "cpython-3.13": {
        "url": "https://www.python.org/ftp/python/3.13.0/Python-3.13.0.tar.xz",
        "size": 22532980,
        "sha256": "086de5882e3cb310d4dca48457522e2e48018ecd43da9cdf827f6a0759efb07d",
        "version": "3.13.0",
        "licenses": ["Python-2.0", "CNRI-Python"],
        "license_file": "LICENSE.cpython.txt",
        "python_tag": "cp313",
    },
    "expat": {
        "url": "https://github.com/libexpat/libexpat/releases/download/R_2_5_0/expat-2.5.0.tar.xz",
        "size": 460560,
        "sha256": "ef2420f0232c087801abf705e89ae65f6257df6b7931d37846a193ef2e8cdcbe",
        "version": "2.5.0",
        "library_names": ["expat"],
        "licenses": ["MIT"],
        "license_file": "LICENSE.expat.txt",
    },
    "inputproto": {
        "url": "https://www.x.org/archive/individual/proto/inputproto-2.3.2.tar.gz",
        "size": 244334,
        "sha256": "10eaadd531f38f7c92ab59ef0708ca195caf3164a75c4ed99f0c04f2913f6ef3",
        "version": "2.3.2",
    },
    "jom-windows-bin": {
        "url": "http://download.qt.io/official_releases/jom/jom_1_1_3.zip",
        "size": 1213852,
        "sha256": "128fdd846fe24f8594eed37d1d8929a0ea78df563537c0c1b1861a635013fff8",
        "version": "1.1.3",
    },
    "kbproto": {
        "url": "https://www.x.org/archive/individual/proto/kbproto-1.0.7.tar.gz",
        "size": 325858,
        "sha256": "828cb275b91268b1a3ea950d5c0c5eb076c678fdf005d517411f89cc8c3bb416",
        "version": "1.0.7",
    },
    # 20221009-3.1 fails to build on musl due to an includes issue.
    "libedit": {
        "url": "https://thrysoee.dk/editline/libedit-20210910-3.1.tar.gz",
        "size": 524722,
        "sha256": "6792a6a992050762edcca28ff3318cdb7de37dccf7bc30db59fcd7017eed13c5",
        "version": "20210910-3.1",
        "library_names": ["edit"],
        "licenses": ["BSD-3-Clause"],
        "license_file": "LICENSE.libedit.txt",
    },
    "libffi-3.3": {
        "url": "https://github.com/libffi/libffi/releases/download/v3.3/libffi-3.3.tar.gz",
        "size": 1305466,
        "sha256": "72fba7922703ddfa7a028d513ac15a85c8d54c8d67f55fa5a4802885dc652056",
        "version": "3.3",
        "library_names": ["ffi"],
        "licenses": ["MIT"],
        "license_file": "LICENSE.libffi.txt",
    },
    "libffi": {
        "url": "https://github.com/libffi/libffi/releases/download/v3.4.6/libffi-3.4.6.tar.gz",
        "size": 1391684,
        "sha256": "b0dea9df23c863a7a50e825440f3ebffabd65df1497108e5d437747843895a4e",
        "version": "3.4.6",
        "library_names": ["ffi"],
        "licenses": ["MIT"],
        "license_file": "LICENSE.libffi.txt",
    },
    "libpthread-stubs": {
        "url": "https://www.x.org/archive/individual/lib/libpthread-stubs-0.5.tar.gz",
        "size": 74938,
        "sha256": "593196cc746173d1e25cb54a93a87fd749952df68699aab7e02c085530e87747",
        "version": "0.5",
    },
    "libX11": {
        "url": "https://www.x.org/archive/individual/lib/libX11-1.6.12.tar.gz",
        "size": 3168158,
        "sha256": "0fce5fc0a24a3dc728174eccd0cb8d6a1b37a2ec1654bd5628c84e5bc200d594",
        "version": "1.6.12",
        "library_names": ["X11", "X11-xcb"],
        "licenses": ["MIT", "X11"],
        "license_file": "LICENSE.libX11.txt",
    },
    "libXau": {
        "url": "https://www.x.org/releases/individual/lib/libXau-1.0.11.tar.gz",
        "size": 404973,
        "sha256": "3a321aaceb803577a4776a5efe78836eb095a9e44bbc7a465d29463e1a14f189",
        "version": "1.0.11",
        "library_names": ["Xau"],
        "licenses": ["MIT"],
        "license_file": "LICENSE.libXau.txt",
    },
    # Newer versions of libxcb require a modern Python to build. We can take this
    # dependency once we feel like doing the work.
    "libxcb": {
        "url": "https://xcb.freedesktop.org/dist/libxcb-1.14.tar.gz",
        "size": 640322,
        "sha256": "2c7fcddd1da34d9b238c9caeda20d3bd7486456fc50b3cc6567185dbd5b0ad02",
        "version": "1.14",
        "library_names": ["xcb"],
        "licenses": ["MIT"],
        "license_file": "LICENSE.libxcb.txt",
    },
    "llvm-14-x86_64-linux": {
        "url": "https://github.com/indygreg/toolchain-tools/releases/download/toolchain-bootstrap%2F20220508/llvm-14.0.3+20220508-gnu_only-x86_64-unknown-linux-gnu.tar.zst",
        "size": 158614671,
        "sha256": "04cb77c660f09df017a57738ae9635ef23a506024789f2f18da1304b45af2023",
        "version": "14.0.3+20220508",
    },
    # Remember to update LLVM_URL in src/release.rs whenever upgrading.
    "llvm-18-x86_64-linux": {
        "url": "https://github.com/indygreg/toolchain-tools/releases/download/toolchain-bootstrap%2F20240713/llvm-18.0.8+20240713-gnu_only-x86_64-unknown-linux-gnu.tar.zst",
        "size": 242840506,
        "sha256": "080c233fc7d75031b187bbfef62a4f9abc01188effb0c68fbc7dc4bc7370ee5b",
        "version": "18.0.8+20240713",
    },
    # Remember to update LLVM_URL in src/release.rs whenever upgrading.
    "llvm-aarch64-macos": {
        "url": "https://github.com/indygreg/toolchain-tools/releases/download/toolchain-bootstrap%2F20240713/llvm-18.0.8+20240713-aarch64-apple-darwin.tar.zst",
        "size": 136598617,
        "sha256": "320da8d639186e020e7d54cdc35b7a5473b36cef08fdf7b22c03b59a273ba593",
        "version": "18.0.8+20240713",
    },
    # Remember to update LLVM_URL in src/release.rs whenever upgrading.
    "llvm-x86_64-macos": {
        "url": "https://github.com/indygreg/toolchain-tools/releases/download/toolchain-bootstrap%2F20240713/llvm-18.0.8+20240713-x86_64-apple-darwin.tar.zst",
        "size": 136599290,
        "sha256": "3032161d1cadb8996b07fe5762444c956842b5a7d798b2fcfe5a04574fdf7549",
        "version": "18.0.8+20240713",
    },
    "m4": {
        "url": "https://ftp.gnu.org/gnu/m4/m4-1.4.19.tar.xz",
        "size": 1654908,
        "sha256": "63aede5c6d33b6d9b13511cd0be2cac046f2e70fd0a07aa9573a04a82783af96",
        "version": "1.4.19",
    },
    "mpdecimal": {
        "url": "https://www.bytereef.org/software/mpdecimal/releases/mpdecimal-4.0.0.tar.gz",
        "size": 315325,
        "sha256": "942445c3245b22730fd41a67a7c5c231d11cb1b9936b9c0f76334fb7d0b4468c",
        "version": "4.0.0",
        "library_names": ["mpdec"],
        "licenses": ["BSD-2-Clause"],
        "license_file": "LICENSE.mpdecimal.txt",
    },
    "musl": {
        "url": "https://musl.libc.org/releases/musl-1.2.5.tar.gz",
        "size": 1080786,
        "sha256": "a9a118bbe84d8764da0ea0d28b3ab3fae8477fc7e4085d90102b8596fc7c75e4",
        "version": "1.2.5",
    },
    "ncurses": {
        "url": "https://ftp.gnu.org/pub/gnu/ncurses/ncurses-6.5.tar.gz",
        "size": 3688489,
        "sha256": "136d91bc269a9a5785e5f9e980bc76ab57428f604ce3e5a5a90cebc767971cc6",
        "version": "6.5",
        "library_names": ["ncurses", "ncursesw", "panel", "panelw"],
        "licenses": ["X11"],
        "license_file": "LICENSE.ncurses.txt",
    },
    # Remember to update OPENSSL_VERSION_INFO in verify_distribution.py whenever upgrading.
    "openssl-1.1": {
        "url": "https://www.openssl.org/source/openssl-1.1.1w.tar.gz",
        "size": 9893384,
        "sha256": "cf3098950cb4d853ad95c0841f1f9c6d3dc102dccfcacd521d93925208b76ac8",
        "version": "1.1.1w",
        "library_names": ["crypto", "ssl"],
        "licenses": ["OpenSSL"],
        "license_file": "LICENSE.openssl-1.1.txt",
    },
    # We use OpenSSL 3.0 because it is an LTS release and has a longer support
    # window. If CPython ends up gaining support for 3.1+ releases, we can consider
    # using the latest available.
    # Remember to update OPENSSL_VERSION_INFO in verify_distribution.py whenever upgrading.
    "openssl-3.0": {
        "url": "https://www.openssl.org/source/openssl-3.0.14.tar.gz",
        "size": 15305497,
        "sha256": "eeca035d4dd4e84fc25846d952da6297484afa0650a6f84c682e39df3a4123ca",
        "version": "3.0.14",
        "library_names": ["crypto", "ssl"],
        "licenses": ["Apache-2.0"],
        "license_file": "LICENSE.openssl-3.txt",
    },
    "nasm-windows-bin": {
        "url": "https://github.com/python/cpython-bin-deps/archive/nasm-2.11.06.tar.gz",
        "size": 384826,
        "sha256": "8af0ae5ceed63fa8a2ded611d44cc341027a91df22aaaa071efedc81437412a5",
        "version": "2.11.06",
    },
    "patchelf": {
        "url": "https://github.com/NixOS/patchelf/releases/download/0.13.1/patchelf-0.13.1.tar.bz2",
        "size": 173598,
        "sha256": "39e8aeccd7495d54df094d2b4a7c08010ff7777036faaf24f28e07777d1598e2",
        "version": "0.13.1",
    },
    "pip": {
        "url": "https://files.pythonhosted.org/packages/e7/54/0c1c068542cee73d8863336e974fc881e608d0170f3af15d0c0f28644531/pip-24.1.2-py3-none-any.whl",
        "size": 1824406,
        "sha256": "7cd207eed4c60b0f411b444cd1464198fe186671c323b6cd6d433ed80fc9d247",
        "version": "24.1.2",
    },
    "readline": {
        "url": "https://ftp.gnu.org/gnu/readline/readline-8.2.tar.gz",
        "size": 3043952,
        "sha256": "3feb7171f16a84ee82ca18a36d7b9be109a52c04f492a053331d7d1095007c35",
        "version": "8.2",
        "library_names": ["readline"],
        "licenses": ["GPL-3.0-only"],
        "license_file": "LICENSE.readline.txt",
    },
    "setuptools": {
        "url": "https://files.pythonhosted.org/packages/ef/15/88e46eb9387e905704b69849618e699dc2f54407d8953cc4ec4b8b46528d/setuptools-70.3.0-py3-none-any.whl",
        "size": 931070,
        "sha256": "fe384da74336c398e0d956d1cae0669bc02eed936cdb1d49b57de1990dc11ffc",
        "version": "70.3.0",
    },
    # Remember to update verify_distribution.py when version changed.
    "sqlite": {
        "url": "https://www.sqlite.org/2024/sqlite-autoconf-3460000.tar.gz",
        "size": 3265248,
        "sha256": "6f8e6a7b335273748816f9b3b62bbdc372a889de8782d7f048c653a447417a7d",
        "version": "3460000",
        "actual_version": "3.46.0.0",
        "library_names": ["sqlite3"],
        "licenses": [],
        "license_file": "LICENSE.sqlite.txt",
        "license_public_domain": True,
    },
    "strawberryperl": {
        "url": "http://strawberryperl.com/download/5.28.1.1/strawberry-perl-5.28.1.1-32bit-portable.zip",
        "size": 143242779,
        "sha256": "8b15c7c9574989568254a7859e473b7d5f68a1145d2e4418036600a81b13805c",
        "version": "5.28.1.1",
    },
    "tcl": {
        "url": "https://prdownloads.sourceforge.net/tcl/tcl8.6.12-src.tar.gz",
        "size": 10353486,
        "sha256": "26c995dd0f167e48b11961d891ee555f680c175f7173ff8cb829f4ebcde4c1a6",
        "version": "8.6.12",
        "library_names": ["tcl8.6"],
        "licenses": ["TCL"],
        "license_file": "LICENSE.tcl.txt",
    },
    "tix": {
        "url": "https://github.com/python/cpython-source-deps/archive/tix-8.4.3.6.tar.gz",
        "size": 1836451,
        "sha256": "f7b21d115867a41ae5fd7c635a4c234d3ca25126c3661eb36028c6e25601f85e",
        "version": "8.4.3.6",
        "licenses": ["TCL"],
        "license_file": "LICENSE.tix.txt",
    },
    "tk": {
        "url": "https://prdownloads.sourceforge.net/tcl/tk8.6.12-src.tar.gz",
        "size": 4515393,
        "sha256": "12395c1f3fcb6bed2938689f797ea3cdf41ed5cb6c4766eec8ac949560310630",
        "version": "8.6.12",
        "library_names": ["tk8.6"],
        "licenses": ["TCL"],
        "license_file": "LICENSE.tcl.txt",
    },
    "tk-windows-bin": {
        "url": "https://github.com/python/cpython-bin-deps/archive/e3c3e9a2856124aa32b608632a52742d479eb7a9.tar.gz",
        "size": 6787654,
        "sha256": "01ad9c663659224e075d487cbc33ea2fed7a225593965b79bed92ca7f79b676f",
        "version": "8.6.12",
        "git_commit": "e3c3e9a2856124aa32b608632a52742d479eb7a9",
    },
    "uuid": {
        "url": "https://sourceforge.net/projects/libuuid/files/libuuid-1.0.3.tar.gz",
        "size": 318256,
        "sha256": "46af3275291091009ad7f1b899de3d0cea0252737550e7919d17237997db5644",
        "version": "1.0.3",
        "library_names": ["uuid"],
        "licenses": ["BSD-3-Clause"],
        "license_file": "LICENSE.libuuid.txt",
    },
    "x11-util-macros": {
        "url": "https://www.x.org/archive/individual/util/util-macros-1.20.0.tar.gz",
        "size": 104931,
        "sha256": "8daf36913d551a90fd1013cb078401375dabae021cb4713b9b256a70f00eeb74",
        "version": "1.20.0",
    },
    "xcb-proto": {
        "url": "https://www.x.org/archive/individual/proto/xcb-proto-1.14.1.tar.gz",
        "size": 194674,
        "sha256": "85cd21e9d9fbc341d0dbf11eace98d55d7db89fda724b0e598855fcddf0944fd",
        "version": "1.14.1",
    },
    "xextproto": {
        "url": "https://www.x.org/archive/individual/proto/xextproto-7.3.0.tar.gz",
        "size": 290814,
        "sha256": "1b1bcdf91221e78c6c33738667a57bd9aaa63d5953174ad8ed9929296741c9f5",
        "version": "7.3.0",
    },
    # Newer versions from at least 2023 have build failures for reasons we haven't
    # fully investigated.
    "xorgproto": {
        "url": "https://www.x.org/archive/individual/proto/xorgproto-2019.1.tar.gz",
        "size": 1119813,
        "sha256": "38ad1d8316515785d53c5162b4b7022918e03c11d72a5bd9df0a176607f42bca",
        "version": "2019.1",
    },
    "xproto": {
        "url": "https://www.x.org/archive/individual/proto/xproto-7.0.31.tar.gz",
        "size": 367979,
        "sha256": "6d755eaae27b45c5cc75529a12855fed5de5969b367ed05003944cf901ed43c7",
        "version": "7.0.31",
    },
    "xtrans": {
        "url": "https://www.x.org/archive/individual/lib/xtrans-1.5.0.tar.gz",
        "size": 230197,
        "sha256": "a806f8a92f879dcd0146f3f1153fdffe845f2fc0df9b1a26c19312b7b0a29c86",
        "version": "1.5.0",
    },
    # IMPORTANT: xz 5.6 has a backdoor. Be extremely cautious before taking any xz
    # upgrade since it isn't clear which versions are safe.
    "xz": {
        "url": "https://github.com/indygreg/python-build-standalone/releases/download/20240224/xz-5.2.12.tar.gz",
        "size": 2190541,
        "sha256": "61bda930767dcb170a5328a895ec74cab0f5aac4558cdda561c83559db582a13",
        "version": "5.2.12",
        "library_names": ["lzma"],
        # liblzma is in the public domain. Other parts of code have licenses. But
        # we only use liblzma.
        "licenses": [],
        "license_file": "LICENSE.liblzma.txt",
        "license_public_domain": True,
    },
    "zlib": {
        "url": "https://github.com/madler/zlib/releases/download/v1.2.13/zlib-1.2.13.tar.gz",
        "size": 1497445,
        "sha256": "b3a24de97a8fdbc835b9833169501030b8977031bcb54b3b3ac13740f846ab30",
        "version": "1.2.13",
        "library_names": ["z"],
        "licenses": ["Zlib"],
        "license_file": "LICENSE.zlib.txt",
    },
}

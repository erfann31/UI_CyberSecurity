<div dir="rtl">
در ابتدا الفبای رمز که همان الفبای انگلیسی است و تعداد حروفش را مشخص کرده ایم
 تابع mod_inverse برای بدست آوردن باقی مانده a در ماد m است. <br>
تابع affine_encrypt برای رمز کردن پلین تکست با کلید(a, b) است و همچنین کارکتر هایی که داخل زبان نیستند را رمز نمی‌کند. <br>
تابع affine_decrypt برای رمز گشایی سایفر تکست با کلید(a, b) است و همچنین کارکتر هایی که داخل زبان نیستند را رمزگشایی نمی‌کند. <br>
تابع frequency_analysis برای بدست آوردن تعداد تکرار هر حرف در متن است. <br>
تابع statistical_attack برای حمله آماری به متن داده شده است که ابتدا بیشترین تکرار را پیدا کرده و سپس a وارون و b را پیش‌بینی می‌کند. <br>
در این برنامه 3 مرتبه برای حمله آماری تست می‌شود و هربار خروجی قسمت قبل به تابع داده می‌شود. <br>
تابع brute_force_attack برای حمله ی بروت فورس به متن است که لیستی از پلین تکست های ممکن را بر می‌گرداند. <br>
لازم به ذکر است که اگر طول متن سایفر کمتر از 16 کارکتر بود حمله ی انجام شده بورت فورس و در غیر این صورت حمله ی آماری است.<br>
نمونه ها:
</div>

```
Plain Text: ALGORITHMSAREQUITEGENERALDEFINITIONSOFARITHMETICPROCESSES
a: 3 , b: 5
Encrypted: FMXVEDKAPHFERBNDKRXRSREFMORUDSDKDVSHVUFEDKAPRKDLYEVLRHHRH

Statistical Attack 1:
a_inverse=9, b=7
Decrypted: UPWQROJFYAUREISOJEWEHERUPVENOHOJOQHAQNUROJFYEJOMZRQMEAAEA

Statistical Attack 2:
a_inverse=9, b=9
Decrypted: SZKIRQXNCUSREOAQXEKEFERSZBEHQFQXQIFUIHSRQXNCEXQYLRIYEUUEU

Statistical Attack 3:
a_inverse=9, b=11
Decrypted: ALGORITHMSAREQUITEGENERALDEFINITIONSOFARITHMETICPROCESSES
```

```
Plain Text: HELLOWORLD
a: 3 , b: 5
Encrypted: ARMMVTVEMO

Brute Force Attack:
a=1, b=0: ARMMVTVEMO
a=1, b=1: ZQLLUSUDLN
a=1, b=2: YPKKTRTCKM
a=1, b=3: XOJJSQSBJL
a=1, b=4: WNIIRPRAIK
a=1, b=5: VMHHQOQZHJ
a=1, b=6: ULGGPNPYGI
a=1, b=7: TKFFOMOXFH
a=1, b=8: SJEENLNWEG
a=1, b=9: RIDDMKMVDF
a=1, b=10: QHCCLJLUCE
a=1, b=11: PGBBKIKTBD
a=1, b=12: OFAAJHJSAC
a=1, b=13: NEZZIGIRZB
a=1, b=14: MDYYHFHQYA
a=1, b=15: LCXXGEGPXZ
a=1, b=16: KBWWFDFOWY
a=1, b=17: JAVVECENVX
a=1, b=18: IZUUDBDMUW
a=1, b=19: HYTTCACLTV
a=1, b=20: GXSSBZBKSU
a=1, b=21: FWRRAYAJRT
a=1, b=22: EVQQZXZIQS
a=1, b=23: DUPPYWYHPR
a=1, b=24: CTOOXVXGOQ
a=1, b=25: BSNNWUWFNP
a=3, b=0: AXEEHPHKEW
a=3, b=1: ROVVYGYBVN
a=3, b=2: IFMMPXPSME
a=3, b=3: ZWDDGOGJDV
a=3, b=4: QNUUXFXAUM
a=3, b=5: HELLOWORLD
a=3, b=6: YVCCFNFICU
a=3, b=7: PMTTWEWZTL
a=3, b=8: GDKKNVNQKC
a=3, b=9: XUBBEMEHBT
a=3, b=10: OLSSVDVYSK
a=3, b=11: FCJJMUMPJB
a=3, b=12: WTAADLDGAS
a=3, b=13: NKRRUCUXRJ
a=3, b=14: EBIILTLOIA
a=3, b=15: VSZZCKCFZR
a=3, b=16: MJQQTBTWQI
a=3, b=17: DAHHKSKNHZ
a=3, b=18: URYYBJBEYQ
a=3, b=19: LIPPSASVPH
a=3, b=20: CZGGJRJMGY
a=3, b=21: TQXXAIADXP
a=3, b=22: KHOORZRUOG
a=3, b=23: BYFFIQILFX
a=3, b=24: SPWWZHZCWO
a=3, b=25: JGNNQYQTNF
a=5, b=0: ATSSZJZGSI
a=5, b=1: FYXXEOELXN
a=5, b=2: KDCCJTJQCS
a=5, b=3: PIHHOYOVHX
a=5, b=4: UNMMTDTAMC
a=5, b=5: ZSRRYIYFRH
a=5, b=6: EXWWDNDKWM
a=5, b=7: JCBBISIPBR
a=5, b=8: OHGGNXNUGW
a=5, b=9: TMLLSCSZLB
a=5, b=10: YRQQXHXEQG
a=5, b=11: DWVVCMCJVL
a=5, b=12: IBAAHRHOAQ
a=5, b=13: NGFFMWMTFV
a=5, b=14: SLKKRBRYKA
a=5, b=15: XQPPWGWDPF
a=5, b=16: CVUUBLBIUK
a=5, b=17: HAZZGQGNZP
a=5, b=18: MFEELVLSEU
a=5, b=19: RKJJQAQXJZ
a=5, b=20: WPOOVFVCOE
a=5, b=21: BUTTAKAHTJ
a=5, b=22: GZYYFPFMYO
a=5, b=23: LEDDKUKRDT
a=5, b=24: QJIIPZPWIY
a=5, b=25: VONNUEUBND
a=7, b=0: AVYYDZDIYC
a=7, b=1: LGJJOKOTJN
a=7, b=2: WRUUZVZEUY
a=7, b=3: HCFFKGKPFJ
a=7, b=4: SNQQVRVAQU
a=7, b=5: DYBBGCGLBF
a=7, b=6: OJMMRNRWMQ
a=7, b=7: ZUXXCYCHXB
a=7, b=8: KFIINJNSIM
a=7, b=9: VQTTYUYDTX
a=7, b=10: GBEEJFJOEI
a=7, b=11: RMPPUQUZPT
a=7, b=12: CXAAFBFKAE
a=7, b=13: NILLQMQVLP
a=7, b=14: YTWWBXBGWA
a=7, b=15: JEHHMIMRHL
a=7, b=16: UPSSXTXCSW
a=7, b=17: FADDIEINDH
a=7, b=18: QLOOTPTYOS
a=7, b=19: BWZZEAEJZD
a=7, b=20: MHKKPLPUKO
a=7, b=21: XSVVAWAFVZ
a=7, b=22: IDGGLHLQGK
a=7, b=23: TORRWSWBRV
a=7, b=24: EZCCHDHMCG
a=7, b=25: PKNNSOSXNR
a=9, b=0: AZKKLFLMKQ
a=9, b=1: XWHHICIJHN
a=9, b=2: UTEEFZFGEK
a=9, b=3: RQBBCWCDBH
a=9, b=4: ONYYZTZAYE
a=9, b=5: LKVVWQWXVB
a=9, b=6: IHSSTNTUSY
a=9, b=7: FEPPQKQRPV
a=9, b=8: CBMMNHNOMS
a=9, b=9: ZYJJKEKLJP
a=9, b=10: WVGGHBHIGM
a=9, b=11: TSDDEYEFDJ
a=9, b=12: QPAABVBCAG
a=9, b=13: NMXXYSYZXD
a=9, b=14: KJUUVPVWUA
a=9, b=15: HGRRSMSTRX
a=9, b=16: EDOOPJPQOU
a=9, b=17: BALLMGMNLR
a=9, b=18: YXIIJDJKIO
a=9, b=19: VUFFGAGHFL
a=9, b=20: SRCCDXDECI
a=9, b=21: POZZAUABZF
a=9, b=22: MLWWXRXYWC
a=9, b=23: JITTUOUVTZ
a=9, b=24: GFQQRLRSQW
a=9, b=25: DCNNOIOPNT
a=11, b=0: ALUUJXJYUG
a=11, b=1: HSBBQEQFBN
a=11, b=2: OZIIXLXMIU
a=11, b=3: VGPPESETPB
a=11, b=4: CNWWLZLAWI
a=11, b=5: JUDDSGSHDP
a=11, b=6: QBKKZNZOKW
a=11, b=7: XIRRGUGVRD
a=11, b=8: EPYYNBNCYK
a=11, b=9: LWFFUIUJFR
a=11, b=10: SDMMBPBQMY
a=11, b=11: ZKTTIWIXTF
a=11, b=12: GRAAPDPEAM
a=11, b=13: NYHHWKWLHT
a=11, b=14: UFOODRDSOA
a=11, b=15: BMVVKYKZVH
a=11, b=16: ITCCRFRGCO
a=11, b=17: PAJJYMYNJV
a=11, b=18: WHQQFTFUQC
a=11, b=19: DOXXMAMBXJ
a=11, b=20: KVEETHTIEQ
a=11, b=21: RCLLAOAPLX
a=11, b=22: YJSSHVHWSE
a=11, b=23: FQZZOCODZL
a=11, b=24: MXGGVJVKGS
a=11, b=25: TENNCQCRNZ
a=15, b=0: APGGRDRCGU
a=15, b=1: TIZZKWKVZN
a=15, b=2: MBSSDPDOSG
a=15, b=3: FULLWIWHLZ
a=15, b=4: YNEEPBPAES
a=15, b=5: RGXXIUITXL
a=15, b=6: KZQQBNBMQE
a=15, b=7: DSJJUGUFJX
a=15, b=8: WLCCNZNYCQ
a=15, b=9: PEVVGSGRVJ
a=15, b=10: IXOOZLZKOC
a=15, b=11: BQHHSESDHV
a=15, b=12: UJAALXLWAO
a=15, b=13: NCTTEQEPTH
a=15, b=14: GVMMXJXIMA
a=15, b=15: ZOFFQCQBFT
a=15, b=16: SHYYJVJUYM
a=15, b=17: LARRCOCNRF
a=15, b=18: ETKKVHVGKY
a=15, b=19: XMDDOAOZDR
a=15, b=20: QFWWHTHSWK
a=15, b=21: JYPPAMALPD
a=15, b=22: CRIITFTEIW
a=15, b=23: VKBBMYMXBP
a=15, b=24: ODUUFRFQUI
a=15, b=25: HWNNYKYJNB
a=17, b=0: ABQQPVPOQK
a=17, b=1: DETTSYSRTN
a=17, b=2: GHWWVBVUWQ
a=17, b=3: JKZZYEYXZT
a=17, b=4: MNCCBHBACW
a=17, b=5: PQFFEKEDFZ
a=17, b=6: STIIHNHGIC
a=17, b=7: VWLLKQKJLF
a=17, b=8: YZOONTNMOI
a=17, b=9: BCRRQWQPRL
a=17, b=10: EFUUTZTSUO
a=17, b=11: HIXXWCWVXR
a=17, b=12: KLAAZFZYAU
a=17, b=13: NODDCICBDX
a=17, b=14: QRGGFLFEGA
a=17, b=15: TUJJIOIHJD
a=17, b=16: WXMMLRLKMG
a=17, b=17: ZAPPOUONPJ
a=17, b=18: CDSSRXRQSM
a=17, b=19: FGVVUAUTVP
a=17, b=20: IJYYXDXWYS
a=17, b=21: LMBBAGAZBV
a=17, b=22: OPEEDJDCEY
a=17, b=23: RSHHGMGFHB
a=17, b=24: UVKKJPJIKE
a=17, b=25: XYNNMSMLNH
a=19, b=0: AFCCXBXSCY
a=19, b=1: PURRMQMHRN
a=19, b=2: EJGGBFBWGC
a=19, b=3: TYVVQUQLVR
a=19, b=4: INKKFJFAKG
a=19, b=5: XCZZUYUPZV
a=19, b=6: MROOJNJEOK
a=19, b=7: BGDDYCYTDZ
a=19, b=8: QVSSNRNISO
a=19, b=9: FKHHCGCXHD
a=19, b=10: UZWWRVRMWS
a=19, b=11: JOLLGKGBLH
a=19, b=12: YDAAVZVQAW
a=19, b=13: NSPPKOKFPL
a=19, b=14: CHEEZDZUEA
a=19, b=15: RWTTOSOJTP
a=19, b=16: GLIIDHDYIE
a=19, b=17: VAXXSWSNXT
a=19, b=18: KPMMHLHCMI
a=19, b=19: ZEBBWAWRBX
a=19, b=20: OTQQLPLGQM
a=19, b=21: DIFFAEAVFB
a=19, b=22: SXUUPTPKUQ
a=19, b=23: HMJJEIEZJF
a=19, b=24: WBYYTXTOYU
a=19, b=25: LQNNIMIDNJ
a=21, b=0: AHIIBRBUIS
a=21, b=1: VCDDWMWPDN
a=21, b=2: QXYYRHRKYI
a=21, b=3: LSTTMCMFTD
a=21, b=4: GNOOHXHAOY
a=21, b=5: BIJJCSCVJT
a=21, b=6: WDEEXNXQEO
a=21, b=7: RYZZSISLZJ
a=21, b=8: MTUUNDNGUE
a=21, b=9: HOPPIYIBPZ
a=21, b=10: CJKKDTDWKU
a=21, b=11: XEFFYOYRFP
a=21, b=12: SZAATJTMAK
a=21, b=13: NUVVOEOHVF
a=21, b=14: IPQQJZJCQA
a=21, b=15: DKLLEUEXLV
a=21, b=16: YFGGZPZSGQ
a=21, b=17: TABBUKUNBL
a=21, b=18: OVWWPFPIWG
a=21, b=19: JQRRKAKDRB
a=21, b=20: ELMMFVFYMW
a=21, b=21: ZGHHAQATHR
a=21, b=22: UBCCVLVOCM
a=21, b=23: PWXXQGQJXH
a=21, b=24: KRSSLBLESC
a=21, b=25: FMNNGWGZNX
a=23, b=0: ADWWTLTQWE
a=23, b=1: JMFFCUCZFN
a=23, b=2: SVOOLDLIOW
a=23, b=3: BEXXUMURXF
a=23, b=4: KNGGDVDAGO
a=23, b=5: TWPPMEMJPX
a=23, b=6: CFYYVNVSYG
a=23, b=7: LOHHEWEBHP
a=23, b=8: UXQQNFNKQY
a=23, b=9: DGZZWOWTZH
a=23, b=10: MPIIFXFCIQ
a=23, b=11: VYRROGOLRZ
a=23, b=12: EHAAXPXUAI
a=23, b=13: NQJJGYGDJR
a=23, b=14: WZSSPHPMSA
a=23, b=15: FIBBYQYVBJ
a=23, b=16: ORKKHZHEKS
a=23, b=17: XATTQIQNTB
a=23, b=18: GJCCZRZWCK
a=23, b=19: PSLLIAIFLT
a=23, b=20: YBUURJROUC
a=23, b=21: HKDDASAXDL
a=23, b=22: QTMMJBJGMU
a=23, b=23: ZCVVSKSPVD
a=23, b=24: ILEEBTBYEM
a=23, b=25: RUNNKCKHNV
a=25, b=0: AJOOFHFWOM
a=25, b=1: BKPPGIGXPN
a=25, b=2: CLQQHJHYQO
a=25, b=3: DMRRIKIZRP
a=25, b=4: ENSSJLJASQ
a=25, b=5: FOTTKMKBTR
a=25, b=6: GPUULNLCUS
a=25, b=7: HQVVMOMDVT
a=25, b=8: IRWWNPNEWU
a=25, b=9: JSXXOQOFXV
a=25, b=10: KTYYPRPGYW
a=25, b=11: LUZZQSQHZX
a=25, b=12: MVAARTRIAY
a=25, b=13: NWBBSUSJBZ
a=25, b=14: OXCCTVTKCA
a=25, b=15: PYDDUWULDB
a=25, b=16: QZEEVXVMEC
a=25, b=17: RAFFWYWNFD
a=25, b=18: SBGGXZXOGE
a=25, b=19: TCHHYAYPHF
a=25, b=20: UDIIZBZQIG
a=25, b=21: VEJJACARJH
a=25, b=22: WFKKBDBSKI
a=25, b=23: XGLLCECTLJ
a=25, b=24: YHMMDFDUMK
a=25, b=25: ZINNEGEVNL
```
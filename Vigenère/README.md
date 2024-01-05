<div dir="rtl">
<h2>توضیحات توابع:</h2>
<h3>vigenere_encrypt(plaintext, key)</h3>
این تابع با استفاده از کلید ارائه شده، رمزگذاری Vigenère را بر روی plaintext  داده شده انجام می دهد. از طریق هر کاراکتر plaintext  تکرار می شود، کاراکتر را بر اساس کاراکتر مربوطه در کلید تغییر می دهد و متن رمزگذاری شده را ایجاد می کند.
<h3>vigenere_decrypt(ciphertext, key)</h3>
این تابع رمزگشایی Vigenère را بر روی متن رمز داده شده با استفاده از کلید ارائه شده انجام می دهد. مشابه رمزگذاری، از طریق هر کاراکتر متن رمزی تکرار می‌شود، فرآیند تغییر را بر اساس کاراکتر مربوطه در کلید معکوس می‌کند و متن رمزگشایی شده را ایجاد می‌کند.
<h3>frequency_analysis(ciphertext)</h3>
تابع frequency_analysis فرکانس هر حرف در متن رمز را محاسبه می کند و فرکانس ها را به ترتیب نزولی مرتب می کند. این تجزیه و تحلیل می تواند به شناسایی حروف رایج در متن رمزی کمک کند، که می تواند با حروف رایج در متن ساده مطابقت داشته باشد و نکاتی برای شکستن رمزگذاری ارائه می دهد.
<h3>kasiski_examination(ciphertext, key_length)</h3>
تابع 'kasiski_examination' روشی است که در تحلیل رمز برای تعیین طول احتمالی کلید مورد استفاده در رمزگذاری رمزنگاری ویژنر استفاده می‌شود. به دنبال دنباله‌های مکرر نویسه‌ها در متن رمز می‌گردد که ممکن است با دنباله‌های تکراری ناشی از استفاده مجدد کلید برای رمزگذاری قسمت‌های مختلف متن ساده مطابقت داشته باشد.

- **روش**:
     1. این تابع یک دیکشنری خالی به نام 'repeated_sequences' را راه اندازی می کند تا دنباله هایی از کاراکترهای موجود در متن رمز را ذخیره کند که حداقل یک بار تکرار شده اند.
    
     2. سپس از طریق متن رمزی تکرار می‌شود و دنباله‌های طول «key_length» را بررسی می‌کند. برای هر دنباله یافت شده، بررسی می‌کند که آیا از قبل در دیکشنری «repeated_sequences» وجود دارد یا خیر. اگر بود، موقعیت فعلی را که دنباله پیدا می شود اضافه می کند. اگر نه، دنباله را به عنوان ورودی جدید با موقعیت اضافه می کند.
    
     3. پس از اسکن در متن رمزگذاری شده، تابع دنباله هایی را که فقط یک بار ظاهر می شوند فیلتر می کند زیرا الگوهای تکراری را نشان نمی دهند.

     4. در مرحله بعد، فواصل بین موقعیت هایی که هر دنباله تکرار می شود را محاسبه می کند. این فواصل را در دیکشنری «distances» ذخیره می‌کند و هر فاصله را با دنباله‌های تکراری مربوطه مرتبط می‌کند که این فاصله بین وقوعشان وجود دارد.

- **خروجی**:
     - تابع یک دیکشنری ("distances") را برمی گرداند که در آن کلیدها فواصل بین دنباله های تکرار شده هستند و مقادیر لیستی از دنباله های تکراری هستند که در آن فواصل در متن رمزی رخ می دهند.
<h3>known_plaintext_attack(plaintext, ciphertext)</h3>
این تابع سعی می کند کلید مورد استفاده برای رمزگذاری را با مقایسه plaintext  شناخته شده با بخش مربوطه از ciphertext  استنتاج کند. این کاراکترهای کلیدی احتمالی را با یافتن تفاوت بین کاراکترهای plaintext  و ciphertext  محاسبه می کند.
<h3>brute_force_attack(ciphertext)</h3>
تابع brute_force_attack با آزمایش تمام کلیدهای ممکن با طول های مختلف در برابر متن رمز، یک حمله brute-force را انجام می دهد. در طول کلیدهای مختلف تکرار می شود و کلیدهای ممکن را برای رمزگشایی متن رمز با استفاده از رمزگشایی Vigenère ایجاد می کند. در نتیجه کلیدهای ممکن و متون رمزگشایی شده مربوط به آنها را پرینت می کند.
<h2>تست توابع و خروجی<h2>
</div>

```
Plain Text: CRYPTOISSHORTFORCRYPTOGRAPHY
Encrypted Text: MVWZXMSWQRSPDJMBGPITRYKPKTFI
Decrypted Text: CRYPTOISSHORTFORCRYPTOGRAPHY

Frequency Analysis Result:
[('M', 3), ('P', 3), ('W', 2), ('S', 2), ('R', 2), ('I', 2), ('T', 2), ('K', 2), ('V', 1), ('Z', 1), ('X', 1), ('Q', 1), ('D', 1), ('J', 1), ('B', 1), ('G', 1), ('Y', 1), ('F', 1)]

Kasiski Examination Result:
{}

Known Plaintext Attack Result:
Probable key:  KEYKEYKEYKEYKEYKEYKEYKEYKEYK

do you want to brute force attack be done? (y , n): y
Brute-force Attack Result:
Key: MSR, Decrypted Text: ADFNFVGEZFAYRRVPOYWBAMSYYBOW
Key: LRQ, Decrypted Text: BEGOGWHFAGBZSSWQPZXCBNTZZCPX
Key: KQP, Decrypted Text: CFHPHXIGBHCATTXRQAYDCOUAADQY
Key: JPO, Decrypted Text: DGIQIYJHCIDBUUYSRBZEDPVBBERZ
Key: ION, Decrypted Text: EHJRJZKIDJECVVZTSCAFEQWCCFSA
Key: HNM, Decrypted Text: FIKSKALJEKFDWWAUTDBGFRXDDGTB
Key: GML, Decrypted Text: GJLTLBMKFLGEXXBVUECHGSYEEHUC
Key: FLK, Decrypted Text: HKMUMCNLGMHFYYCWVFDIHTZFFIVD
Key: EKJ, Decrypted Text: ILNVNDOMHNIGZZDXWGEJIUAGGJWE
Key: DJI, Decrypted Text: JMOWOEPNIOJHAAEYXHFKJVBHHKXF
Key: CIH, Decrypted Text: KNPXPFQOJPKIBBFZYIGLKWCIILYG
Key: BHG, Decrypted Text: LOQYQGRPKQLJCCGAZJHMLXDJJMZH
Key: AGF, Decrypted Text: MPRZRHSQLRMKDDHBAKINMYEKKNAI
Key: ZFE, Decrypted Text: NQSASITRMSNLEEICBLJONZFLLOBJ
Key: YED, Decrypted Text: ORTBTJUSNTOMFFJDCMKPOAGMMPCK
Key: XDC, Decrypted Text: PSUCUKVTOUPNGGKEDNLQPBHNNQDL
Key: WCB, Decrypted Text: QTVDVLWUPVQOHHLFEOMRQCIOOREM
Key: VBA, Decrypted Text: RUWEWMXVQWRPIIMGFPNSRDJPPSFN
Key: UAZ, Decrypted Text: SVXFXNYWRXSQJJNHGQOTSEKQQTGO
Key: TZY, Decrypted Text: TWYGYOZXSYTRKKOIHRPUTFLRRUHP
Key: SYX, Decrypted Text: UXZHZPAYTZUSLLPJISQVUGMSSVIQ
Key: RXW, Decrypted Text: VYAIAQBZUAVTMMQKJTRWVHNTTWJR
Key: QWV, Decrypted Text: WZBJBRCAVBWUNNRLKUSXWIOUUXKS
Key: PVU, Decrypted Text: XACKCSDBWCXVOOSMLVTYXJPVVYLT
Key: OUT, Decrypted Text: YBDLDTECXDYWPPTNMWUZYKQWWZMU
Key: NTS, Decrypted Text: ZCEMEUFDYEZXQQUONXVAZLRXXANV
Key: MPK, Decrypted Text: AGMNICGHGFDFRUCPRFWEHMVFYEVW
Key: LOJ, Decrypted Text: BHNOJDHIHGEGSVDQSGXFINWGZFWX
Key: KNI, Decrypted Text: CIOPKEIJIHFHTWERTHYGJOXHAGXY
Key: JMH, Decrypted Text: DJPQLFJKJIGIUXFSUIZHKPYIBHYZ
Key: ILG, Decrypted Text: EKQRMGKLKJHJVYGTVJAILQZJCIZA
Key: HKF, Decrypted Text: FLRSNHLMLKIKWZHUWKBJMRAKDJAB
Key: GJE, Decrypted Text: GMSTOIMNMLJLXAIVXLCKNSBLEKBC
Key: FID, Decrypted Text: HNTUPJNONMKMYBJWYMDLOTCMFLCD
Key: EHC, Decrypted Text: IOUVQKOPONLNZCKXZNEMPUDNGMDE
Key: DGB, Decrypted Text: JPVWRLPQPOMOADLYAOFNQVEOHNEF
Key: CFA, Decrypted Text: KQWXSMQRQPNPBEMZBPGORWFPIOFG
Key: BEZ, Decrypted Text: LRXYTNRSRQOQCFNACQHPSXGQJPGH
Key: ADY, Decrypted Text: MSYZUOSTSRPRDGOBDRIQTYHRKQHI
Key: ZCX, Decrypted Text: NTZAVPTUTSQSEHPCESJRUZISLRIJ
Key: YBW, Decrypted Text: OUABWQUVUTRTFIQDFTKSVAJTMSJK
Key: XAV, Decrypted Text: PVBCXRVWVUSUGJREGULTWBKUNTKL
Key: WZU, Decrypted Text: QWCDYSWXWVTVHKSFHVMUXCLVOULM
Key: VYT, Decrypted Text: RXDEZTXYXWUWILTGIWNVYDMWPVMN
Key: UXS, Decrypted Text: SYEFAUYZYXVXJMUHJXOWZENXQWNO
Key: TWR, Decrypted Text: TZFGBVZAZYWYKNVIKYPXAFOYRXOP
Key: SVQ, Decrypted Text: UAGHCWABAZXZLOWJLZQYBGPZSYPQ
Key: RUP, Decrypted Text: VBHIDXBCBAYAMPXKMARZCHQATZQR
Key: QTO, Decrypted Text: WCIJEYCDCBZBNQYLNBSADIRBUARS
Key: PSN, Decrypted Text: XDJKFZDEDCACORZMOCTBEJSCVBST
Key: ORM, Decrypted Text: YEKLGAEFEDBDPSANPDUCFKTDWCTU
Key: NQL, Decrypted Text: ZFLMHBFGFECEQTBOQEVDGLUEXDUV
Key: MDK, Decrypted Text: ASMNUCGTGFPFRGCPDFWQHMHFYQVW
Key: LCJ, Decrypted Text: BTNOVDHUHGQGSHDQEGXRINIGZRWX
Key: KBI, Decrypted Text: CUOPWEIVIHRHTIERFHYSJOJHASXY
Key: JAH, Decrypted Text: DVPQXFJWJISIUJFSGIZTKPKIBTYZ
Key: IZG, Decrypted Text: EWQRYGKXKJTJVKGTHJAULQLJCUZA
Key: HYF, Decrypted Text: FXRSZHLYLKUKWLHUIKBVMRMKDVAB
Key: GXE, Decrypted Text: GYSTAIMZMLVLXMIVJLCWNSNLEWBC
Key: FWD, Decrypted Text: HZTUBJNANMWMYNJWKMDXOTOMFXCD
Key: EVC, Decrypted Text: IAUVCKOBONXNZOKXLNEYPUPNGYDE
Key: DUB, Decrypted Text: JBVWDLPCPOYOAPLYMOFZQVQOHZEF
Key: CTA, Decrypted Text: KCWXEMQDQPZPBQMZNPGARWRPIAFG
Key: BSZ, Decrypted Text: LDXYFNRERQAQCRNAOQHBSXSQJBGH
Key: ARY, Decrypted Text: MEYZGOSFSRBRDSOBPRICTYTRKCHI
Key: ZQX, Decrypted Text: NFZAHPTGTSCSETPCQSJDUZUSLDIJ
Key: YPW, Decrypted Text: OGABIQUHUTDTFUQDRTKEVAVTMEJK
Key: XOV, Decrypted Text: PHBCJRVIVUEUGVRESULFWBWUNFKL
Key: WNU, Decrypted Text: QICDKSWJWVFVHWSFTVMGXCXVOGLM
Key: VMT, Decrypted Text: RJDELTXKXWGWIXTGUWNHYDYWPHMN
Key: ULS, Decrypted Text: SKEFMUYLYXHXJYUHVXOIZEZXQINO
Key: TKR, Decrypted Text: TLFGNVZMZYIYKZVIWYPJAFAYRJOP
Key: SJQ, Decrypted Text: UMGHOWANAZJZLAWJXZQKBGBZSKPQ
Key: RIP, Decrypted Text: VNHIPXBOBAKAMBXKYARLCHCATLQR
Key: QHO, Decrypted Text: WOIJQYCPCBLBNCYLZBSMDIDBUMRS
Key: PGN, Decrypted Text: XPJKRZDQDCMCODZMACTNEJECVNST
Key: OFM, Decrypted Text: YQKLSAEREDNDPEANBDUOFKFDWOTU
Key: NEL, Decrypted Text: ZRLMTBFSFEOEQFBOCEVPGLGEXPUV
Key: MJF, Decrypted Text: AMRNOHGNLFJKRAHPXKWKMMBKYKAW
Key: LIE, Decrypted Text: BNSOPIHOMGKLSBIQYLXLNNCLZLBX
Key: KEY, Decrypted Text: CRYPTOISSHORTFORCRYPTOGRAPHY
Key: KHD, Decrypted Text: COTPQJIPNHLMTCJRZMYMOODMAMCY
Key: JGC, Decrypted Text: DPUQRKJQOIMNUDKSANZNPPENBNDZ
Key: IFB, Decrypted Text: EQVRSLKRPJNOVELTBOAOQQFOCOEA
Key: HEA, Decrypted Text: FRWSTMLSQKOPWFMUCPBPRRGPDPFB
Key: GDZ, Decrypted Text: GSXTUNMTRLPQXGNVDQCQSSHQEQGC
Key: FCY, Decrypted Text: HTYUVONUSMQRYHOWERDRTTIRFRHD
Key: EBX, Decrypted Text: IUZVWPOVTNRSZIPXFSESUUJSGSIE
Key: DAW, Decrypted Text: JVAWXQPWUOSTAJQYGTFTVVKTHTJF
Key: CZV, Decrypted Text: KWBXYRQXVPTUBKRZHUGUWWLUIUKG
Key: BYU, Decrypted Text: LXCYZSRYWQUVCLSAIVHVXXMVJVLH
Key: AXT, Decrypted Text: MYDZATSZXRVWDMTBJWIWYYNWKWMI
Key: ZWS, Decrypted Text: NZEABUTAYSWXENUCKXJXZZOXLXNJ
Key: YVR, Decrypted Text: OAFBCVUBZTXYFOVDLYKYAAPYMYOK
Key: XUQ, Decrypted Text: PBGCDWVCAUYZGPWEMZLZBBQZNZPL
Key: WTP, Decrypted Text: QCHDEXWDBVZAHQXFNAMACCRAOAQM
Key: VSO, Decrypted Text: RDIEFYXECWABIRYGOBNBDDSBPBRN
Key: URN, Decrypted Text: SEJFGZYFDXBCJSZHPCOCEETCQCSO
Key: TQM, Decrypted Text: TFKGHAZGEYCDKTAIQDPDFFUDRDTP
Key: SPL, Decrypted Text: UGLHIBAHFZDELUBJREQEGGVESEUQ
Key: ROK, Decrypted Text: VHMIJCBIGAEFMVCKSFRFHHWFTFVR
Key: QNJ, Decrypted Text: WINJKDCJHBFGNWDLTGSGIIXGUGWS
Key: PMI, Decrypted Text: XJOKLEDKICGHOXEMUHTHJJYHVHXT
Key: OLH, Decrypted Text: YKPLMFELJDHIPYFNVIUIKKZIWIYU
Key: NKG, Decrypted Text: ZLQMNGFMKEIJQZGOWJVJLLAJXJZV
```

# Source for MID > Country mapping: https://www.vtexplorer.com/mmsi-mid-codes-en/ 

vessel_flags = {
    201: "🇦🇱", # Albania
    202: "🇦🇩", # Andorra
    203: "🇦🇹", # Austria
    # Note: Azores doesn't have its own flag emoji, using Portugal's flag
    204: "🇵🇹", # Azores
    205: "🇧🇪", # Belgium
    206: "🇧🇾", # Belarus
    207: "🇧🇬", # Bulgaria
    208: "🇻🇦", # Vatican
    209: "🇨🇾", # Cyprus
    210: "🇨🇾", # Cyprus
    211: "🇩🇪", # Germany
    212: "🇨🇾", # Cyprus
    213: "🇬🇪", # Georgia
    214: "🇲🇩", # Moldova
    215: "🇲🇹", # Malta
    216: "🇦🇲", # Armenia
    218: "🇩🇪", # Germany
    219: "🇩🇰", # Denmark
    220: "🇩🇰", # Denmark
    224: "🇪🇸", # Spain
    225: "🇪🇸", # Spain
    226: "🇫🇷", # France
    227: "🇫🇷", # France
    228: "🇫🇷", # France
    230: "🇫🇮", # Finland
    231: "🇫🇴", # Faroe Islands
    232: "🇬🇧", # United Kingdom
    233: "🇬🇧", # United Kingdom
    234: "🇬🇧", # United Kingdom
    235: "🇬🇧", # United Kingdom
    236: "🇬🇮", # Gibraltar
    237: "🇬🇷", # Greece
    238: "🇭🇷", # Croatia
    239: "🇬🇷", # Greece
    240: "🇬🇷", # Greece
    241: "🇬🇷", # Greece
    242: "🇲🇦", # Morocco
    243: "🇭🇺", # Hungary
    244: "🇳🇱", # Netherlands
    245: "🇳🇱", # Netherlands
    246: "🇳🇱", # Netherlands
    247: "🇮🇹", # Italy
    248: "🇲🇹", # Malta
    249: "🇲🇹", # Malta
    250: "🇮🇪", # Ireland
    251: "🇮🇸", # Iceland
    252: "🇱🇮", # Liechtenstein
    253: "🇱🇺", # Luxembourg
    254: "🇲🇨", # Monaco
    255: "🇵🇹", # Madeira
    256: "🇲🇹", # Malta
    257: "🇳🇴", # Norway
    258: "🇳🇴", # Norway
    259: "🇳🇴", # Norway
    261: "🇵🇱", # Poland
    262: "🇲🇪", # Montenegro
    263: "🇵🇹", # Portugal
    264: "🇷🇴", # Romania
    265: "🇸🇪", # Sweden
    266: "🇸🇪", # Sweden
    267: "🇸🇰", # Slovak Republic
    268: "🇸🇲", # San Marino
    269: "🇨🇭", # Switzerland
    270: "🇨🇿", # Czech Republic
    271: "🇹🇷", # Turkey
    272: "🇺🇦", # Ukraine
    273: "🇷🇺", # Russian Federation
    274: "🇲🇰", # North Macedonia
    275: "🇱🇻", # Latvia
    276: "🇪🇪", # Estonia
    277: "🇱🇹", # Lithuania
    278: "🇸🇮", # Slovenia
    279: "🇷🇸", # Serbia
    301: "🇦🇮", # Anguilla
    303: "🇺🇸", # Alaska
    304: "🇦🇬", # Antigua and Barbuda
    305: "🇦🇬", # Antigua and Barbuda
    306: "🇧🇶", # Netherlands Antilles
    307: "🇦🇼", # Aruba
    308: "🇧🇸", # Bahamas
    309: "🇧🇸", # Bahamas
    310: "🇧🇲", # Bermuda
    311: "🇧🇸", # Bahamas
    312: "🇧🇿", # Belize
    314: "🇧🇧", # Barbados
    316: "🇨🇦", # Canada
    319: "🇰🇾", # Cayman Islands
    321: "🇨🇷", # Costa Rica
    323: "🇨🇺", # Cuba
    325: "🇩🇲", # Dominica
    327: "🇩🇴", # Dominican Republic
    329: "🇬🇵", # Guadeloupe
    330: "🇬🇩", # Grenada
    331: "🇬🇱", # Greenland
    332: "🇬🇹", # Guatemala
    334: "🇭🇳", # Honduras
    336: "🇭🇹", # Haiti
    338: "🇺🇸", # United States of America
    339: "🇯🇲", # Jamaica
    341: "🇰🇳", # Saint Kitts and Nevis
    343: "🇱🇨", # Saint Lucia
    345: "🇲🇽", # Mexico
    347: "🇲🇶", # Martinique
    348: "🇲🇸", # Montserrat
    350: "🇳🇮", # Nicaragua
    351: "🇵🇦", # Panama
    352: "🇵🇦", # Panama
    353: "🇵🇦", # Panama
    354: "🇵🇦", # Panama
    # 355-357 not assigned
    358: "🇵🇷", # Puerto Rico
    359: "🇸🇻", # El Salvador
    361: "🇵🇲", # Saint Pierre and Miquelon
    362: "🇹🇹", # Trinidad and Tobago
    364: "🇹🇨", # Turks and Caicos Islands
    366: "🇺🇸", # United States of America
    367: "🇺🇸", # United States of America
    368: "🇺🇸", # United States of America
    369: "🇺🇸", # United States of America
    370: "🇵🇦", # Panama
    371: "🇵🇦", # Panama
    372: "🇵🇦", # Panama
    375: "🇻🇨", # Saint Vincent and the Grenadines
    376: "🇻🇨", # Saint Vincent and the Grenadines
    377: "🇻🇨", # Saint Vincent and the Grenadines
    378: "🇻🇬", # British Virgin Islands
    379: "🇻🇮", # US Virgin Islands
    401: "🇦🇫", # Afghanistan
    403: "🇸🇦", # Saudi Arabia
    405: "🇧🇩", # Bangladesh
    408: "🇧🇭", # Bahrain
    410: "🇧🇹", # Bhutan
    412: "🇨🇳", # China
    413: "🇨🇳", # China
    416: "🇹🇼", # Taiwan
    417: "🇱🇰", # Sri Lanka
    419: "🇮🇳", # India
    422: "🇮🇷", # Iran
    423: "🇦🇿", # Azerbaijan
    425: "🇮🇶", # Iraq
    428: "🇮🇱", # Israel
    431: "🇯🇵", # Japan
    432: "🇯🇵", # Japan
    434: "🇹🇲", # Turkmenistan
    436: "🇰🇿", # Kazakhstan
    437: "🇺🇿", # Uzbekistan
    438: "🇯🇴", # Jordan
    440: "🇰🇷", # South Korea
    441: "🇰🇷", # South Korea
    443: "🇵🇸", # Palestine
    445: "🇰🇵", # North Korea
    447: "🇰🇼", # Kuwait
    450: "🇱🇧", # Lebanon
    451: "🇰🇬", # Kyrgyzstan
    453: "🇲🇴", # Macao
    455: "🇲🇻", # Maldives
    457: "🇲🇳", # Mongolia
    459: "🇳🇵", # Nepal
    461: "🇴🇲", # Oman
    463: "🇵🇰", # Pakistan
    466: "🇶🇦", # Qatar
    468: "🇸🇾", # Syria
    470: "🇦🇪", # UAE
    473: "🇾🇪", # Yemen
    475: "🇾🇪", # Yemen
    477: "🇭🇰", # Hong Kong
    478: "🇧🇦", # Bosnia and Herzegovina
    501: "🇫🇷", # Adelie Land
    503: "🇦🇺", # Australia
    506: "🇲🇲", # Myanmar
    508: "🇧🇳", # Brunei
    510: "🇫🇲", # Micronesia
    511: "🇵🇼", # Palau
    512: "🇳🇿", # New Zealand
    514: "🇰🇭", # Cambodia
    515: "🇰🇭", # Cambodia
    516: "🇨🇽", # Christmas Island
    518: "🇨🇰", # Cook Islands
    520: "🇫🇯", # Fiji
    523: "🇨🇨", # Cocos Islands
    525: "🇮🇩", # Indonesia
    529: "🇰🇮", # Kiribati
    531: "🇱🇦", # Laos
    533: "🇲🇾", # Malaysia
    536: "🇲🇵", # Northern Mariana Islands
    538: "🇲🇭", # Marshall Islands
    540: "🇳🇨", # New Caledonia
    542: "🇳🇺", # Niue
    544: "🇳🇷", # Nauru
    546: "🇵🇫", # French Polynesia
    548: "🇵🇭", # Philippines
    553: "🇵🇬", # Papua New Guinea
    555: "🇵🇳", # Pitcairn Islands
    557: "🇸🇧", # Solomon Islands
    559: "🇦🇸", # American Samoa
    561: "🇼🇸", # Samoa
    563: "🇸🇬", # Singapore
    564: "🇸🇬", # Singapore
    565: "🇸🇬", # Singapore
    567: "🇹🇭", # Thailand
    570: "🇹🇴", # Tonga
    572: "🇹🇻", # Tuvalu
    574: "🇻🇳", # Vietnam
    576: "🇻🇺", # Vanuatu
    578: "🇼🇫", # Wallis and Futuna
    601: "🇿🇦", # South Africa
    603: "🇦🇴", # Angola
    605: "🇩🇿", # Algeria
    607: "🇹🇫", # Saint Paul and Amsterdam Islands
    608: "🇦🇨", # Ascension Island
    609: "🇧🇮", # Burundi
    610: "🇧🇯", # Benin
    611: "🇧🇼", # Botswana
    612: "🇨🇫", # Central African Republic
    613: "🇨🇲", # Cameroon
    615: "🇨🇬", # Republic of the Congo
    616: "🇰🇲", # Comoros
    617: "🇨🇻", # Cape Verde
    618: "🇹🇫", # Crozet Archipelago
    619: "🇨🇮", # Ivory Coast
    621: "🇩🇯", # Djibouti
    622: "🇪🇬", # Egypt
    624: "🇪🇹", # Ethiopia
    625: "🇪🇷", # Eritrea
    626: "🇬🇦", # Gabon
    627: "🇬🇭", # Ghana
    629: "🇬🇲", # Gambia
    630: "🇬🇼", # Guinea-Bissau
    631: "🇬🇶", # Equatorial Guinea
    632: "🇬🇳", # Guinea
    633: "🇧🇫", # Burkina Faso
    634: "🇰🇪", # Kenya
    635: "🇹🇫", # Kerguelen Islands
    636: "🇱🇷", # Liberia
    637: "🇱🇷", # Liberia
    642: "🇱🇾", # Libya
    644: "🇱🇸", # Lesotho
    645: "🇲🇺", # Mauritius
    647: "🇲🇬", # Madagascar
    649: "🇲🇱", # Mali
    650: "🇲🇿", # Mozambique
    654: "🇲🇷", # Mauritania
    655: "🇲🇼", # Malawi
    656: "🇳🇪", # Niger
    657: "🇳🇬", # Nigeria
    659: "🇳🇦", # Namibia
    660: "🇷🇪", # Reunion
    661: "🇷🇼", # Rwanda
    662: "🇸🇩", # Sudan
    664: "🇸🇨", # Seychelles
    665: "🇸🇭", # Saint Helena
    666: "🇸🇴", # Somalia
    667: "🇸🇱", # Sierra Leone
    668: "🇸🇹", # Sao Tome and Principe
    669: "🇸🇿", # Eswatini
    670: "🇹🇩", # Chad
    671: "🇹🇬", # Togo
    672: "🇹🇳", # Tunisia
    674: "🇹🇿", # Tanzania
    675: "🇺🇬", # Uganda
    676: "🇨🇩", # Democratic Republic of the Congo
    677: "🇹🇿", # Tanzania
    678: "🇿🇲", # Zambia
    679: "🇿🇼", # Zimbabwe
    701: "🇦🇷", # Argentina
    710: "🇧🇷", # Brazil
    720: "🇧🇴", # Bolivia
    725: "🇨🇱", # Chile
    730: "🇨🇴", # Colombia
    735: "🇪🇨", # Ecuador
    740: "🇫🇰", # Falkland Islands
    745: "🇬🇫", # French Guiana
    750: "🇬🇾", # Guyana
    755: "🇵🇾", # Paraguay
    760: "🇵🇪", # Peru
    765: "🇸🇷", # Suriname
    770: "🇺🇾", # Uruguay
    775: "🇻🇪", # Venezuela
}
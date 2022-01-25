#!/usr/bin/env python3
# File name     : uri_schemes.py
# Author        : Jules Bozouklian (@bozou_client)
# Date created  : 24/01/2022

# URI schema based on :
# https://en.wikipedia.org/wiki/List_of_URI_schemes
# https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml

uri_map = {
    # OFFICIAL URI SCHEMES
    "http": 	                    "hXXp",
    "https": 	                    "hXXps",
    ### A
    "aaa":                          "(aaa)",
    "aaas":                         "(aaas)",
    "about":                        "(about)",
    "acap":                         "(acap)",
    "acct":                         "(acct)",
    "acd":                          "(acd)",
    "acr":                          "(acr)",
    "adiumxtra":                    "(adiumxtra)",
    "adt":                          "(adt)",
    "afp":                          "(afp)",
    "afs":                          "(afs)",
    "aim":                          "(aim)",
    "amss":                         "(amss)",
    "android":                      "(android)",
    "appdata":                      "(appdata)",
    "apt":                          "(apt)",
    "ar":                           "(ar)",
    "ark":                          "(ark)",
    "attachment":                   "(attachment)",
    "aw":                           "(aw)",
    ### B
    "barion":                       "(barion)",
    "beshare":                      "(beshare)",
    "bitcoin":                      "(bitcoin)",
    "bitcoincash":                  "(bitcoincash)",
    "blob":                         "(blob)",
    "bolo":                         "(bolo)",
    "browserext":                   "(browserext)",
    ### C
    "cabal":                        "(cabal)",
    "calculator":                   "(calculator)",
    "callto":                       "(callto)",
    "cap":                          "(cap)",
    "cast":                         "(cast)",
    "casts":                        "(casts)",
    "chrome":                       "(chrome)",
    "chrome-extension":             "(chrome-extension)",
    "com-eventbrite-attendee":      "(com-eventbrite-attendee)",
    "cid":                          "(cid)",
    "coap":                         "(coap)",
    "coap+tcp":                     "(coap+tcp)",
    "coap+ws":                      "(coap+ws)",
    "coaps":                        "(coaps)",
    "coaps+tcp":                     "(coaps+tcp)",
    "coaps+ws":                      "(coaps+ws)",
    "content":                      "(content)",
    "content-type":                 "(content-type)",
    "crid":                         "(crid)",
    "cvs":                          "(cvs)",
    ### D
    "dab":                          "(dab)",
    "dav":                          "(dav)",
    "diaspora":                     "(diaspora)",
    "data":                         "(data)",
    "dict":                         "(dict)",
    "did":                          "(did)",
    "dis":                          "(dis)",
    "dlna-playsingle":              "(dlna-playsingle)",
    "dlna-playcontainer":           "(dlna-playcontainer)",
    "dns":                          "(dns)",
    "dntp":                         "(dntp)",
    "doi":                          "(doi)",
    "dpp":                          "(dpp)",
    "drm":                          "(drm)",
    "drop":                         "(drop)",
    "dtmi":                         "(dtmi)",
    "dtn":                          "(dtn)",
    "dvb":                          "(dvb)",
    "dvx":                          "(dvx)",
    "dweb":                         "(dweb)",
    ### E
    "ed2k":                         "(ed2k)",
    "elsi":                         "(elsi)",
    "embedded":                     "(embedded)",
    "ens":                          "(ens)",
    "ethereum":                     "(ethereum)",
    "example":                      "(example)",
    ### F
    "facetime":                     "(facetime)",
    "fax":                          "(fax)",
    "feed":                         "(feed)",
    "feedready":                    "(feedready)",
    "fido":                         "(fido)",
    "file":                         "(file)",
    "filesystem":                   "(filesystem)",
    "finger":                       "(finger)",
    "first-run-pen-experience":     "(first-run-pen-experience)",
    "fish":                         "(fish)",
    "fm":                           "(fm)",
    "ftp":                          "(ftp)",
    "fuschia-pkg":                  "(fuschia-pkg)",
    ### G
    "gemini":                       "(gemini)",
    "geo":                          "(geo)",
    "gg":                           "(gg)",
    "git":                          "(git)",
    "gizmoproject":                 "(gizmoproject)",
    "go":                           "(go)",
    "gopher":                       "(gopher)",
    "gtalk":                        "(gtalk)",
    "graph":                        "(graph)",
    ### H
    "ham":                          "(ham)",
    "hcap":                         "(hcap)",
    "h323":                         "(h323)",
    "hcp":                          "(hcp)",
    "hydrazone":                    "(hydrazone)",
    "hyper":                        "(hyper)",
    ### I
    "iax":                          "(iax)",
    "icap":                         "(icap)",
    "icon":                         "(icon)",
    "im":                           "(im)",
    "im:sip":                       "(im:sip)",
    "imap":                         "(imap)",
    "info":                         "(info)",
    "iotdisco":                     "(iotdisco)",
    "ipn":                          "(ipn)",
    "ipns":                         "(ipns)",
    "ipp":                          "(ipp)",
    "ipps":                         "(ipps)",
    "irc":                          "(irc)",
    "irc6":                         "(irc6)",
    "ircs":                         "(ircs)",
    "iris":                         "(iris)",
    "iris.beep":                    "(iris.beep)",
    "iris.xpc":                     "(iris.xpc)",
    "iris.xpcs":                    "(iris.xpcs)",
    "iris.lws":                     "(iris.lws)",
    "isostore":                     "(isostore)",
    "itms":                         "(itms)",
    ### J
    "jabber":                       "(jabber)",
    "jar":                          "(jar)",
    "jms":                          "(jms)",
    ### K
    "keyparc":                      "(keyparc)",
    ### L
    "lastfm":                       "(lastfm)",
    "lbry":                         "(lbry)",
    "ldap":                         "(ldap)",
    "ldaps":                        "(ldaps)",
    "leaptofrogans":                "(leaptofrogans)",
    "lorawan":                      "(lorawan)",
    "lvlt":                         "(lvlt)",
    ### M
    "magnet":                       "(magnet)",
    "mailserver":                   "(mailserver)",
    "mailto":                       "(mailto)",
    "maps":                         "(maps)",
    "market":                       "(market)",
    "matrix":                       "(matrix)",
    "message":                      "(message)",
    "mid":                          "(mid)",
    "mms":                          "(mms)",
    "modem":                        "(modem)",
    "mongodb":                      "(mongodb)",
    "moz":                          "(moz)",
    "ms-help":                      "(ms-help)",
    "ms-settings":                  "(ms-settings)",
    "ms-access":                    "(ms-access)",
    "ms-browser-extension":         "(ms-browser-extension)",
    "ms-calculator":                "(ms-calculator)",
    "ms-drive-to":                  "(ms-drive-to)",
    "ms-enrollment":                "(ms-enrollment)",
    "ms-excel":                     "(ms-excel)",
    "ms-eyecontrolspeech":          "(ms-eyecontrolspeech)",
    "ms-gamebarservices":           "(ms-gamebarservices)",
    "ms-gamingoverlay":             "(ms-gamingoverlay)",   
    "ms-getoffice":                 "(ms-getoffice)",
    "ms-help":                      "(ms-help)",
    "ms-infopath":                  "(ms-infopath)",
    "ms-inputapp":                  "(ms-inputapp)",
    "ms-lockscreencomponent-config":"(ms-lockscreencomponent-config)",
    "ms-media-stream-id":           "(ms-media-stream-id)",
    "ms-meetnow":                   "(ms-meetno)",
    "ms-mixedrealitycapture":       "(ms-mixedrealitycapture)",
    "ms-mobileplans":               "(ms-mobileplans)",
    "ms-officeapp":                 "(ms-officeapp)",
    "ms-people":                    "(ms-people)",
    "ms-project":                   "(ms-project)",
    "ms-powerpoint":                "(ms-powerpoint)",
    "ms-publisher":                 "(ms-publisher)",
    "ms-restoretabcompanion":       "(ms-restoretabcompanion)",
    "ms-screenclip":                "(ms-screenclip)",
    "ms-screensketch":              "(ms-screensketch)",
    "ms-search":                    "(ms-search)",
    "ms-search-repair":             "(ms-search-repair)",
    "ms-secondary-screen-controller":"(ms-secondary-screen-controller)",
    "ms-secondary-screen-setup":    "(ms-secondary-screen-setup)",
    "ms-settings":                  "(ms-settings)",
    "ms-spd":                       "(ms-spd)",
    "ms-stickers":                  "(ms-stickers)",
    "ms-sttoverlay":                "(ms-sttoverlay)",
    "ms-transit-to":                "(ms-transit-to)",
    "ms-useractivityset":           "(ms-useractivityset)",
    "ms-virtualtouchpad":           "(ms-virtualtouchpad)",
    "ms-walk-to":                   "(ms-walk-to)",   
    "ms-whiteboard":                "(ms-whiteboard)",
    "ms-whiteboard-cmd":            "(ms-whiteboard-cmd)",
    "ms-visio":                     "(ms-visio)",
    "ms-word":                      "(ms-word)",
    "msnim":                        "(msnim)",
    "msrp":                         "(msrp)",
    "msrps":                        "(msrps)",
    "mss":                          "(mss)",
    "mt":                           "(mt)",
    "mtqp":                         "(mtqp)",
    "mumble":                       "(mumble)",
    "mupdate":                      "(mupdate)",
    "mvn":                          "(mvn)",
    ### N
    "news":                         "(news)",
    "nfs":                          "(nfs)",
    "ni":                           "(ni)",
    "nih":                          "(nih)",
    "nntp":                         "(nntp)",
    "notes":                        "(notes)",
    "num":                          "(num)",
    ### O
    "ocf":                          "(ocf)",
    "oid":                          "(oid)",
    "onenote":                      "(onenote)",
    "onenote-cmd":                  "(onenote-cmd)",
    "opaquelocktoken":              "(opaquelocktoken)",
    "openpgp4fpr":                  "(openpgp4fpr)",
    "otpauth":                      "(otpauth)",
    ### P
    "pack":                         "(pack)",
    "palm":                         "(palm)",
    "paparazzi":                    "(paparazzi)",
    "payment":                      "(payment)",
    "payto":                        "(payto)",
    "pkcs11":                       "(pkcs11)",
    "platform":                     "(platform)",
    "pop":                          "(pop)",
    "pres":                         "(pres)",
    "prospero":                     "(prospero)",
    "proxy":                        "(proxy)",
    "pwid":                         "(pwid)",
    "psyc":                         "(psyc)",
    "pttp":                         "(pttp)",
    ### Q
    "qb":                           "(qb)",
    "query":                        "(query)",
    "quic-transport":               "(quic-transport)",
    ### R
    "redis":                        "(redis)",
    "rediss":                       "(rediss)",
    "reload":                       "(reload)",
    "res":                          "(res)",
    "resource":                     "(resource)",
    "rmi":                          "(rmi)",
    "rsync":                        "(rsync)",
    "rtmfp":                        "(rtmfp)",
    "rtmp":                         "(rtmp)",
    "rtsp":                         "(rtsp)",
    "rtspu":                        "(rtspu)",
    ### S
    "sarif":                        "(sarif)",
    "s3":                           "(s3)",
    "secondlife":                   "(secondlife)",
    "secret-token":                 "(secret-token)",
    "service":                      "(service)",
    "session":                      "(session)",
    "sftp":                         "(sftp)",
    "sgn":                          "(sgn)",
    "shc":                          "(shc)",
    "shttp":                        "(shttp)",
    "sieve":                        "(sieve)",
    "simpleledger":                 "(simpleledger)",
    "simplex":                      "(simplex)",
    "sip":                          "(sip)",
    "sips":                         "(sips)",
    "skype":                        "(skype)",
    "smb":                          "(smb)",
    "sms":                          "(sms)",
    "smtp":                         "(smtp)",
    "snews":                        "(snews)",
    "snmp":                         "(snmp)",
    "soap.beep":                    "(soap.beep)",
    "soap.beeps":                   "(soap.beeps)",
    "soldat":                       "(soldat)",
    "spiffe":                       "(spiffe)",
    "spotify":                      "(spotify)",
    "ssb":                          "(ssb)",
    "ssh":                          "(ssh)",
    "steam":                        "(steam)",
    "stun":                         "(stun)",
    "stuns":                        "(stuns)",
    "submit":                       "(submit)",
    "svn":                          "(svn)",
    ### T
    "tag":                          "(tag)",
    "teamspeak":                    "(teamspeak)",
    "tel":                          "(tel)",
    "teliaeid":                     "(teliaeid)",
    "telnet":                       "(telnet)",
    "tftp":                         "(tftp)",
    "things":                       "(things)",
    "thismessage":                  "(thismessage)",
    "tn3270":                       "(tn3270)",
    "tip":                          "(tip)",
    "tool":                         "(tool)",
    "turn":                         "(turn)",
    "turns":                        "(turns)",
    "tv":                           "(tv)",
    ### U
    "udp":                          "(udp)",
    "unreal":                       "(unreal)",
    "urn":                          "(urn)",
    "ut2004":                       "(ut2004)",
    "uuid-in-package":              "(uuid-in-package)",
    ### V
    "v-event":                      "(v-event)",
    "vemmi":                        "(vemmi)",
    "ventrilo":                     "(ventrilo)",
    "ves":                          "(ves)",
    "videotex":                     "(videotex)",
    "view-source":                  "(view-source)",
    "vnc":                          "(vnc)",
    "vscode":                       "(vscode)",
    "vscode-insiders":              "(vscode-insiders)",
    "vsls":                         "(vsls)",
    ### W
    "wais":                         "(wais)",
    "wcr":                          "(wcr)",
    "webcal":                       "(webcal)",
    "wifi":                         "(wifi)",
    "wpid":                         "(wpid)",
    "ws":                           "(ws)",
    "wss":                          "(wss)",
    "wtai":                         "(wtai)",
    "wyciwyg":                      "(wyciwyg)",
    ### X
    "xcon":                         "(xcon)",
    "xcon-userid":                  "(xcon-userid)",
    "xfire":                        "(xfire)",
    "xmlrpc.beep":                  "(xmlrpc.beep)",
    "xmlrpc.beeps":                 "(xmlrpc.beeps)",
    "xmpp":                         "(xmpp)",
    "xri":                          "(xri)",
    ### Y
    "ymsgr":                        "(ymsgr)",
    ### Z
    "z39.50":                       "(z39.50)",
    "z39.50r":                       "(z39.50r)",
    "z39.50s":                       "(z39.50s)",
    # UNOFFICIAL BUT COMMON URI SCHEMES
    "admin":        "(admin)",
    "app":          "(app)",
    "javascript":   "(javascript)",
    "jdbc":         "(jdbc)",
    "odbc":         "(odbc)",
    "stratum+tcp":  "(stratum+tcp)",
    "stratum+udp":  "(stratum+udp)",
    "trueconf":     "(trueconf)",
    "slack":        "(slack)",
    "web+":         "(web+)",
    "zoommtg":      "(zoommtg)",
    "zoomus":       "(zoomus)",
    # SYMBOL
    ".":    "[.]",
    ":": 	"[:]",
    "@": 	"[@]"
}

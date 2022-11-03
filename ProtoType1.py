import cv2

p = ["130de601", "17c31ffc", "13943bb3", "141e7339", "1258deec", "7eefa5b0", "14ba0cd2", "c51cae0e", "14d01bb8", "5f3d5129", "143ff720", "106f9f3a", "5ce28d02", "af66eb85", "e7e6ecbb", "12b61424", "1210e0f5", "1656d5ea"]
s = [["42d750d3", "d93a1cd3", "a4d8a504", "e8cc2047", "231bc8c7", "9ff93fcc", "cdfe6d49", "5dc2e220", "9461168a", "bb02d49d", "415f39dd", "cfa7c30b", "2b19f288", "263c6296", "7daa8347", "df28fd52", "872adb10", "b7884da6", "542d564a", "50f5f14c", "e102bb65", "ba8ffd60", "73a024e9", "579e1eb0", "dadd2fba", "4fe5e4e6", "6bc862fe", "46df4cdf", "bd44a088", "5b1e2a8c", "bbe3fd50", "39dfcfbe", "10a0840e", "dbb4c605", "949b3a1b", "70570686", "86da1b12", "d917b74c", "9d8f04d5", "9e9ce021", "e7af332e", "ac8e30ff", "2249d25c", "7869d269", "4dedfb9d", "187d6a81", "cefdc8b3", "1d4d2dab", "d5f3f9a5", "4b710c75", "a0f90e6f", "8476172e", "14d19723", "8a9f7779", "b66144e8", "85a62108", "df4899b6", "1fb7ea93", "bc695a12", "c79f1ede", "b6f374ea", "21c0c1f6", "d931aee8", "59bd60d2", "92dc7499", "38358883", "bd84895e", "c4ce80d5", "9dd67e15", "13c011ed", "4b43d918", "8e0d3e60", "474f1db0", "3e39482a", "def7cd4e", "454ae9bf", "c15ca48d", "7d855be7", "e0a7a6a6", "777d1530", "59c0b450", "a2595b42", "735c681a", "133f88d1", "699a54fb", "d8859c18", "3210beb9", "d1d932ce", "58a9fc66", "48f4267b", "3650c21f", "45cd03f8", "e65412d3", "d3e4fd1c", "e1c09c27", "d9c860e2", "d7250995", "e85f2da8", "4140cbec", "acf317de", "e0c926a8", "e1b6cc1c", "ab04d6fc", "1a9c0e7e", "13357389", "10f0e214", "31bf2bf9", "a0d79cac", "b9809fd4", "5f719c62", "d52e41d0", "7af0fd82", "b4b11869", "c4b73c1f", "56a36454", "a93d0cc8", "431511d8", "a505feab", "e23550a9", "d05fc184", "cc5460aa", "5788e3a8", "5e3078de", "8ccfb64e", "43219258", "392c17a6", "be6f61a1", "31b6acdb", "b81db135", "8c1af864", "c271fc54", "d21493a0", "81d41675", "5d7fc502", "371e7269", "20ac75fd", "1bf994eb", "e3370d67", "75620c35", "932b84c9", "17ee8aca", "a3c480d1", "99bb2f5c", "1ac654e7", "2ef0f602", "ab04ec81", "6e132132", "b48f1677", "36e146e9", "cb367a78", "122fa49a", "1ed2826a", "75b23a12", "6f0d552a", "3f5b4dde", "4453bdc2", "9c3a4ba6", "57d6d925", "65edf23d", "a1f1acf1", "403ffa7b", "6b6c66ba", "13e151cf", "7dd56193", "c2c26a57", "c24c931c", "8cc6a860", "7a5372db", "7198d2c3", "8fb27d4a", "cc408ae0", "d97b6ef5", "e08f72d0", "89958e36", "d54af9a6", "66e0dbbb", "e2918b0f", "6d96b2bb", "55ba1d5d", "c895065f", "da81af39", "797e4355", "80e2764e", "56e5f9b8", "6e46c536", "a30a6f4f", "be3e2e37", "c4e22cb5", "7185f0d0", "a1528f93", "c8c4e6f1", "6950e30b", "cbbd5063", "d761cc58", "df086fc8", "259a2003", "7b81f9e3", "6a0bd902", "c48fb466", "291c4c9d", "46324f41", "5b4cf2f5", "18a1368a", "901796ed", "69e78aa3", "b9925d76", "bbbce469", "7749ba6f", "63b56601", "d3a87421", "e779b108", "7daccbaf", "6e0b43d6", "b3eec04e", "82496e84", "35d3bc3d", "ba18579c", "831d0b41", "d66319b8", "97258002", "2c6ebdc5", "4aa68e11", "9a784bf0", "b70a9641", "1aeb5c8f", "47d3f185", "1ca1983b", "c9eb9afd", "864d1273", "a5c0e3f2", "1e3587eb", "d361f136", "bc32f9bb", "d0912167", "2b62aada", "58f07d44", "8b1dd788", "17c640a6", "c1a1aaea", "c578ab7f", "db64e46f", "90f2d653", "c66b7308", "a975f5e4", "e61656ff", "67cbbe5d", "5fe4704c", "9a643101", "8c8cf6ed", "17568889", "637d1fdc", "eab58e97", "2bb8006f", "930ad44b", "2d3ec041", "8e648747"], ["7a6e465f", "cea2d6f0", "16a0e88a", "6e15bae2", "c652ec14", "fb143c4b", "9158d5f1", "aa378a2c", "8e437842", "e11989e9", "ccbaf0be", "22f164a5", "c62e5ef9", "9159e620", "1dab3228", "e21eea34", "5e287d44", "4a8e99ac", "b54005cb", "c66b8ad2", "c0806fa8", "a81f37f9", "76d31097", "8772b5d2", "d222bb12", "4e89c7da", "b6c5404c", "7b9e5ca8", "2d880137", "aa960e3b", "39164db2", "10c6a92a", "1a91876a", "dd42f53e", "cd68f9e4", "99054b60", "6e1e6892", "3ea61a8a", "6f51bcb2", "6fab44c6", "65278617", "9ccecb8c", "b0661288", "4ac2e82f", "5edf4bc6", "3f2b943c", "a53a990e", "e69c707f", "b22da40d", "66482e37", "b7731ce1", "bd94f4a1", "7a91b417", "d905cd9c", "81cc5b5d", "77c9f220", "d27d0092", "7e7d5bb1", "e0323b78", "b87ce907", "6eacf1b2", "3d132d7d", "72ea075e", "1656c388", "84ad2aff", "50826f08", "e39988d5", "490105e1", "2d57986d", "41392a4b", "74d3fd55", "1c7e1e95", "456f5ebf", "5371e2ea", "7bdf13a4", "afeec75f", "3779da61", "a712a59f", "846a2f6b", "ade673be", "76a82a0c", "adb91e0b", "5b24163d", "68a3c0b5", "15c1b9d3", "a3b54606", "7c2f2705", "4ad07b7c", "7f922c25", "7d469b0f", "d98a2cb4", "9583284e", "69355669", "cefdfd9a", "e729369c", "a4b15759", "c12ec255", "268cc59e", "e314823c", "4bdd900f", "d6a819b5", "5e8dfeea", "7751d599", "4ffc4a01", "1baa6dbc", "4947e830", "997142c1", "bf619f67", "b12ca4f5", "45054e2e", "5bbc3db7", "2c650d6e", "9ce41b84", "c30376c6", "e669da0c", "9957044d", "335e5e89", "182ce1bb", "aae4add6", "34ca993d", "819f3ba4", "52201506", "34ea8ecf", "5570a7e9", "6edbc73a", "debc789e", "9c34baf7", "a6716052", "e03d103c", "9343ea73", "8e161c89", "c29c4f5e", "25a5f924", "e1632e3f", "548fcab8", "e1503a2e", "145e31f0", "96ebc86b", "7a04cbe7", "2c2d1a03", "b7feaf02", "147555ca", "b2db25fd", "78da3fad", "3bd582d0", "32d34046", "a59c5161", "20c594a5", "b673fe37", "c91309ce", "bdf1fbe4", "97bfd041", "d7260f7b", "aba21d5b", "49e9567b", "a7d33798", "e45caa4c", "57f4114c", "cf30fed0", "7adcb598", "471df50c", "c3d5a616", "89053d1e", "b829d62e", "ce8cf1a5", "d046dac6", "20027ad9", "c3eb019f", "ca92ed3b", "82f0fa8d", "8300e37a", "60fc0dd9", "de33f0e6", "50365e74", "e6292f51", "3d7e2d07", "30efdc95", "dfebb346", "2a000f1e", "868da1b9", "7be65c31", "2cbc2857", "8a24be0b", "1fe4ff75", "18dfa556", "7a866975", "a96fce46", "7a3d77e3", "37ecc0a7", "e04e10db", "d66f428d", "474c1654", "c947cd48", "46fe9148", "a9f7928a", "7db036e6", "82f756a1", "bad6adb3", "a0a7aee6", "591bb472", "d73eef1f", "3592fbd6", "6bfdf6a7", "bdf5eb01", "2c1142e9", "49b9ec6f", "6f3ce761", "ae7ad03f", "b7eac06a", "d535a2da", "46d6a9b6", "715f3603", "5b873336", "ca5b3a25", "b8499828", "785f7a21", "91dd6d0f", "eb8943d1", "8cee1a34", "cdaf5c9e", "a1962668", "5835a222", "5101dfb3", "2819ea54", "39c108e8", "1158190c", "be4cb56e", "5166ddf5", "d85bd315", "8b8c9904", "20f85ffc", "dee0a16f", "af4823a5", "7c250c9c", "c9331357", "e82be1f5", "189475ed", "e18cded6", "63957be6", "cb313a7a", "caaac984", "5d7d9264", "4560a2a5", "30d17bc5", "8a4f1275", "c7a4f3e9", "f016f34c", "5510986b", "2bbcf346", "3c2c561c", "e2f7f430", "de52137b", "c0f7e62b", "8342bed3", "97a60883", "4d80fc"], ["978fd788", "9952a483", "e4b903ea", "5eb1cb68", "d66d23d8", "d79515e8", "d3fa689c", "7a4c7a77", "34f5fc4f", "68972357", "a5d47be0", "64b07402", "4c3ad186", "7d7294ea", "a730a0e0", "857cf683", "77f9c7d9", "ac08b2fa", "560db898", "7fd45cc4", "aef89f2a", "287f7bd9", "25302854", "66646e09", "c411edf6", "65ac0fea", "6efa37d9", "577debe5", "45d7d44b", "2b3cc2e6", "c09c0d96", "6213295b", "d8335608", "bd4d838c", "d95ec8f1", "3a757ea0", "a72a7f18", "936525f8", "97a6abad", "9b533e28", "8b0a80db", "2cea1788", "34307f00", "4710a9cc", "166aeac8", "29c8b4fa", "a037d9e6", "9214f5d8", "adebd9fd", "4b659f0e", "da70acb9", "fd9d8eda", "c329d88e", "772d2315", "fd1d83b7", "56f79142", "37e5827c", "380fbfdc", "37392c54", "7d5f7456", "ae204027", "541b6e7c", "2bbf54ff", "2baadad9", "3541609c", "4a79dfc2", "ada4bd1a", "27560d9f", "6f5bcf69", "6852256b", "87cae353", "290d3e17", "5cb9a7a5", "4371519b", "8ceb49b0", "e37685bd", "d5d4e45b", "c1abb0e0", "9b0675db", "e6279695", "1fb32a60", "6d1ad154", "3e7074f7", "dc7f8bed", "1563d8de", "91ca1960", "c46ad9ff", "503e0d32", "2fd69363", "1b3cac7e", "1d56d9dc", "ac4ca38c", "3ff0a7b5", "d7368665", "b26934bf", "3be0631e", "7fef1e11", "4963b627", "a1dd5640", "7748784d", "9afc231c", "6540ab2b", "bf91c4d2", "19721604", "6cb4481d", "4ee08b36", "1210548c", "80df3795", "95a43c30", "56c40dd0", "a4c07800", "4667ac9b", "11552665", "621c3fe4", "cf55975e", "e07794a6", "dbfd6d5d", "1b2676fa", "419c0ff6", "95ab39c8", "d736be94", "a1fa4f6a", "ba442167", "b3552a95", "9a0455e7", "6b06dc81", "a5cae411", "a088d542", "164402db", "d79227f0", "5fe97e41", "506a7f6c", "3f567517", "2b71caf5", "22923578", "e2a76c0b", "7dfadd89", "a2f6359d", "c504aced", "5572d01d", "596604a5", "72e7b794", "a2a6e82a", "7cba9fe5", "3ec48a19", "fcf50e9a", "87c67d33", "df58b2fa", "a7da27fe", "95213465", "62aba35c", "a07a2870", "fea63671", "d97038f2", "ce1e2a1b", "4b3a313d", "12906120", "4cbee2cf", "23f15d90", "d6434430", "5dc651b6", "d04d8917", "bdd99086", "8483470a", "dfd8d73c", "40c72e67", "498dde81", "c9c7f528", "2bb87b0f", "3a18111c", "8df6e387", "db273c3e", "68c60e1d", "cfbf1bcb", "76c312af", "41362a3f", "a6dc4670", "b48c40be", "91e12805", "cde55b5c", "22c7ac42", "b85cd5bc", "accf0a10", "69ce94c3", "71f2c8b5", "c9d958ad", "96923e95", "905121e7", "1062bf90", "37e2594a", "81250d27", "cf1aa981", "b4240c3c", "7103f5ae", "77d0d6ea", "441120ea", "620d7a72", "9ae869cc", "c1d8d6f1", "c368e2ef", "fbb63da4", "d78a71b2", "3effc7d0", "d5967b6f", "d4ccced4", "5a9889f6", "671b55db", "164ad009", "ab2fc6ae", "d9a6dc34", "430194f4", "6f11600f", "e3ee4057", "2f0eaea5", "bf9960f2", "3e0003eb", "616265be", "302eff6e", "d0c5b45c", "6ce46f4a", "a138eb43", "7de1a9f7", "41eba79e", "cd33f7da", "75708318", "a7abfd52", "712bdce5", "432513c2", "bcce2ca4", "c8397f63", "9bf7e03f", "e0164b29", "9001734e", "9e2d6150", "695290e5", "c4fd6019", "10683f60", "2c133385", "cc7a1a9d", "524f5c87", "d8229b3d", "6f9dd3f2", "c410c2d4", "87ce1a63", "be9f4431", "2c5071a9", "3edafbbc", "42414235", "652505fa", "52301a3c", "d31c567e", "17a26971", "74bc0a8f", "cc263f57", "9753f727", "1d25b263"], ["6f1b693e", "c6335597", "1f5ade6d", "2666140a", "8e4fa637", "db4e9345", "8269b811", "a6f76bb1", "e8659c8c", "d4e6782b", "59aa60f9", "7cde3356", "ccb682f0", "ad0e45b8", "62ca1906", "8f35e0b8", "b09cdfb5", "dc2cfd08", "23d51f57", "e3fe26e8", "831ef07a", "d57f6926", "b999cb07", "314b5fde", "b751d7df", "2d6a5af2", "5e24a888", "5b221853", "4d702461", "6aef6b63", "a1c0d004", "cb696a7b", "1da26764", "4f5f4c9c", "b64b1053", "49110010", "a10924c0", "94846d50", "3112a7b7", "6c87a381", "56ce14dd", "355c6a2a", "57e90ff4", "c534c35c", "575208e7", "ad819ad5", "29fe2451", "119b6926", "204d97ee", "2028ad1d", "9a3a32f3", "9876b554", "5dfbce1f", "7f01fa70", "4ca92788", "a60844b8", "3186edd5", "2686e848", "8bc55ce9", "88920ee9", "8e567505", "58f0be1d", "13acd1f6", "18dd3afa", "5d9b83d9", "736ca56f", "1932b5cc", "7a44d900", "a2541346", "23f195a6", "221afafa", "22103f30", "a1bf6f15", "c807f4dc", "61cea29d", "5f8fc8e4", "1599c47d", "3ce2ab7e", "4f03968e", "ba730179", "dd7902ef", "bc8ffc0d", "5ecb525e", "686f4f5e", "254eb836", "4a31b62c", "6463541d", "4866ead6", "a2b8155c", "b1987495", "2d58758f", "e191188f", "6b4a65d3", "2e1cf97c", "41b22a24", "257ca78f", "e0f00da6", "acd18702", "e8237721", "9ce7917e", "9ac60ed3", "68efd691", "e6eaf696", "8e5286bc", "c3049e67", "63e8da31", "6e1423c5", "2dd0177a", "ae9c9779", "6cac7ef2", "57cace39", "197bf3ff", "9fbecfe0", "2ecbc01d", "7db2e360", "a5351784", "1785168d", "77a054a5", "a38e2f5c", "50a6df21", "d40eecc2", "37b32a7e", "4d0d1b91", "4a1a914a", "4eba2c70", "a04e6815", "ac248229", "2ce14a2b", "86f66f81", "67dd61a9", "73e17f62", "289ac02b", "53ee62e4", "c121abf1", "76470ed3", "4d4ed53f", "2b52d58b", "e35b7352", "e8462cf8", "bb17e82c", "2716e81f", "e50cc3f2", "233b5d7b", "4d10a1ae", "cd5faa92", "5765b9a7", "386a357d", "493b753c", "75ee893d", "77f6ffc3", "785eb763", "5120f358", "15aa6b7d", "748ebc97", "41efbcdc", "6c7e2526", "480f51ba", "3c1a8708", "702684e7", "dcd28638", "269ccdb5", "706e95f4", "28f12b26", "4f4a7772", "c8929fcd", "87b34ae3", "49805776", "a8f31b46", "91bc2bf9", "29e175e5", "36a5513d", "51a3e99c", "57322601", "a16e4798", "276e128a", "92b29a7a", "90305707", "6d195149", "d90198ab", "e26a7f0d", "7229553f", "e149bf1d", "61885dcb", "a09af006", "4c2ddbdc", "587104f3", "271ad395", "4d4e5803", "b81a98da", "6931c450", "e1c0ae2f", "8068dd20", "58b09f30", "4e1bcc17", "6dca2c95", "4a8d179f", "3b65ee89", "d2fae6a2", "316e9b2f", "69cbe18e", "e118d96c", "48d31ef9", "649b5a7a", "da58e5ba", "75b0529d", "744b0880", "46cc934b", "138117a8", "e642a8d0", "7b94f25f", "980bf003", "b2bc7da8", "26b5223a", "1ee3d8e9", "6d199f9f", "968f06db", "8c964418", "e71bee28", "b5df915c", "19eea287", "8cebc713", "1a63f381", "92065008", "5f0933a1", "20503fbe", "37200038", "594e1942", "73c7d490", "b39d1b86", "42604bea", "95a220af", "8c6493c4", "95de5718", "e641cd12", "ce1a0664", "989d9589", "2b953027", "c1fce9d8", "9a9f585c", "b2a83b5b", "bc895187", "25d3da6e", "17ff3646", "49770eb2", "d69fbfe7", "22c54fa0", "a5b41e60", "44f3be63", "12560ad3", "a56139e3", "8ab9777e", "38869322", "305dd14b", "3897a0f7", "40853020", "900ec040"]]

def hextostr(text):
    temp = ""
    for i in range(0,len(text),2):
        temp += chr(int(text[i:i+2],16))
    return temp
def strtohex(text):
    return "".join(['{:002x}'.format(ord(x)) for x in text])
def hex_size(text, size = 8):
    return text.rjust(size * (len(text)/size).__ceil__(), "0")
def XOR(num1, num2):
    return hex_size(hex(int(num1, 16) ^ int(num2, 16))[2:])
def add(num1, num2):
    return hex_size(hex((int(num1, 16) + int(num2, 16)) % (2 ** 32))[2:])
def f(text):
    text = hex_size(text)
    a = [s[i//2][int(text[i : i + 2], 16)] for i in range(0, len(text), 2)]
    num = add(a[0], a[1])
    num = XOR(num, a[2])
    num = add(num, a[3])
    return num
def keyGenerate(text):
    text = [text[i : i + 8] for i in range(0, len(text), 8)]
    for i in range(len(p)):
        p_temp[i] = XOR(p[i], text[i%len(text)])
def round(num, text):
    left = XOR(text[0 : 8], p_temp[num])
    right = XOR(f(left), text[8 : 16])
    return right + left
def encrypt(text):
    cipherText = ""
    text = [text[i : i + 16] for i in range(0, len(text), 16)]
    for i in range(len(text)):
        for j in range(16):
            text[i] = round(j, text[i])
        right = XOR(text[i][0:8], p_temp[16])
        left = XOR(text[i][8:16], p_temp[17])

        cipherText += (left + right)
    cipherText = hextobin(cipherText)
    image = steg(cv2.imread('TEST.png'), cipherText)
    cv2.imwrite("TEST1.png",image)
def decrypt():
    text = bintohex(desteg(cv2.imread(f"TEST1.png")))
    plainText = ""
    text = [text[i : i + 16] for i in range(0, len(text), 16)]
    for i in range(len(text)):
        for j in range(17,1,-1):
            text[i] = round(j, text[i])
        right = XOR(text[i][0:8], p_temp[1])
        left = XOR(text[i][8:16], p_temp[0])

        plainText += (left + right)
    return plainText
def hextobin(num):
    return "".join(['{:04b}'.format(int(x,16)) for x in num])
def steg(img, text):
    length = len(text)
    temp = 0
    binlen = '{:030b}'.format(length)

    for i in range(-1,-11,-1):
        for j in range(3):
            img[-1][i][j] = int((('{:0b}'.format(int(img[-1][i][j])))[:-1]+binlen[0]),2)
            binlen = binlen[1:]

    for i in range(len(img)):
        for j in range(len(img[i])):
            for k in range(len(img[i][j])):
                img[i][j][k] = int((('{:0b}'.format(int(img[i][j][k])))[:-1]+text[0]),2)
                text = text[1:]
                temp += 1
                if (temp == length):
                    return img
def bintohex(text):
    return hex(int(text,2))[2:]
def desteg(img):
    length = ''
    data = ''
    temp = 0

    for i in range(-1,-11,-1):
        for j in range(3):
            length += ('{:0b}'.format(int(img[-1][i][j])))[-1]
    
    length = int(length,2)

    for i in range(len(img)):
        for j in range(len(img[i])):
            for k in range(len(img[i][j])):
                data += ('{:0b}'.format(int(img[i][j][k])))[-1]
                temp += 1
                if (temp == length):
                    return data

ch = eval(input("Press 1 to Encrypt Data\nPress 2 to Decrypt Data\n>>>"))
if(ch == 1):
    p_temp = p
    file= open("abcd.txt","r")
    data = file.read()
    plainText = hex_size(strtohex(data),16)
    key = input("Enter key\n>>>")
    key = hex_size(strtohex(key))
    keyGenerate(key)
    encrypt(plainText)
    print("Encrypted!!!")
elif(ch == 2):
    p_temp = p
    key = input("Enter key\n>>>")
    key = hex_size(strtohex(key))
    keyGenerate(key)
    print("-----Decryption-----")
    plainText = hextostr(decrypt())
    file1 = open('Decrypted.txt','w')
    file1.write(plainText)
    file1.close()
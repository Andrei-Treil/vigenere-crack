import sys
import itertools
import string

#letter frequencies from https://en.wikipedia.org/wiki/Letter_frequency
LETTER_FREQ = [8.2,1.5,2.8,4.3,13,2.2,2,6.1,7,0.15,0.77,4,2.4,6.7,7.5,1.9,0.095,6,6.3,9.1,2.8,0.98,2.4,0.15,2,0.074]
LETTER_FREQ = [i/100 for i in LETTER_FREQ]

#function to decrypt cipher given a key
def decrypt(text,key):

    if len(text) != len(key):
        key = list(key)
        for i in range(len(text) -len(key)):
            key.append(key[i % len(key)])
        key = "".join(key)

    decrypted = []
    for i in range(len(text)):
        letter = (ord(text[i]) - ord(key[i]) + 26) % 26
        letter += ord('A')
        decrypted.append(chr(letter))
    return("".join(decrypted))

def break_cipher(text,min_length,max_length):
    #all keys with their results
    res_keys = []

    for length in range(min_length,max_length):
        #keys for given key length
        keys = [None]*length
        for i in range(length):
            #amount to increase the letters
            increase = []
            #check every ith letter and compare char distribution
            ith_letter = "".join(itertools.islice(text,i,None,length))

            for letter in string.ascii_uppercase:
                increase.append((freq_analyze(decrypt(ith_letter,letter)),letter))

            keys[i] = min(increase, key=lambda arr: arr[0])[1]
        res_keys.append("".join(keys))
    res_keys.sort(key=lambda key: freq_analyze(decrypt(text,key)))
    
    print(res_keys[0] + " Deciphered: " + decrypt(text,res_keys[0]) + "\n")
    print(res_keys[1] + " Deciphered: " + decrypt(text,res_keys[1]) + "\n")

#compare frequency of text to letter distribution
def freq_analyze(text):
    freq = [0]*26
    
    for letter in text:
        freq[ord(letter) - ord('A')] += 1
    
    return sum(abs(text_freq / len(text) - letter_freq) for text_freq, letter_freq in zip(freq,LETTER_FREQ))

def main():
    glorgo = "TSMVM MPPCW CZUGX HPECP RFAUE IOBQW PPIMS FXIPCTSQPK SZNUL OPACR DDPKT SLVFW ELTKR GHIZS FNIDFARMUE NOSKR GDIPH WSGVL EDMCM SMWKP IYOJS TLVFAHPBJI RAQIW HLDGA IYOUX"
    break_cipher("".join(glorgo.split()),3,10)


if __name__ == '__main__':
    argv_len = len(sys.argv)
    main()
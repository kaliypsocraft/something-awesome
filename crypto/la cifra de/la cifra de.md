# CTF Write-Up: [La Cifra De][Cryptography]

## Description
>I found this cipher in an old book. Can you figure out what it says? Connect with nc jupiter.challenges.picoctf.org 5726.


## Flag
The flag you obtained after solving the challenge. (e.g., `picoCTF{b311a50_0r_v1gn3r3_c1ph3r7b996649}`)

## Difficulty
- **Difficulty Level:** medium

## Tools Used
- https://www.guballa.de/vigenere-solver

## Write-Up

### Preparatory Phase
Upon connecting to the server the client receives a block of text. It is enciphered, however the punctuation and word lengths are maintained Furthermore numbers which likely indicate years in history are maintained. 
```
Ne iy nytkwpsznyg nth it mtsztcy vjzprj zfzjy rkhpibj nrkitt ltc tnnygy ysee itd tte cxjltk

Ifrosr tnj noawde uk siyyzre, yse Bnretèwp Cousex mls hjpn xjtnbjytki xatd eisjd

Iz bls lfwskqj azycihzeej yz Brftsk ip Volpnèxj ls oy hay tcimnyarqj dkxnrogpd os 1553 my Mnzvgs Mazytszf Merqlsu ny hox moup Wa inqrg ipl. Ynr. Gotgat Gltzndtg Gplrfdo

Ltc tnj tmvqpmkseaznzn uk ehox nivmpr g ylbrj ts ltcmki my yqtdosr tnj wocjc hgqq ol fy oxitngwj arusahje fuw ln guaaxjytrd catizm tzxbkw zf vqlckx hizm ceyupcz yz tnj fpvjc hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3x7g996649}

Ehk ktryy herq-ooizxetypd jjdcxnatoty ol f aordllvmlbkytc inahkw socjgex, bls sfoe gwzuti 1467 my Rjzn Hfetoxea Gqmexyt.
Tnj Gimjyèrk Htpnjc iy ysexjqoxj dosjeisjd cgqwej yse Gqmexyt Doxn ox Fwbkwei Inahkw.

Tn 1508, Ptsatsps Zwttnjxiax tnbjytki ehk xz-cgqwej ylbaql rkhea (g rltxni ol xsilypd gqahggpty) ysaz bzuri wazjc bk f nroytcgq nosuznkse ol yse Bnretèwp Cousex.

Gplrfdo’y xpcuso butvlky lpvjlrki tn 1555 gx l cuseitzltoty ol yse lncsz. Yse rthex mllbjd ol yse gqahggpty fce tth snnqtki cemzwaxqj, bay ehk fwpnfmezx lnj yse osoed qptzjcs gwp mocpd hd xegsd ol f xnkrznoh vee usrgxp, wnnnh ify bk itfljcety hizm paim noxwpsvtydkse.
```

I suspected it to be either a subsitution cipher or Vigenere cipher. The reason being was due to the constant repeating of the trigram `yse` and `ltc`. I ran `grep -o . cipher.txt | sort -f | uniq -ic | sort` and noticed a relatively even spread of frequencies which indicates it likely is a Vigenere cipher
![alt text](images/image-1.png).

### Attack Phase
Using an online tool https://www.guballa.de/vigenere-solver, we were able to obtain the decryption quite easily. Reading their source code made me realise how non-trivial even breaking classical ciphers can be via [here](#https://www.guballa.de/bits-and-bytes/implementierung-des-vigenere-solvers).
### Final Solution/Payload
![alt text](images/image.png)

### Lessons Learnt
Conducting a Vigenere break manually without intervention from online tools is a relatively non-trivial task. Without knowledge of the key-length and key itself an operator would need to conduct Kasiski examination. This only produces a tentative list of possible key lengths. Once this is discovered one can conduct frequency analysis and using a fitness function: https://stackoverflow.com/questions/36620231/understanding-fitness-function

<details><summary> Dropdown for implementation of my attempt </bold> </summary>
<br>
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <map>
#include <set>
#include <algorithm>
#include <cctype>
#include <string.h>

/*
# ==============================================================================
# Conducting a basic Vigenere decryption utilising frequency analysis of unigrams,
# bigrams. Then comparing to common letters in English dictionary to obtain
# tentative keys.
#
# Written by: J.L (z5417289)
# ==============================================================================
*/

using namespace std;

map<pair<string, int>, pair<int, int>> scores;

const vector<string> commonFiveLetter = {
    "ABOUT", "OTHER", "WHICH", "THEIR", "THERE", "FIRST", "WOULD", 
    "THESE", "WHERE",
};
const vector<string> commonFourLetter = {
    "THAT", "THIS", "WITH", "FROM", "YOUR", "HAVE", "MORE", "WILL",
    "HOME", "WERE", "FREE", "TIME", "THEY", "SITE", "WHAT", "NEWS",
    "ONLY", "WHEN", "HERE", "ALSO", "DAYS",
};
const vector<string> commonThreeLetter = {
    "THE", "AND", "FOR", "ARE", "BUT", "NOT", "YOU", "ALL", "ANY", "CAN", 
    "HAD", "HER", "WAS", "ONE", "OUR", "OUT", "DAY", "GET", "HAS", "HIM", 
    "HIS", "HOW", "MAN", "NEW", "NOW", "OLD", "SEE", "TWO", "WAY", "WHO", 
    "BOY", "DID", "ITS", "LET", "PUT", "SAY", "SHE", "TOO", "USE"
};

const vector<string> bigrams = {
    "TH", "HE", "IN", "EN", "NT", "RE",
};

const vector<char> englishAlphaRanking = {
    'E', 'T', 'A', 'O', 'I', 
};

/*
# ==============================================================================
# findPlainText
# Given a key, keyLength and cipherText decrypts and returns the plainText.
#
# ==============================================================================
*/

string findPlainText(const string& CT, const string& key, int keyLength) {
    int textLength = CT.length();
    string plainText = "";
    int keyIndex = 0;
    for (char c : CT) {
        if (isalpha(c)) {
            char k = key[keyIndex % keyLength];
            c = toupper(c);
            k = toupper(k);
            char decryptedChar = (c - k + 26) % 26 + 'A';
            plainText += decryptedChar;
            keyIndex++;
        } else {
            plainText += c;
        } 
    }
    return plainText;
}

// Get frequencies of bigrams
vector<map<string, int>> getBigrams(const string& CT, int keyLength) {
    vector<map<string, int>> frequencies(keyLength);
    string temp = CT;
    temp.erase(remove_if(temp.begin(), temp.end(), ::isspace), temp.end());

    for (int i = 0; i < keyLength; i++) {
        map<string, int>& frequency = frequencies[i];  
        for (int j = i; j + 1 < temp.length(); j += keyLength) { 
            string bigram = temp.substr(j, 2);
            frequency[bigram]++;
        }
    }
    return frequencies;
}

// Get frequencies from monograms
vector<map<char, int>> getUnigrams(const string& CT, int keyLength) {
    vector<map<char, int>> frequencies(keyLength);
    string temp = CT;
    temp.erase(remove_if(temp.begin(), temp.end(), ::isspace), temp.end());

    for (int i = 0; i < keyLength; i++) {
        map<char, int>& frequency = frequencies[i];  
        for (int j = i; j < temp.length(); j += keyLength) { 
            char cipherLetter = temp[j];
            if (!isalpha(cipherLetter)) {
                continue;
            }
            if (frequency.count(cipherLetter) == 0) {
                frequency[cipherLetter] = 1;
            } else {
                frequency[cipherLetter]++;
            }
        }   
    }
    int counter = 1;
    for (const auto& elem : frequencies) {
        cout << "COLUMN : " << counter << endl;
        for (const auto& column : elem) {
            cout << "LETTER " << column.first << " : FREQ " << column.second  << endl;
        }
        counter++;
    }
    return frequencies;
}

// Iteratively alter key in order to fulfil greater ranking
string rectifyKey(string tentativeKey, pair<string, int> element, string desiredString) {
    bool pointsOfDifference[3];
    memset(pointsOfDifference, false, 3 * sizeof(bool));
    for (int i = 0; i < 3; i++) {
        if (desiredString[i] != element.first[i]) {
            pointsOfDifference[i] = true;
        }
    }
    
    for (int i = 0; i < 3; i++) {
        if (pointsOfDifference[i]) {
            char misplaceLetter = element.first[i];
            char desiredLetter = desiredString[i];
            int keyPosition = element.second + i;

            int diff = (misplaceLetter - desiredLetter + 26) % 26;  
            int keyLength = tentativeKey.length();
            tentativeKey[keyPosition % keyLength] = ((tentativeKey[keyPosition % keyLength] - 'A' + diff) % 26) + 'A';
        }
    }
    return tentativeKey;
}

// Gives a ranking based on common triplets
// Sees common letters and provides a ranking based on these findings.
set<string> getTripletRankings(map<string, int> threeLetterWords, string tentativeKey) {
    string commonFirst = "THE";
    string commonSecond = "AND";
    set<string> candidateKeys;
    candidateKeys.insert(tentativeKey);
    
    for (const auto& elem : threeLetterWords) {
        float ranking = 0;
        pair<int, int> rankings;
        for (int i = 0; i < 3; i++) {
            if (elem.first[i] == commonFirst[i]) {
                ranking++;
            } 
        }
        rankings.first = ranking;
        ranking = 0;
        for (int i = 0; i < 3; i++) {
            if (elem.first[i] == commonSecond[i]) {
                ranking++;
            } 
        }
        rankings.second = ranking;
        scores[elem] = rankings;
    }
    for (const auto& elem : scores) {
        if (elem.second.first == 2) {
            tentativeKey = rectifyKey(tentativeKey, elem.first, commonFirst);
        } else if (elem.second.second == 2) {
            tentativeKey = rectifyKey(tentativeKey, elem.first, commonSecond);
        } else if (elem.second.first == 1) {
            tentativeKey = rectifyKey(tentativeKey, elem.first, commonFirst);
        } else if (elem.second.second == 1) {
            tentativeKey = rectifyKey(tentativeKey, elem.first, commonSecond);
        }
        candidateKeys.insert(tentativeKey);
    }
    return candidateKeys;
}

// Given a CT and key length finds a key
string findKey(const string& CT, int keyLength) {
   vector<map<char, int>> unigrams = getUnigrams(CT, keyLength);
   string tentativeKey = "";
   vector<char> mostFrequent;
   for (int i = 0; i < unigrams.size(); ++i) {
        vector<pair<char, int>> letterFreqPairs(unigrams[i].begin(), unigrams[i].end());

        sort(letterFreqPairs.begin(), letterFreqPairs.end(), [](const auto& lhs, const auto& rhs) {
            return lhs.second > rhs.second; 
        });

        for (const auto& elem : letterFreqPairs) {
            mostFrequent.push_back(elem.first);
            break;
        }
    }
    string key = "";

    for (char elem : mostFrequent) {
        char potentialKeyChar = (toupper(elem) - englishAlphaRanking[0] + 26) % 26 + 'A';
        key += potentialKeyChar;
    }
    tentativeKey = key;
    string tentativePlainText = findPlainText(CT, key, key.length());
    
    map<string, int> threeLetterWords;
    int letterCount = 0;
    int overallCounter = 0;
    string temp = "";
    for (char letter : tentativePlainText) {
        if (isalpha(letter)) {
            temp += letter;
            letterCount++;
            overallCounter++;
        }
        if (!isalpha(letter)) {
            if (letterCount == 3) {
                threeLetterWords[temp] = ((overallCounter - 3 + keyLength) % keyLength );
            }
            letterCount = 0;
            temp = "";
        }
    }
    set<string> keys;
    keys = getTripletRankings(threeLetterWords, key);
    int counter = 0;
    for (const auto& key : keys) {
        if (counter == 0) {
            tentativeKey = key;
        }
        cout << findPlainText(CT, key, key.length()) << endl;
        cout << "Key: " << key << endl;
        cout << "------------------------------------------" << endl;
        counter++;
    }
    vector<string> maxBigrams(5);
    vector<map<string, int>> bigrams = getBigrams(tentativePlainText, key.length());
    for (int i = 0; i < bigrams.size(); ++i) {
        vector<pair<string, int>> letterFreqPairs(bigrams[i].begin(), bigrams[i].end());

        sort(letterFreqPairs.begin(), letterFreqPairs.end(), [](const auto& lhs, const auto& rhs) {
            return lhs.second > rhs.second; 
        });
        cout << "Most Frequent Bigrams Columns: " << i << "," << (i + 1) % keyLength << endl;
        for (const auto& elem : letterFreqPairs) {
            maxBigrams[i] = elem.first;
            cout << elem.first << " | " << elem.second << endl;
            break;
        }
    }
    /*
    string bigramFirstCol = maxBigrams[0];
    string mostCommonBigram = "TH";
    for (int i = 0; i < bigramFirstCol.length(); i++) {
        int diff = (bigramFirstCol[i] - mostCommonBigram[i] + 26) % 26;  
        key[i % key.length()] = ((key[i % key.length()] - 'A' + diff) % 26) + 'A';
    }
    tentativePlainText = findPlainText(CT, key, key.length());
    */
    return tentativeKey;
}

// Sets all plain text and cipher text into UPPER-CASE
string toUpper(string str) {
    transform(str.begin(), str.end(), str.begin(), ::toupper);
    return str;
}

// Given command line argument 1 which is cipher text and argument 2 which is key length.
int main(int argc, char* argv[]) {
    string cipherText = argv[1];
    int keyLength = atoi(argv[2]);
   
    cipherText = toUpper(cipherText);
    string key = findKey(cipherText, keyLength);
    cout << findPlainText(cipherText, key ,keyLength) << endl;

    return 0;
}

```
## References
- https://www.guballa.de/vigenere-solver

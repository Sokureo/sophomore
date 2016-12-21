CREATE TABLE text_lem (id INTEGER PRIMARY KEY, wordform VARCHAR (100), lemma VARCHAR (100));
INSERT INTO text_lem (id, wordform, lemma) values ("0", "я", "я");
INSERT INTO text_lem (id, wordform, lemma) values ("1", "пишу", "писать");
INSERT INTO text_lem (id, wordform, lemma) values ("2", "к", "к");
INSERT INTO text_lem (id, wordform, lemma) values ("3", "тебе", "ты");
INSERT INTO text_lem (id, wordform, lemma) values ("4", "в", "в");
INSERT INTO text_lem (id, wordform, lemma) values ("5", "полной", "полный");
INSERT INTO text_lem (id, wordform, lemma) values ("6", "уверенности", "уверенность");
INSERT INTO text_lem (id, wordform, lemma) values ("7", "что", "что");
INSERT INTO text_lem (id, wordform, lemma) values ("8", "мы", "мы");
INSERT INTO text_lem (id, wordform, lemma) values ("9", "никогда", "никогда");
INSERT INTO text_lem (id, wordform, lemma) values ("10", "больше", "больше");
INSERT INTO text_lem (id, wordform, lemma) values ("11", "не", "не");
INSERT INTO text_lem (id, wordform, lemma) values ("12", "увидимся", "увидеться");
INSERT INTO text_lem (id, wordform, lemma) values ("13", "несколько", "несколько");
INSERT INTO text_lem (id, wordform, lemma) values ("14", "лет", "год");
INSERT INTO text_lem (id, wordform, lemma) values ("15", "тому", "то");
INSERT INTO text_lem (id, wordform, lemma) values ("16", "назад", "назад");
INSERT INTO text_lem (id, wordform, lemma) values ("17", "расставаясь", "расставаться");
INSERT INTO text_lem (id, wordform, lemma) values ("18", "с", "с");
INSERT INTO text_lem (id, wordform, lemma) values ("19", "думала", "думать");
INSERT INTO text_lem (id, wordform, lemma) values ("20", "же", "же");
INSERT INTO text_lem (id, wordform, lemma) values ("21", "самое", "самый");
INSERT INTO text_lem (id, wordform, lemma) values ("22", "но", "но");
INSERT INTO text_lem (id, wordform, lemma) values ("23", "небу", "небо");
INSERT INTO text_lem (id, wordform, lemma) values ("24", "было", "быть");
INSERT INTO text_lem (id, wordform, lemma) values ("25", "угодно", "угодно");
INSERT INTO text_lem (id, wordform, lemma) values ("26", "испытать", "испытывать");
INSERT INTO text_lem (id, wordform, lemma) values ("27", "вторично", "вторично");
INSERT INTO text_lem (id, wordform, lemma) values ("28", "вынесла", "вынести");
INSERT INTO text_lem (id, wordform, lemma) values ("29", "этого", "этот");
INSERT INTO text_lem (id, wordform, lemma) values ("30", "испытания", "испытание");
INSERT INTO text_lem (id, wordform, lemma) values ("31", "мое", "мой");
INSERT INTO text_lem (id, wordform, lemma) values ("32", "слабое", "слабый");
INSERT INTO text_lem (id, wordform, lemma) values ("33", "сердце", "сердце");
INSERT INTO text_lem (id, wordform, lemma) values ("34", "покорилось", "покоряться");
INSERT INTO text_lem (id, wordform, lemma) values ("35", "снова", "снова");
INSERT INTO text_lem (id, wordform, lemma) values ("36", "знакомому", "знакомый");
INSERT INTO text_lem (id, wordform, lemma) values ("37", "голосу", "голос");
INSERT INTO text_lem (id, wordform, lemma) values ("38", "презирать", "презирать");
INSERT INTO text_lem (id, wordform, lemma) values ("39", "за", "за");
INSERT INTO text_lem (id, wordform, lemma) values ("40", "это", "это");
INSERT INTO text_lem (id, wordform, lemma) values ("41", "правда", "правда");
INSERT INTO text_lem (id, wordform, lemma) values ("42", "ли", "ли");
INSERT INTO text_lem (id, wordform, lemma) values ("43", "письмо", "письмо");
INSERT INTO text_lem (id, wordform, lemma) values ("44", "вместе", "вместе");
INSERT INTO text_lem (id, wordform, lemma) values ("45", "прощаньем", "прощание");
INSERT INTO text_lem (id, wordform, lemma) values ("46", "и", "и");
INSERT INTO text_lem (id, wordform, lemma) values ("47", "исповедью", "исповедь");
INSERT INTO text_lem (id, wordform, lemma) values ("48", "обязана", "обязанный");
INSERT INTO text_lem (id, wordform, lemma) values ("49", "сказать", "сказать");
INSERT INTO text_lem (id, wordform, lemma) values ("50", "все", "все");
INSERT INTO text_lem (id, wordform, lemma) values ("51", "накопилось", "накапливаться");
INSERT INTO text_lem (id, wordform, lemma) values ("52", "на", "на");
INSERT INTO text_lem (id, wordform, lemma) values ("53", "тех", "тот");
INSERT INTO text_lem (id, wordform, lemma) values ("54", "пор", "пора");
INSERT INTO text_lem (id, wordform, lemma) values ("55", "как", "как");
INSERT INTO text_lem (id, wordform, lemma) values ("56", "оно", "оно");
INSERT INTO text_lem (id, wordform, lemma) values ("57", "любит", "любить");

CREATE TABLE text (id INTEGER PRIMARY KEY, wordform VARCHAR (100), punctuation_left VARCHAR (100), punctuation_right VARCHAR (100), text_number INTEGER, id_lemma INTEGER);
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("0", "Я", " ", "", "1", "0");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("1", "пишу", "", "", "2", "1");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("2", "к", "", "", "3", "2");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("3", "тебе", "", "", "4", "3");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("4", "в", "", "", "5", "4");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("5", "полной", "", "", "6", "5");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("6", "уверенности", "", ",", "7", "6");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("7", "что", ",", "", "8", "7");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("8", "мы", "", "", "9", "8");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("9", "никогда", "", "", "10", "9");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("10", "больше", "", "", "11", "10");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("11", "не", "", "", "12", "11");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("12", "увидимся", "", ".", "13", "12");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("13", "Несколько", ".", "", "14", "13");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("14", "лет", "", "", "15", "14");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("15", "тому", "", "", "16", "15");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("16", "назад", "", ",", "17", "16");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("17", "расставаясь", ",", "", "18", "17");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("18", "с", "", "", "19", "18");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("19", "тобою", "", ",", "20", "3");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("20", "я", ",", "", "21", "0");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("21", "думала", "", "", "22", "19");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("22", "то", "", "", "23", "15");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("23", "же", "", "", "24", "20");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("24", "самое", "", ";", "25", "21");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("25", "но", ";", "", "26", "22");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("26", "небу", "", "", "27", "23");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("27", "было", "", "", "28", "24");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("28", "угодно", "", "", "29", "25");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("29", "испытать", "", "", "30", "26");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("30", "меня", "", "", "31", "0");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("31", "вторично", "", ";", "32", "27");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("32", "я", ";", "", "33", "0");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("33", "не", "", "", "34", "11");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("34", "вынесла", "", "", "35", "28");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("35", "этого", "", "", "36", "29");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("36", "испытания", "", ",", "37", "30");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("37", "мое", ",", "", "38", "31");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("38", "слабое", "", "", "39", "32");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("39", "сердце", "", "", "40", "33");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("40", "покорилось", "", "", "41", "34");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("41", "снова", "", "", "42", "35");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("42", "знакомому", "", "", "43", "36");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("43", "голосу", "", "...", "44", "37");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("44", "ты", "...", "", "45", "3");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("45", "не", "", "", "46", "11");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("46", "будешь", "", "", "47", "24");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("47", "презирать", "", "", "48", "38");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("48", "меня", "", "", "49", "0");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("49", "за", "", "", "50", "39");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("50", "это", "", ",", "51", "40");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("51", "не", ",", "", "52", "11");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("52", "правда", "", "", "53", "41");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("53", "ли", "", "?", "54", "42");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("54", "Это", "?", "", "55", "29");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("55", "письмо", "", "", "56", "43");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("56", "будет", "", "", "57", "24");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("57", "вместе", "", "", "58", "44");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("58", "прощаньем", "", "", "59", "45");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("59", "и", "", "", "60", "46");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("60", "исповедью", "", ":", "61", "47");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("61", "я", ":", "", "62", "0");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("62", "обязана", "", "", "63", "48");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("63", "сказать", "", "", "64", "49");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("64", "тебе", "", "", "65", "3");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("65", "все", "", ",", "66", "50");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("66", "что", ",", "", "67", "7");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("67", "накопилось", "", "", "68", "51");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("68", "на", "", "", "69", "52");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("69", "моем", "", "", "70", "31");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("70", "сердце", "", "", "71", "33");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("71", "с", "", "", "72", "18");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("72", "тех", "", "", "73", "53");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("73", "пор", "", ",", "74", "54");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("74", "как", ",", "", "75", "55");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("75", "оно", "", "", "76", "56");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("76", "тебя", "", "", "77", "3");
INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("77", "любит", "", ".", "78", "57");

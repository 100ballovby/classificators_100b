train_spam = ['send your password', 'send us your account details',
              'subscribe to our newsletter', 'you have received a large inheritance',
              'review our website', 'send and sms', 'subscribe newsletter']
train_ham = ['your activity report', 'benefits physical activity', 'the important vows',
             'view you stats', 'renew subscription']
test_email = {
    'spam': ['renew your password', 'renew your account'],
    'ham': ['benefits of your account', 'the importance of physical activity']
}


# сделаем словарь уникальных слов, которые появлялись в спам-сообщениях (о которых известно)
spam_dict = []
for sentence in train_spam:
    sentence_list = sentence.split()
    for word in sentence_list:
        spam_dict.append(word)

unique_spam_dict = list(dict.fromkeys(spam_dict))
print(unique_spam_dict)

dict_spamicity = {}
for word in unique_spam_dict:
    emails_with_word = 0
    for sentence in train_spam:  # перебор всех спамных сообщений
        if word in sentence:  # если слово встречается в спамном сообщении
            emails_with_word += 1  # "посчитать" это письмо
    total_spam = len(train_spam)
    spamicity = (emails_with_word + 1) / (total_spam + 2)
    dict_spamicity[word.lower()] = spamicity

print(dict_spamicity)


# рассчитываю хамисити (чистоту) для слов из тренировочного набора
ham_dict = []
for sentence in train_ham:
    sentence_list = sentence.split()
    for word in sentence_list:
        ham_dict.append(word)

unique_ham_dict = list(dict.fromkeys(ham_dict))
print(unique_ham_dict)

dict_hamicity = {}
for word in unique_ham_dict:
    emails_with_word = 0
    for sentence in train_ham:  # перебор всех хамных сообщений
        if word in sentence:  # если слово встречается в хамном сообщении
            emails_with_word += 1  # "посчитать" это письмо
    total_ham = len(train_spam)
    hamicity = (emails_with_word + 1) / (total_ham + 2)
    dict_hamicity[word.lower()] = hamicity

print(dict_hamicity)


# считаю вероятность спама (априорная/классическая)
prob_spam = len(train_spam) / (len(train_spam) + len(train_ham))
print(prob_spam)
# считаю вероятность хама (априорная/классическая)
prob_ham = len(train_ham) / (len(train_spam) + len(train_ham))
print(prob_ham)


test = []
for i in test_email['spam']:
    test.append(i)

for i in test_email['ham']:
    test.append(i)

# разбить имейлы на отдельные слова
distinct_words_from_email = []
for sentence in test:
    sentence_as_list = sentence.split()
    senten = []
    for word in sentence_as_list:
        senten.append(word)
    distinct_words_from_email.append(senten)


test_spam_labeled = [distinct_words_from_email[0], distinct_words_from_email[1]]
test_ham_labeled = [distinct_words_from_email[2], distinct_words_from_email[3]]

# игнорить слова, которые ни разу не встречались в тестовых данных
reduced_spam_test = []
for sentence in test_spam_labeled:
    _words = []
    for word in sentence:
        if word in unique_spam_dict:
            _words.append(word)
        elif word in unique_ham_dict:
            _words.append(word)
    reduced_spam_test.append(_words)

reduced_ham_test = []
for sentence in test_ham_labeled:
    _words = []
    for word in sentence:
        if word in unique_ham_dict:
            _words.append(word)
        elif word in unique_spam_dict:
            _words.append(word)
    reduced_spam_test.append(_words)

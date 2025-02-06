from journal import Journal

#===================================================================================================

mathematical_modeling = Journal('Математическое Моделирование',      '0234-0879', '',          '3', 'К~', '', '',   '', '3595', 'se:00002821|00007173', '', '', '', '', '', '+', '+', '+', 'https://www.mathnet.ru/php/journal.phtml?jrnid=mm&option_lang=rus')
lncs =                  Journal('Lecture Notes in Computer Science', '0302-9743', '1611-3349', '',  '',   '', 'Q3', '', '',     '',                     '', '', '', '', '', '+', '',  '',  'https://www.springer.com/de/it-informatik/lncs')

all = \
[
    mathematical_modeling, lncs
]

#===================================================================================================

if __name__ == '__main__':
    for j in all:
        print(j)

#===================================================================================================

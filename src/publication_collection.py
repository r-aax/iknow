from publication import Publication as Pub
import person_collection as pc
import person_private_collection as ppc
import job_place_collection as jpc
import job_place_private_collection as jppc
import journal_collection as jc

#===================================================================================================

nrcki_2025 = \
[
    Pub([(pc.potashev_ka, [jpc.kfu_imm, jpc.kgeu]), (ppc.uraimov_aa, [jpc.kfu_imm, jppc.nrcki]), (pc.mazo_ab, [jpc.kfu_imm])],
        'Определение длин трещин многозонного гидроразрыва пласта с помощью модели фильтрации в трубках тока.',
        jc.mathematical_modeling, 2025, '37', '1', '131-150',
        '10.20948/mm-2025-01-08', '',
        'Работа выполнена при финансовой поддержке Научно-исследовательского центра “Курчатовский институт” в рамках государственного задания (номер проекта FNEF-2022-0016).',
        'ru'),
    Pub([(ppc.baranov_av, [jpc.niisi_jscc, jppc.nrcki]), (ppc.aladyshev_os, [jpc.niisi_jscc, jppc.nrcki]), (ppc.bragin_ka, [jpc.niisi_jscc, jppc.nrcki])],
        'Job mapping cyclic composite algorithm for supercomputer resource manager.',
        jc.lncs, 2025, '15406', '', '377-389',
        '10.1007/978-3-031-78459-0_27', 'https://link.springer.com/chapter/10.1007/978-3-031-78459-0_27',
        'The research was carried out as part of government assignment of the National Research Centre «Kurchatov Institute».',
        'en')
]

#===================================================================================================

if __name__ == '__main__':
    for p in nrcki_2025:
        print(p)

#===================================================================================================

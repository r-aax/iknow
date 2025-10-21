import worksheet_private_collection as wc
import temporary_team_private_collection as ttc
import person
import complex_theme_private_collection as cx
import generator_word as gw
import publication_collection as pc
import generator_html as gh

#===================================================================================================

def print_worksheets_statitics():
    """
    Print worksheet statistics.
    """

    #print(f'ОССиПВ штатное расписание:')
    #wc.osspv.print()
    #print(f'ОВК штатное расписание:')
    #wc.kvvk_ovk.print()

    osspv_all = wc.osspv.slots_sum()
    osspv_occupied = wc.osspv.occupied_slots_sum()
    kvvk_ovk_all = wc.kvvk_ovk.slots_sum()
    kvvk_ovk_occupied = wc.kvvk_ovk.occupied_slots_sum()

    print(f'Статистика по ставкам:')
    print(f'\tОССиПВ : занято {osspv_occupied} из {osspv_all}'
          f', ОВК : занято {kvvk_ovk_occupied} из {kvvk_ovk_all}'
          f', всего : {osspv_occupied + kvvk_ovk_occupied}')

#---------------------------------------------------------------------------------------------------

def print_temporary_teams_statistics():
    """
    Print temporary teams statistics.
    """

    cx1_slots = ttc.cx1.slots_sum()
    cx2_slots = ttc.cx2.slots_sum()
    oth_slots = ttc.other.slots_sum()

    print(f'Статистика по временному трудовому коллективу:')
    print(f'\t6Ф-СИ.1 : {cx1_slots}, 6Ф-СИ.2 : {cx2_slots}, другие : {oth_slots}'
          f', всего : {cx1_slots + cx2_slots + oth_slots}')

#===================================================================================================

if __name__ == '__main__':

    # statistics
    print_worksheets_statitics()
    print_temporary_teams_statistics()

    """
    ps1, ps2 = ttc.cx1.people(), ttc.cx2.people()
    print(f'Статистика по ставкам:\n'
          f'\tОССиПВ = {wc.osspv.slots_sum()}, ОВК = {wc.kvvk_ovk.slots_sum()}, '
          f'всего доступно {wc.all.slots_sum()}\n'
          f'\tтема 6Ф-СИ.1 = {ttc.cx1.slots_sum()}, тема 6Ф-СИ.2 = {ttc.cx2.slots_sum()}, '
          f'не задействовано в темах {ttc.other.slots_sum()}')
    print(f'Статистика по среднему возрасту:\n'
          f'\tтема 6Ф-СИ.1 = {person.mean_age_in_the_end_of_year(ps1)}, '
          f'тема 6Ф-СИ.2 = {person.mean_age_in_the_end_of_year(ps2)}')
    print(f'Статистика по проценту молодых:\n'
          f'\tтема 6Ф-СИ.1 = {person.percent_le_age_in_the_end_of_year(ps1, 39)}, '
          f'тема 6Ф-СИ.2 = {person.percent_le_age_in_the_end_of_year(ps2, 39)}')
    """

    # temporary teams
    gw.generate_temporary_team(4, cx.cx1, ttc.cx1, 2025, '../out/6Ф-СИ.1-приложение-4-коллектив')
    gw.generate_temporary_team(4, cx.cx2, ttc.cx2, 2025, '../out/6Ф-СИ.2-приложение-4-коллектив')

    # plans
    gh.generate_publications_info(pc.nrcki_2025, '../out/publications_2025.html')
    gh.generate_plan(cx.cx1, '../out/plan_6f_si_1.html', year_to=2028)
    gh.generate_plan(cx.cx2, '../out/plan_6f_si_2.html', year_to=2028)

    #

    tab = []
    cxx = []
    for lin in ttc.cx1.lines:
        cxx.append(lin)
        tab.append(lin.employee.tabel)
    for lin in ttc.cx2.lines:
        if not lin.employee.tabel in tab:
            cxx.append(lin)
            tab.append(lin.employee.tabel)

    lines = [lin for lin in cxx if (lin.status == 'осн.')]

    for lin in lines:
        print(lin)

    print('всего', len(lines))

#===================================================================================================

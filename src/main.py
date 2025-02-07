import worksheet_private_collection as wc
import temporary_team_private_collection as ttc
import person
import complex_theme_private_collection as cx
import generator_word as gw
import publication_collection as pc
import generator_html as gh

#===================================================================================================

if __name__ == '__main__':

    """
    print(wc.osspv.occupied_slots_sum(), wc.kvvk_ovk.occupied_slots_sum())
    print(ttc.cx1.slots_sum(), ttc.cx2.slots_sum(), ttc.other.slots_sum())

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

    gw.generate_temporary_team(4, cx.cx1, ttc.cx1, 2025, '../out/6Ф-СИ.1-приложение-4-коллектив')
    gw.generate_temporary_team(4, cx.cx2, ttc.cx2, 2025, '../out/6Ф-СИ.2-приложение-4-коллектив')
    """

    gh.generate_publications_info(pc.nrcki_2025, '../out/publications_2025.html')
    gh.generate_plan(cx.cx1, '../out/plan_6f_si_1.html')
    gh.generate_plan(cx.cx2, '../out/plan_6f_si_2.html')

#===================================================================================================

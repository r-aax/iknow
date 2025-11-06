import worksheet_private_collection as wc
import temporary_team_private_collection as ttc
import complex_theme_private_collection as cx
import generator_word as gw
import generator_excel as ge
import publication_collection as pc
import generator_html as gh

#===================================================================================================

def print_worksheets_statitics():
    """
    Print worksheet statistics.
    """

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

#---------------------------------------------------------------------------------------------------

def generate_documents_pack(y, out_dir):
    """
    Generate documents pack.

    Parameters
    ----------
    y : int
        Start year.
    out_dir : str
        Out directory.
    """

    for (theme, team) in [(cx.cx1, ttc.cx1), (cx.cx2, ttc.cx2)]:
        pre = f'{out_dir}/{theme.short_title}'

        # Supplement 1 - technical task.
        gw.generate_technical_task(1, theme, y, f'{pre}-приказ-приложение-1-ТЗ')

        # Supplement 4 - temporary team.
        gw.generate_temporary_team(4, theme, team, y, f'{pre}-приказ-приложение-4-коллектив')

        # Supplement 5 - equipment.
        gw.generate_equipment(5, theme, f'{pre}-приказ-приложение-5-оборудование')

        # PTNI forms.
        ge.generate_PTNI_performers(team, f'{pre}-ПТНИ-исполнители')

#===================================================================================================

if __name__ == '__main__':

    # statistics
    print_worksheets_statitics()
    print_temporary_teams_statistics()

    # plans
    gh.generate_publications_info(pc.nrcki_2025, '../out/publications_2025.html')
    gh.generate_plan(cx.cx1, '../out/plan_6f_si_1.html', year_to=2029)
    gh.generate_plan(cx.cx2, '../out/plan_6f_si_2.html', year_to=2029)

    # generate documents for complex themes
    generate_documents_pack(2026, '../out/orders')

#===================================================================================================

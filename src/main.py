import worksheet_private_collection as wc
import temporary_team_private_collection as ttc
import complex_theme_private_collection as cx
from generator_word import GeneratorWord as gw
import generator_excel as ge
import publication_collection as pc
import generator_html as gh
import generator_word

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

        # Form gos assignment (supplements 7 - 11).
        #gw.generate_form_gos_assignment_suppl_07_technical_task(theme, y, f'{pre}-пре-1-ТЗ')
        gw.generate_form_gos_assignment_suppl_08_calendar_plan(theme, y, f'{pre}-пре-2-КП')

#===================================================================================================

if __name__ == '__main__':

    # plans
    #gh.generate_publications_info(pc.nrcki_2025, '../out/publications_2025.html')
    gh.generate_plan(cx.cx1, '../out/plan_6f_si_1.html', year_from=2025, year_to=2029)
    gh.generate_plan(cx.cx2, '../out/plan_6f_si_2.html', year_from=2025, year_to=2029)

    # generate documents for complex themes
    generate_documents_pack(2027, '../out/docs')

#===================================================================================================

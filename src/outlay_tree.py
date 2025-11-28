
#===================================================================================================

class Nod:
    """
    Node of tree.
    """

    #-----------------------------------------------------------------------------------------------

    def __init__(self, label, name):
        """
        Constructor.

        Parameters
        ----------
        label : str
            Label.
        name : str
            Name.
        """

        self.label = label
        self.name = name
        self.money = 0.0
        self.ch = []

    #-----------------------------------------------------------------------------------------------

    @property
    def xmoney(self):
        """
        Get extended money.

        Returns
        -------
        float
            Extended money.
        """

        if self.ch == []:
            return self.money
        else:
            return sum(c.xmoney for c in self.ch)

    #-----------------------------------------------------------------------------------------------

    def __repr__(self):
        """
        String representation.

        Returns
        -------
        str
            String representation.
        """

        return f'{self.label} {self.name} : {self.xmoney}'

    #-----------------------------------------------------------------------------------------------

    def __getitem__(self, s):
        """
        Get item.

        Parameters
        ----------
        s : str
            Index.

        Returns
        -------
        Nod
            Child.
        """

        if s == 'II':
            return self.ch[0]
        elif s == 'III':
            return self.ch[1]
        else:
            return self.ch[s - 1]

    #-----------------------------------------------------------------------------------------------

    def count(self):
        """
        Count.

        Returns
        -------
        int
            Count of elements (including self).
        """

        return 1 + sum([c.count() for c in self.ch])

    #-----------------------------------------------------------------------------------------------

    def add(self, n):
        """
        Add new child.

        Parameters
        ----------
        n : Nod
            Node.

        Returns
        -------
        Nod
            New node.
        """

        self.ch.append(n)

        return n

    #-----------------------------------------------------------------------------------------------

    def print(self, off=0):
        """
        Print tree.

        Parameters
        ----------
        off : int
            Offset.
        """

        pre = ' ' * (2 * off)

        print(f'{pre}{self}')

        for c in self.ch:
            c.print(off + 1)

    #-----------------------------------------------------------------------------------------------

    def flatten(self):
        """
        Get all nodes in flatten view.

        Returns
        -------
        [Nod]
            List of nodes.
        """

        if self.ch == []:
            return [self]

        f = [self]

        for c in self.ch:
            f = f + c.flatten()

        return f

#===================================================================================================

def create_outlay_skeleton(obj):
    """
    Create outlay.

    Parameters
    ----------
    obj : str
        Object for outlay.

    Returns
    -------
    Nod
        Outlay root node.
    """

    pI = Nod('I.', f'ВСЕГО по {obj}, в том числе:')
    pII = pI.add(Nod('II.', 'Прямые и общепроизводственные затраты'))
    pII1 = pII.add(Nod('1.', 'Затраты на оплату труда работников и начисления на выплаты по оплате труда работников, в том числе:'))
    pII11 = pII1.add(Nod('1.1.', 'Затраты на оплату труда работников, непосредственно связанных с выполнением работы, и начисления на выплаты по оплате труда работников, непосредственно связанных с выполнением работы, которые определяются исходя из показателей необходимых трудовых ресурсов (трудозатрат), рассчитываемых с учетом длительности выполнения научной темы по направлению научного исследования, состава, квалификации и численности работников, участвующих в выполнении научной темы, исчисляемых в человеко-месяцах'))
    pII12 = pII1.add(Nod('1.2', 'Затраты на оплату труда работников, которые не принимают непосредственного участия в выполнении работы, и начисления на выплаты по оплате труда работников, которые не принимают непосредственного участия в выполнении работы, включая административно-управленческий персонал'))
    pII2 = pII.add(Nod('2.', 'Затраты на приобретение материальных запасов и на приобретение движимого имущества (основных средств и нематериальных активов), используемого в процессе выполнения работы, с учетом срока его полезного использования, а также затраты на аренду указанного имущества, в том числе:'))
    pII21 = pII2.add(Nod('2.1.', 'Затраты на приобретение материальных запасов'))
    pII22 = pII2.add(Nod('2.2.', 'Затраты на приобретение движимого имущества (основных средств и нематериальных активов)'))
    pII23 = pII2.add(Nod('2.3.', 'Затраты на аренду движимого имущества (основных средств и нематериальных активов)'))
    pII3 = pII.add(Nod('3.', 'Затраты на иные расходы, непосредственно связанные с выполнением работы, в том числе:'))
    pII31 = pII3.add(Nod('3.1.', 'Командировочные расходы'))
    pII32 = pII3.add(Nod('3.2.', 'Затраты на закупку работ, выполняемых сторонними организациями'))
    pII33 = pII3.add(Nod('3.3.', 'Затраты на закупку услуг, выполняемых сторонними организациями'))
    pII34 = pII3.add(Nod('3.4.', 'Затраты на повышение квалификации и обучение'))
    pII35 = pII3.add(Nod('3.5.', 'Затраты на участие в выставках, конференциях и иных мероприятиях'))
    pII36 = pII3.add(Nod('3.6.', 'Иные расходы, не указанные в пунктах 3.1.-3.5. (указать)'))
    pII4 = pII.add(Nod('4.', 'Общепроизводственные затраты на содержание и аренду объектов недвижимого имущества, необходимого для выполнения государственного задания'))
    pII41 = pII4.add(Nod('4.1.', 'Затраты на содержание объектов недвижимого имущества'))
    pII42 = pII4.add(Nod('4.2.', 'Затраты на аренду объектов недвижимого имущества'))
    pII5 = pII.add(Nod('5.', 'Общепроизводственные затраты на содержание объектов особо ценного движимого имущества и имущества, необходимого для выполнения государственного задания, а также затраты на аренду указанного имущества'))
    pII51 = pII5.add(Nod('5.1.', 'Затраты на содержание объектов особо ценного движимого имущества и имущества, необходимого для выполнения государственного задания,'))
    pII52 = pII5.add(Nod('5.2.', 'Затраты на аренду объектов особо ценного движимого имущества и имущества, необходимого для выполнения государственного задания,'))
    pII6 = pII.add(Nod('6.', 'Общепроизводственные затраты на приобретение услуг связи'))
    pII7 = pII.add(Nod('7.', 'Общепроизводственные затраты на приобретение транспортных услуг'))
    pII8 = pII.add(Nod('8.', 'Затраты на прочие общепроизводственные нужды'))
    pIII = pI.add(Nod('III.', 'Общехозяйственные затраты'))
    pIII1 = pIII.add(Nod('1.', 'Затраты на оплату труда работников и начисления на выплаты по оплате труда работников, в том числе:'))
    pIII11 = pIII1.add(Nod('1.1.', 'Затраты на оплату труда работников, которые не принимают непосредственного участия в выполнении работы, и начисления на выплаты по оплате труда работников, которые не принимают непосредственного участия в выполнении работы, включая административно-управленческий персонал'))
    pIII2 = pIII.add(Nod('2.', 'Общехозяйственные затраты на содержание и аренду объектов недвижимого имущества, необходимого для выполнения государственного задания'))
    pIII21 = pIII2.add(Nod('2.1.', 'Затраты на содержание объектов недвижимого имущества'))
    pIII22 = pIII2.add(Nod('2.2.', 'Затраты на аренду объектов недвижимого имущества'))
    pIII3 = pIII.add(Nod('3.', 'Общехозяйственные затраты на содержание объектов особо ценного движимого имущества и имущества, необходимого для выполнения государственного задания, а также затраты на аренду указанного имущества'))
    pIII31 = pIII3.add(Nod('3.1.', 'Затраты на содержание объектов особо ценного движимого имущества и имущества, необходимого для выполнения государственного задания,'))
    pIII32 = pIII3.add(Nod('3.2.', 'Затраты на аренду объектов особо ценного движимого имущества и имущества, необходимого для выполнения государственного задания,'))
    pIII4 = pIII.add(Nod('4.', 'Общехозяйственные затраты на приобретение услуг связи'))
    pIII5 = pIII.add(Nod('5.', 'Общехозяйственные затраты на приобретение транспортных услуг'))
    pIII6 = pIII.add(Nod('6.', 'Затраты на оплату коммунальных услуг'))
    pIII7 = pIII.add(Nod('7.', 'Затраты на прочие общехозяйственные нужды'))

    return pI

#---------------------------------------------------------------------------------------------------

def create_outlay(obj, pII11, pII12, pII21, pII22, pII23,
                  pII31, pII32, pII33, pII34, pII35, pII36,
                  pII41, pII42, pII51, pII52, pII6, pII7, pII8,
                  pIII11, pIII21, pIII22, pIII31, pIII32, pIII4, pIII5, pIII6, pIII7):
    """
    Create outlay.

    Parameters
    ----------
    obj : str
        Object for outlay.
    pII11 : float
        Value II.1.1.
    pII12 : float
        Value II.1.2.
    pII21 : float
        Value II.2.1.
    pII22 : float
        Value II.2.2.
    pII23 : float
        Value II.2.3.
    pII31 : float
        Value II.3.1.
    pII32 : float
        Value II.3.2.
    pII33 : float
        Value II.3.3.
    pII34 : float
        Value II.3.4.
    pII35 : float
        Value II.3.5.
    pII36 : float
        Value II.3.6.
    pII41 : float
        Value II.4.1.
    pII42 : float
        Value II.4.2.
    pII51 : float
        Value II.5.1.
    pII52 : float
        Value II.5.2.
    pII6 : float
        Velue II.6.
    pII7 : float
        Value II.7.
    pII8 : float
        Value II.8.
    pIII11 : float
        Value III.1.1.
    pIII21 : float
        Value III.2.1.
    pIII22 : float
        Value III.2.2.
    pIII31 : float
        Value III.3.1.
    pIII32 : float
        Value III.3.2.
    pIII4 : float
        Value III.4.
    pIII5 : float
        Value III.5.
    pIII6 : float
        Value III.6.
    pIII7 : float
        Value III.7.

    Returns
    -------
    Nod
        Outlay node.
    """

    t = create_outlay_skeleton(obj)

    t['II'][1][1].money = pII11
    t['II'][1][2].money = pII12
    t['II'][2][1].money = pII21
    t['II'][2][2].money = pII22
    t['II'][2][3].money = pII23
    t['II'][3][1].money = pII31
    t['II'][3][2].money = pII32
    t['II'][3][3].money = pII33
    t['II'][3][4].money = pII34
    t['II'][3][5].money = pII35
    t['II'][3][6].money = pII36
    t['II'][4][1].money = pII41
    t['II'][4][2].money = pII42
    t['II'][5][1].money = pII51
    t['II'][5][2].money = pII52
    t['II'][6].money = pII6
    t['II'][7].money = pII7
    t['II'][8].money = pII8
    t['III'][1][1].money = pIII11
    t['III'][2][1].money = pIII21
    t['III'][2][2].money = pIII22
    t['III'][3][1].money = pIII31
    t['III'][3][2].money = pIII32
    t['III'][4].money = pIII4
    t['III'][5].money = pIII5
    t['III'][6].money = pIII6
    t['III'][7].money = pIII7

    return t

#---------------------------------------------------------------------------------------------------

def duplicate_outlay(t, obj, part):
    """
    Duplicate outlay.

    Parameters
    ----------
    t : Nod
        Outlay.
    obj : str
        New object for outlay.
    part : float
        Part for extract.

    Returns
    -------
    Nod
        New outlay.
    """

    return create_outlay(obj,
                         t['II'][1][1].money * part,
                         t['II'][1][2].money * part,
                         t['II'][2][1].money * part,
                         t['II'][2][2].money * part,
                         t['II'][2][3].money * part,
                         t['II'][3][1].money * part,
                         t['II'][3][2].money * part,
                         t['II'][3][3].money * part,
                         t['II'][3][4].money * part,
                         t['II'][3][5].money * part,
                         t['II'][3][6].money * part,
                         t['II'][4][1].money * part,
                         t['II'][4][2].money * part,
                         t['II'][5][1].money * part,
                         t['II'][5][2].money * part,
                         t['II'][6].money * part,
                         t['II'][7].money * part,
                         t['II'][8].money * part,
                         t['III'][1][1].money * part,
                         t['III'][2][1].money * part,
                         t['III'][2][2].money * part,
                         t['III'][3][1].money * part,
                         t['III'][3][2].money * part,
                         t['III'][4].money * part,
                         t['III'][5].money * part,
                         t['III'][6].money * part,
                         t['III'][7].money * part)

#---------------------------------------------------------------------------------------------------

def duplicate_outlay_each_line(t, obj,
                               pII11, pII12, pII21, pII22, pII23,
                               pII31, pII32, pII33, pII34, pII35, pII36,
                               pII41, pII42, pII51, pII52, pII6, pII7, pII8,
                               pIII11, pIII21, pIII22, pIII31, pIII32, pIII4, pIII5, pIII6, pIII7):
    """
    Duplicate outline with each line part given.

    Parameters
    ----------
    t : Nod
        Tree.
    obj : str
        Object description.
    pII11 : float
        Part for line.
    pII12 : float
        Part for line.
    pII21 : float
        Part for line.
    pII22 : float
        Part for line.
    pII23 : float
        Part for line.
    pII31 : float
        Part for line.
    pII32 : float
        Part for line.
    pII33 : float
        Part for line.
    pII34 : float
        Part for line.
    pII35 : float
        Part for line.
    pII36 : float
        Part for line.
    pII41 : float
        Part for line.
    pII42 : float
        Part for line.
    pII51 : float
        Part for line.
    pII52 : float
        Part for line.
    pII6 : float
        Part for line.
    pII7 : float
        Part for line.
    pII8 : float
        Part for line.
    pIII11 : float
        Part for line.
    pIII21 : float
        Part for line.
    pIII22 : float
        Part for line.
    pIII31 : float
        Part for line.
    pIII32 : float
        Part for line.
    pIII4 : float
        Part for line.
    pIII5 : float
        Part for line.
    pIII6 : float
        Part for line.
    pIII7 : float
        Part for line.

    Returns
    -------
    Nod
        New outline.
    """

    return create_outlay(obj,
                         t['II'][1][1].money * pII11,
                         t['II'][1][2].money * pII12,
                         t['II'][2][1].money * pII21,
                         t['II'][2][2].money * pII22,
                         t['II'][2][3].money * pII23,
                         t['II'][3][1].money * pII31,
                         t['II'][3][2].money * pII32,
                         t['II'][3][3].money * pII33,
                         t['II'][3][4].money * pII34,
                         t['II'][3][5].money * pII35,
                         t['II'][3][6].money * pII36,
                         t['II'][4][1].money * pII41,
                         t['II'][4][2].money * pII42,
                         t['II'][5][1].money * pII51,
                         t['II'][5][2].money * pII52,
                         t['II'][6].money * pII6,
                         t['II'][7].money * pII7,
                         t['II'][8].money * pII8,
                         t['III'][1][1].money * pIII11,
                         t['III'][2][1].money * pIII21,
                         t['III'][2][2].money * pIII22,
                         t['III'][3][1].money * pIII31,
                         t['III'][3][2].money * pIII32,
                         t['III'][4].money * pIII4,
                         t['III'][5].money * pIII5,
                         t['III'][6].money * pIII6,
                         t['III'][7].money * pIII7)

#===================================================================================================

if __name__ == '__main__':
    pass

#===================================================================================================
